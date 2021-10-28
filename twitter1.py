'''
This program retrieves the timeline for a particular Twitter user
and returns it to us in JSON format in a string.
We simply print the first 250 characters of the string:
'''

import urllib.request, urllib.parse, urllib.error
import twurl
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# this is to circumvent the https cirtificates instead of the http 

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print(data[:250])
    headers = dict(connection.getheaders())
    # print headers
    print('Remaining', headers['x-rate-limit-remaining'])

'''
One header in particular, x-rate-limit-remaining, informs us how many more requests
we can make before we will be shut off for a short time period.
You can see that our remaining retrievals drop by one each time we make a request to the API.
'''
