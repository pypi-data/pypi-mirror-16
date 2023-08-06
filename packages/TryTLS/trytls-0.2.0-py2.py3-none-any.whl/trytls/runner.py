from __future__ import print_function, unicode_literals

import os
import sys
import argparse
import subprocess
from colorama import Fore, Back, Style, init, AnsiToWin32

from . import __version__, gencert, utils, result, bundles


# Initialize colorama without wrapping sys.stdout globally
init(wrap=False)
wrapped_stdout = AnsiToWin32(sys.stdout, autoreset=True).stream


def output(format_string="", **kwargs):
    keys = dict(Fore=Fore, Back=Back, Style=Style, RESET=Style.RESET_ALL)
    keys.update(kwargs)
    print(format_string.format(**keys), file=wrapped_stdout)


class Unsupported(Exception):
    pass


class ProcessFailed(Exception):
    pass


class UnexpectedOutput(Exception):
    pass


def indent(text, by=4, first_line=True):
    r"""
    >>> indent("a\nb\nc", by=1) == ' a\n b\n c'
    True
    """

    spaces = " " * by
    lines = text.splitlines(True)
    prefix = lines.pop(0) if (lines and not first_line) else ""
    return prefix + "".join(spaces + line for line in lines)


def output_info(args, openssl_version, runner_name="trytls"):
    output(
        "{Style.BRIGHT}platform:{RESET} {platform}",
        platform=utils.platform_info()
    )
    output(
        "{Style.BRIGHT}runner:{RESET} {runner} {version} ({python}, {openssl})",
        runner=runner_name,
        version=__version__,
        python=utils.python_info(),
        openssl=openssl_version
    )
    output(
        "{Style.BRIGHT}stub:{RESET} {command}",
        command=utils.format_command(args)
    )


def run_one(args, host, port, cafile=None):
    args = args + [host, str(port)]
    if cafile is not None:
        args.append(cafile)

    try:
        process = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
    except OSError as ose:
        raise ProcessFailed("failed to launch the stub", os.strerror(ose.errno))

    out, _ = process.communicate()
    if process.returncode != 0:
        raise ProcessFailed("stub exited with return code {}".format(process.returncode), out)

    out = out.rstrip()
    lines = out.splitlines()
    if lines:
        verdict = lines.pop()
        if verdict == b"ACCEPT":
            return True, "".join(lines)
        elif verdict == b"REJECT":
            return False, "".join(lines)
        elif verdict == b"UNSUPPORTED":
            raise Unsupported("".join(lines))
    raise UnexpectedOutput(out)


def collect(args, tests):
    for env in tests:
        with env() as test:
            try:
                accept, details = run_one(list(args), test.host, test.port, test.cafile)
            except Unsupported as us:
                yield test, result.Skip(details=us.args[0])
            except UnexpectedOutput as uo:
                output = uo.args[0].strip()
                if output:
                    yield test, result.Error("unexpected output", output)
                else:
                    yield test, result.Error("no output")
            except ProcessFailed as pf:
                yield test, result.Error(pf.args[0], pf.args[1])
            else:
                if accept and test.accept:
                    yield test, result.Pass(details=details)
                elif not accept and not test.accept:
                    yield test, result.Pass(details=details)
                elif not accept and test.accept:
                    yield test, result.Fail(details=details)
                else:
                    yield test, result.Fail(details=details)


class Formatter(object):
    def __init__(self, base="", type="", reason="", details=""):
        self.base = base
        self.type = type
        self.reason = reason
        self.details = details

    def format(self, test, res):
        template = self.base
        reset = "{RESET}"

        template += self.type + res.name.rjust(5) + reset + self.base + " "
        template += test.description
        template += " {Style.DIM}" + "[{accept} {name}]".format(
            name=test.name,
            accept="accept" if test.accept else "reject"
        )

        if res.reason.rstrip():
            template += reset + self.base + "\n" + indent("reason: " + self.reason + res.reason.rstrip(), by=6)
        if res.details.rstrip():
            template += reset + self.base + "\n" + indent("output: ", by=6) + self.details + indent(res.details.rstrip(), by=14, first_line=False)

        return template


formats = {
    result.Skip: Formatter(
        base="{Style.DIM}"
    ),
    result.Error: Formatter(
        base="{Fore.RED}",
        type="{Back.RED}{Fore.WHITE}",
        details="{Style.DIM}"
    ),
    result.Fail: Formatter(
        base="{Fore.RED}",
        reason="{Fore.RED}{Style.DIM}"
    ),
    result.Pass: Formatter(
        type="{Fore.GREEN}",
        reason="{Style.DIM}",
        details="{Style.DIM}"
    )
}


def format_result(test, res):
    formatter = formats.get(res.type)
    if formatter is None:
        raise RuntimeError("unknown result type")
    return formatter.format(test, res)


def run(args, tests):
    fail_count = 0
    error_count = 0

    for test, res in collect(args, tests):
        output(format_result(test, res))

        if res.type == result.Fail:
            fail_count += 1
        elif res.type == result.Error:
            error_count += 1

    return fail_count == 0 and error_count == 0


def main():
    try:
        openssl_version = gencert.openssl_version()
    except gencert.OpenSSLNotFound as err:
        output("{Back.RED}{Fore.WHITE}ERROR:{RESET} {error}", error=err)
        return 1

    parser = argparse.ArgumentParser(
        usage="%(prog)s bundle command [arg ...]"
    )
    parser.add_argument(
        "remainder",
        help=argparse.SUPPRESS,
        nargs=argparse.REMAINDER
    )

    args = parser.parse_args()
    if args.remainder and args.remainder[0] == "--":
        args.remainder.pop(0)
    bundle_name = args.remainder[0] if args.remainder else None

    args = parser.parse_args(args.remainder[1:], args)
    if args.remainder and args.remainder[0] == "--":
        args.remainder.pop(0)
    command = args.remainder

    if bundle_name is None:
        bundle_list = sorted(bundles.iter_bundles())
        parser.error("missing the bundle argument\n\nValid bundle options:\n" + indent("\n".join(bundle_list), 2))

    bundle = bundles.load_bundle(bundle_name)
    if bundle is None:
        parser.error("unknown bundle '{}'".format(bundle_name))

    if not command:
        parser.error("too few arguments, missing command")

    output_info(command, openssl_version=openssl_version)
    if not run(command, bundle):
        # Return with a non-zero exit code if all tests were not successful. The
        # CPython interpreter exits with 1 when an unhandled exception occurs,
        # and with 2 when there is a problem with a command line parameter. The
        # argparse module also uses the code 2 for the same purpose. Therefore
        # the chosen return value here is 3.
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
