import requests
import hmac
import hashlib
import time
import datetime
import base64

def msg(t, id, data):
	t=str(t)
	r=t+id
	for v in data.values():
		r += v
	return r

key = "593fe6ed77014f9507761028801aa376f141916bd26b1b3f0271b5ec3135b989"

ts = time.time()

#st = datetime.datetime.fromtimestamp(1395682554).strftime('%Y-%m-%d %H:%M:%S')
#print st

s = {'id': '23'}
msg = msg(int(ts), '1', s)

cash = hmac.new(key, msg=msg, digestmod=hashlib.sha256).hexdigest()

headers = {'API_ID': 1, 'API_TIME': int(ts), 'API_HASH': cash}

r = requests.post('http://ne-govori-mne.net', data=s, headers=headers)

#print r.headers, "\n"
for v in r.headers.values():
    print v

print r.text,"\n"
