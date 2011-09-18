import os
import sys
import subprocess

"""
Update packages unless tethered via bandwidth capped personal mobile hotspot
"""
BAD_SSIDS = ('Tom',)

def do(cmd, debug=False):
    if debug:
        print
        print cmd
    status_code = os.system(cmd)
    assert status_code==0, 'Status code: %s' % status_code

def on_mifi(bad_ssids=BAD_SSIDS):
    conn_data = subprocess.Popen('iwconfig', stdout=subprocess.PIPE).communicate()[0]
    return any(('ESSID:"%s"' % ssid) in conn_data for ssid in bad_ssids)

def upgrade_packages(debug=False):
    cmds= """
        apt-get update
        apt-get upgrade
        apt-get autoremove
        apt-get autoclean
        """.strip().splitlines()

    for cmd in cmds:
        do(cmd + ' -y', debug=True)

def main():
    if on_mifi():
        print >>sys.stderr, "On personal mobile hotspot so don't update"
        sys.exit()
    upgrade_packages(debug=True)

if __name__ == '__main__':
    main()
