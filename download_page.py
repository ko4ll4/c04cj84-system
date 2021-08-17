import urllib.request
import time

now_time=time.localtime(time.time())
save_time=time.strftime('%Y%m%d%H%M%S',now_time)
print(save_time)

# --------------------------------------------------------------------------
url='https://twitch.center/customapi/quote/list?token=cafdbf9f&no_id=1'
filename=f'list{save_time}.txt'
# --------------------------------------------------------------------------

with urllib.request.urlopen(url) as f:
    list_text = f.read().decode('utf-8')


with open(filename,'w',encoding='UTF-8') as file:
    file.write(list_text)