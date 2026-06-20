from datetime import datetime, timedelta

today = datetime.now()

five_days_ago = today - timedelta(days=5)
print("Five days ago:", five_days_ago.date())

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())

without_microseconds = today.replace(microsecond=0)
print("Without microseconds:", without_microseconds)

date1 = datetime(2026, 6, 20, 12, 0, 0)
date2 = datetime(2026, 6, 21, 14, 30, 0)

difference = date2 - date1
print("Difference in seconds:", difference.total_seconds())