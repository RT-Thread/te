"""
testcase example
"""

import qemubox
import pexpect

def run(box):
    qemubox.BoxLogClear(box)

    if qemubox.BoxRunCmd(box, 'ex1', ['testsuite example', pexpect.TIMEOUT]) != 0:
        return False

    print box.before
    print box.after

    return True
