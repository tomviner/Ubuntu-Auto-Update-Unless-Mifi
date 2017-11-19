Motivation
----------
Ubuntu has a nice auto-update feature that can run in the background or popup a window when updates are available. I find this annoying because I'm often on the train using my personal wifi connection via my Android phone and this slows down my limited bandwidth and adds to my monthly download quota.

Solution
--------
This script checks the SSID found in `iwconfig` and exits if it matches my mifi SSID. Otherwise it simply calls `os.system` with a series of `apt-get` commands to update, upgrade then clean up your packages. 

Usage
-----
    
update.py takes an optional list of SSIDs to ignore:

    python update.py CappedAndroidMifiSSID StingySteve DodgyDave

I add this script as a sudo cron job with: `sudo crontab -e` then enter

    0 */4 * * * python /path/to/update.py Tom

which will run every 4 hours. Adjust as required.
