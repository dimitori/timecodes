import sys
from datetime import datetime, timedelta
import pickle
import os.path

start_time = sys.argv[1]  # 2020-12-05T19:07:00
comment = sys.argv[2]  # 'some text'

try:
    delta_min = int(sys.argv[3])
except IndexError:
    delta_min = 0
delta_min = timedelta(minutes=delta_min)


start_datetime = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")

now = datetime.now()
delta = now - start_datetime

stream_time = datetime(1, 1, 1) + delta - delta_min

timecode = f'{stream_time.hour:02}:{stream_time.minute:02}:{stream_time.second:02}'

with open(f'{start_time}.txt', 'a+') as f:
    f.write(f'{timecode} - {comment}\n')

# Pickle here
if os.path.exists(f'{start_time}.pickle'):
    with open(f'{start_time}.pickle', 'rb+') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = []
else:
    data = []


with open(f'{start_time}.pickle', 'wb') as f:
    data.append((stream_time, comment))
    pickle.dump(data, f)
