#!/usr/bin/env python3

import sys
import settings
import subprocess as sp
import library as lb


def invalid_time():
	print("\n\tERROR: Invalid Time\n")
	exit(1)


def parse_time(time):
	if ':' in time:
		hour, minute = time.split(':')

		if not hour.isnumeric():
			invalid_time()
		hour = int(hour)

		if minute.endswith('PM'):
			hour += 12
			minute = minute.rstrip('PM')
		elif minute.endswith('AM'):
			minute = minute.rstrip('AM')
		else:
			invalid_time()

		if not minute.isnumeric():
			invalid_time()
		minute = int(minute)

		if not (0 < hour <= 12 or 0 <= minute < 60):
			invalid_time()
	else:
		if not time.isnumeric():
			invalid_time()
		hour, minute = time_after_delta(int(time))

	return hour, minute


def unique(hour, minute):
	for alarm in lb.get_alarms():
		if (hour, minute) == alarm[:-1]:
			return False
	return True


if len(sys.argv) != 2:
	invalid_time()

hour, minute = parse_time(sys.argv[1])
if not unique(hour, minute):
	print("\n\tERROR: Alarm Already Set for This Time\n")
	exit(2)


if (hour, minute) == lb.min_alarm((hour, minute), lb.get_next_alarm()):
	lb.write_next_alarm(hour, minute)

with open(settings.crontab_file, 'a') as outfile:
	outfile.write(lb.crontab_line(hour, minute))

with open(settings.alarms_file, 'a') as outfile:
	outfile.write(lb.alarms_line(hour, minute))

sp.run(f"crontab {settings.crontab_file}".split(' '))
