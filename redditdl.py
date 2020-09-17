#!/usr/bin/env python3
# a tool to scrape image datasets from reddit using pushshift.io
# gives a file with a list of links to image files downloadable using aria2c or wget or curl
# args: redditdl.py subreddit_name output_file
# requires requests

import requests
import re
import sys
import json
import time

_image_re = re.compile(r'^https:\/\/preview.redd.it\/([a-zA-Z0-9]+\.[a-zA-Z0-9]+)')
def url_before(before):
    return 'https://api.pushshift.io/reddit/submission/search/?subreddit={}&is_video=false&is_self=false&sort_type=created_utc&sort=desc&before={}'.format(sys.argv[1], before)

def loop_results(start):
    ts = int(start)
    results = []
    while True:
        url = url_before(ts)
        results = requests.get(url).json()['data']
        if not results:
            break
        ts = results[-1]['created_utc']
        yield from results
        time.sleep(2)

def loop_images(start):
    for result in loop_results(start):
        try:
            if not result['url'].startswith('https://www.reddit.com/gallery'):
                yield result['url']
                continue
            for item in result['media_metadata'].values():
                f = _image_re.match(item['s']['u']).group(1)
                yield 'https://i.redd.it/' + f
        except Exception as e:
            print(e)

with open(sys.argv[2], 'a') as f:
    for img in loop_images(time.time()):
        print(img)
        f.write('{}\n'.format(img))
        f.flush()
