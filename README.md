# Timecodes

Small script for register time codes while streaming.

## Usage

```bash
python tc.py 2020-12-05T19:12:44 'some comment' 3 
```
where
19:12:44 - start time of stream.
'some comment' - comment for this time code.
3 - time shift. If set this, time will be computed with - 3 minutes.

See the Example

## Examples

Input (in terminal):
```bash
python tc.py 2020-12-05T19:12:44 'some comment'
```

Output (in 2020-12-05T19:12:44.txt):
```
00:01:12 - some comment
```

Example above illustrates situation, when stream was started at 19:12:44 and command was executed at 19:13:56. So it's been 1 minute 12 seconds since the stream started. 

If there was last parameter, e.g. 1, then in *.txt would be time = 00:00:12


Also we have output in 2020-12-05T19:12:44.tuple.
there will be python list of datetimes and comments:
```python
List[Tuple[datetime, str]]
```
It needs for case, when we need change something in string formatting or set some time shift or whatever.

