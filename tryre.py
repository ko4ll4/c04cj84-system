import time
import os
import urllib.request


req = urllib.request.Request(
    'https://stats.popcat.click/pop?pop_count=799&captcha_token=goodmorningMF')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
headers = {'User-Agent': user_agent}
print('start')
urllib.request.urlopen(req, headers)
time.sleep(30)


os.system("pause")
