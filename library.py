from datetime import datetime, timedelta
import settings


def to_datetime(hour, minute):
	return datetime.strptime(f"{hour}, {minute}", "%H, %M")


def time_after_delta(minutes):
	time = datetime.now() + timedelta(minutes=minutes)
	return time.hour, time.minute


def time_remaining(time):
	hour, minute = time
	dt = to_datetime(hour, minute)
	now = to_datetime(*datetime.now().strftime("%H, %M").split(', '))

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
			hour, minute = map(eval, line.strip().split(','))
			alarms.append((hour, minute))
	return alarms


def get_next_alarm():
	with open(settings.next_alarm_file) as infile:
		next_alarm = infile.read()
		if not next_alarm:
			return
		return tuple(map(eval, next_alarm.split(',')))


def write_next_alarm(data):
	with open(settings.next_alarm_file, 'w') as outfile:
		if data:
			hour, minute = data
			outfile.write(f"{hour},{minute}")


def min_alarm(*alarms):
	if alarms:
		return min(alarms, key=time_remaining)
	return None


def alarms_line(hour, minute):
	return f"{hour},{minute}\n"


def crontab_line(hour, minute):
	return f"{minute} {hour} * * * {settings.alarm_unset_script}\n"


def write_reminder():
	time = datetime.now().strftime("%I,%M,%p").split(',')
	time = f"{int(time[0])}:{time[1]} {time[2]}"

	message = '"' * 3
	message += f"\n\tAlarm Finished!\n\n\tIts {time}!!!\n\n"
	message += '"' * 3

	with open(settings.alarm_reminder_file, 'w') as outfile:
		outfile.write(message)

