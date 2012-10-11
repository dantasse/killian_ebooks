#!/usr/bin/env python

# Scrapes twitter (hopefully) for all of killian's tweets

import twitter

api = twitter.Api(cache=None)
# gotta try 10 times because you get <200 tweets each time, I dunno why this is
for i in range(10):
  statuses = api.GetUserTimeline('KillianCzuba', count=200, page=i)
  for status in statuses:
    # strip out people's names so they don't get surprisingly tweeted at
    text = status.text.encode('utf8')
    text = text.replace('@','')
    print text

