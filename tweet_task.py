from celery import Celery
import json
import re

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)



@app.task


def read():

	prons = ["han", "hon", "den", "det", "denna", "denne", "hen"]

	with open('tweets/0c7526e6-ce8c-4e59-884c-5a15bbca5eb3') as file:

		tweets = [line.rstrip('\n') for line in file]

		for tweet in tweets[:10]:

			if tweet:

				parsed = json.loads(tweet)

				text = parsed['text']

				r = re.compile('|'.join([r'\b%s\b' % w for w in prons]), flags=re.I)

				print("Tweet: \n" + text + '\n' + 
				"////////////////////////////\n" + 
				"Pronouns: \n" + str(r.findall(text)))
