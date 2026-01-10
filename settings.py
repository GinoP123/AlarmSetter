import os, shutil

next_alarm_file = f"{os.environ['HOME']}/Scripts/AlarmSetter/text_files/next_alarm.txt"
alarms_file = f"{os.environ['HOME']}/Scripts/AlarmSetter/text_files/alarms.csv"
alarm_reminder_file = f"{os.environ['HOME']}/Scripts/AlarmSetter/text_files/alarm_reminder.py"

alarm_unset_script = f"{os.environ['HOME']}/Scripts/AlarmSetter/main.sh unset"

open_file_script = shutil.which("subl")
open_file_script = "/usr/local/bin/sublime" if not (open_file_script and os.path.exists(open_file_script)) else open_file_script
open_file_script = shutil.which("vim") if not os.path.exists(open_file_script) else open_file_script

crontab_file = f"{os.environ['HOME']}/Scripts/miscellaneous/text_files/crontab.txt"
crontab_file = f"{os.environ['HOME']}/crontab.txt" if not os.path.exists(crontab_file) else crontab_file
