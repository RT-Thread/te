"""
testcase_filesystem: mkdir
"""

import qemubox

def run(box):
    ret = qemubox.BoxRunCmd(box, 'ls /test', ['Directory /test:', 'No such directory'])
    if ret == 0:
        qemubox.BoxRunCmd(box, 'rm /test')

    qemubox.BoxRunCmd(box, 'mkdir /test')
    ret = qemubox.BoxRunCmd(box, 'ls /test', ['Directory /test:', 'No such directory'])
    print box.before
    print box.after

    if ret != 0:
        print '[TC] failed'
        return False

    return True
