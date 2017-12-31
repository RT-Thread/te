# TestCase on Host for RT-Thread

"""
testcase example
"""

import qemubox

def run(box):
    qemubox.BoxRunCmd(box, 'ps', ['tidle'])
    # qemubox.BoxDelay(box, 1)
    print box.before
    print box.after

    return True
