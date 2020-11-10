#! /usr/bin/env python3

""" Runs External Programs/Scripts as child processes, supplies Input(s) and evaluates their output
    Supports only programs that use STDIN, STDOUT and STDERR

    Popen works in Text Mode
    """

from subprocess import Popen, PIPE, STDOUT, TimeoutExpired
from resource import getrusage, RUSAGE_CHILDREN


def evaluate(cmd: str, testcase=PIPE, text: str = "", wd: str = None) -> list:
    """Gives input to the child process and returns the child process details:
    runtime, memory usage, stdout, stderr.
    'cmd' command with args to be executed
    'testcase' open file object
    'text' is alternative input
    'wd' is the working directory for the child process
    """

    with Popen(cmd, cwd=wd, shell=True, stdin=testcase, stdout=PIPE, stderr=PIPE, text=True) as proc:

        if testcase == PIPE:
            proc.stdin.write(text + '\n')

        try:
            # Commuication must be started for the child process to proceed and terminate
            # and for waiting and data streams to work
            output, error = proc.communicate(timeout=30)
        except TimeoutExpired:
                proc.wait()
                output, error = proc.stdout.read(), proc.stderr.read()

        res_usage = getrusage(RUSAGE_CHILDREN)
        # runtime is user + system
        runtime = round(sum(res_usage[0:2]), 6)
        mem_usage = res_usage[2]  # kiloBytes  # Max among all child processes spawned

    return [runtime, mem_usage, output, error]

