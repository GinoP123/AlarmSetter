#!/usr/bin/env python3

import subprocess as sp
import library as lb
import settings


def remove_line(file, line):
	with open(file) as infile:
		lines = infile.readlines()

	lines.remove(line)
	with open(file, 'w') as outfile:
		for line in lines:
			outfile.write(line)


next_alarm = lb.get_next_alarm()
if next_alarm is None:
	print("\n\tERROR: no alarms to unset\n")
	exit(1)

remove_line(settings.crontab_file, lb.crontab_line(*next_alarm[:-1]))
remove_line(settings.alarms_file, lb.alarms_line(*next_alarm))
lb.write_reminder(next_alarm[-1])

min_alarm = lb.min_alarm(*lb.get_alarms())
lb.write_next_alarm(min_alarm)

sp.run(f"crontab {settings.crontab_file}".split(' '))
sp.run("say Ring Ring, Ring Ring, Alarm Finished".split())
sp.run(f"{settings.open_file_script} {settings.alarm_reminder_file}".split())

