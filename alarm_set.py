#!/usr/bin/env python3

import sys
import settings
import subprocess as sp
import library as lb


def invalid_time():
	print("\n\tERROR: Invalid Time\n")
	exit(1)


def parse_time(time):
	if not time.isnumeric():
		if ':' not in time:
			time = f"{time[:-2]}:00{time[-2:]}"

		hour, minute = time.split(':')
		if not hour.isnumeric():
			invalid_time()
		hour = int(hour) % 12

		if minute.upper().endswith('PM'):
			hour += 12
		elif not minute.upper().endswith('AM'):
			invalid_time()
		minute = minute[:2]

		if not minute.isnumeric():
			invalid_time()
		minute = int(minute)

		if not (0 < hour <= 12 or 0 <= minute < 60):
			invalid_time()
	else:
		hour, minute = lb.time_after_delta(int(time))

	return hour, minute


def unique(hour, minute):
	for alarm in lb.get_alarms():
		if (hour, minute) == alarm[:-1]:
			return False
	return True


if len(sys.argv) < 2:
	invalid_time()

hour, minute = parse_time(sys.argv[1])
message = ' '.join(sys.argv[2:])

if not unique(hour, minute):
	print("\n\tERROR: Alarm Already Set for This Time\n")
	exit(2)

new_alarm = (hour, minute, message)
next_alarm = lb.get_next_alarm()
if not next_alarm or new_alarm == lb.min_alarm(new_alarm, next_alarm):
	lb.write_next_alarm(new_alarm)

with open(settings.crontab_file, 'a') as outfile:
	outfile.write(lb.crontab_line(hour, minute))

with open(settings.alarms_file, 'a') as outfile:
	outfile.write(lb.alarms_line(hour, minute, message))

sp.run(f"crontab {settings.crontab_file}".split(' '))
