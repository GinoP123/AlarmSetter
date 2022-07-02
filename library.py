from datetime import datetime, timedelta
import settings


def to_datetime(hour, minute):
	return datetime.strptime(f"{h}, {m}", "%H, %M")


def time_after_delta(minutes):
	time = datetime.now() + timedelta(minutes=minutes)
	return time.hour, time.minute


def time_remaining(hour, minute):
	dt = to_datetime(hour, minute)
	now = to_datetime(*datetime.now().strftime("%M, %H").split(', '))

	day = timedelta(days=1)
	diff = dt - now

	if diff.days < 0:
		diff += day
	assert diff.days >= 0

	return diff.seconds // 3600, (diff.seconds // 60) % 60


def get_alarms():
	alarms = []
	with open(settings.alarms_file) as infile:
		for line in infile:
			hour, minute, index = map(eval, line.strip().split(','))
			alarms.append((hour, minute, index))
	return alarms


def get_next_alarm():
	with open(settings.next_alarm_file) as infile:
		next_alarm = infile.read()
		if not next_alarm:
			return
		return map(eval, next_alarm.split(','))


def write_next_alarm(*data):
	with open(settings.next_alarm_file, 'w') as outfile:
		if data:
			outfile.write(','.join(data))


def min_alarm(*alarms):
	return min(alarms, key=time_remaining)


def alarms_line(hour, minute):
	return f"{hour},{minute}\n"


def crontab_line(hour, minute):
	return f"{minute} {hour} * * * {settings.alarm_unset_script}\n"


