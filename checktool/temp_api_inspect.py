import urllib.request
import json

url = 'https://script.google.com/macros/s/AKfycbwQqf2AlZ5m9epZL7n8j6VQxZIqryTOt9eMK29xO5Qp4SnNOB7tSYzE4x0B6FKFc4b-/exec'
with urllib.request.urlopen(url) as r:
    data = json.loads(r.read().decode('utf-8'))

print('type', type(data).__name__, 'len', len(data) if hasattr(data, '__len__') else 'n/a')
print('sample0', data[0])
print('sample1', data[1])
print('sample2', data[2])

fields = ['date', 'Date', 'DATE', 'day', 'Day', 'DAY']
dates = [next((item.get(f) for f in fields if item.get(f) is not None), None) for item in data]
print('unique dates', sorted(set(dates))[:20])
print('days starting 2026-05', [d for d in dates if d and d.startswith('2026-05')][:20])
print('today candidates')
from datetime import datetime, timezone
now = datetime.now()
print(now.strftime('%Y-%m-%d'))
print(now.strftime('%Y/%m/%d'))
print(now.strftime('%d-%m-%Y'))
print(now.strftime('%d/%m/%Y'))
print(now.strftime('%Y%m%d'))
