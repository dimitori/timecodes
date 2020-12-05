import sys
from datetime import datetime, timedelta
import pickle


start_time = sys.argv[1]  # 19:07:00
comment = sys.argv[2]  # 'some text'

try:
    delta_min = int(sys.argv[3])
except IndexError:
    delta_min = 0
delta_min = timedelta(minutes=delta_min)


start_h, start_m, start_s = [int(time) for time in start_time.split(':')]

now = datetime.now()

if start_h <= now.hour:
    start_datetime = now.replace(hour=start_h, minute=start_m, second=start_s)
else:
    delta = timedelta(days=1)
    start_datetime = now.replace(hour=start_h, minute=start_m, second=start_s) - delta


d = now - start_datetime

st = datetime(1, 1, 1) + d - delta_min

stream_time = f'{st.hour:02}:{st.minute:02}:{st.second:02}'

with open(f'{start_time}.txt', 'a+') as f:
    f.write(f'{stream_time} - {comment}\n')


with open(f'{start_time}.pickle', 'rb') as f:
    try:
        data = pickle.load(f)
    except (FileNotFoundError, EOFError):
        data = []


with open(f'{start_time}.pickle', 'wb') as f:
    data.append(st)
    pickle.dump(data, f)
