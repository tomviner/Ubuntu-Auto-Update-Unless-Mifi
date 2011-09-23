"""
Update packages unless tethered via bandwidth capped personal mobile hotspot
"""

import os
import sys
import subprocess


IWCONFIG_PATH = '/sbin/iwconfig'


def do(cmd, debug=False):
    if debug:
        print
        print cmd
    status_code = os.system(cmd)
    assert status_code==0, 'Status code: %s' % status_code

def on_mifi(bad_ssids=()):
    try:
        p = subprocess.Popen(IWCONFIG_PATH, stdout=subprocess.PIPE)
    except OSError, e:
        print "Problem calling iwconfig at %s: %r" % (IWCONFIG_PATH, e)
        return False
    comms = p.communicate()
    conn_data = comms[0]
    return any(('ESSID:"%s"' % ssid) in conn_data for ssid in bad_ssids)

def upgrade_packages(debug=False):
    cmds= """
        apt-get update -y
        apt-get upgrade -y
        apt-get autoremove -y
        apt-get autoclean -y
    """.strip().splitlines()

    for cmd in cmds:
        do(cmd, debug=True)

def main():
    bad_ssids = ()
    if sys.argv[1:]:
        bad_ssids = sys.argv[1:]
    if on_mifi(bad_ssids):
        print "On personal mobile hotspot so don't update"
        sys.exit()
    upgrade_packages(debug=True)

if __name__ == '__main__':
    main()
