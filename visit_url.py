from urllib import request,parse

#------------------------------------------------------
filename='words.txt'
private_token='ee4b51101b4137ca'
public_token='cafdbf9f'
add_url='https://twitch.center/customapi/addquote'
#------------------------------------------------------

try:
    f=open(filename,'r',encoding="UTF-8")    
except FileNotFoundError:
    print('file doesn\'t exist or wrong file name')
else:
    for line_data in f:        
        data = {}
        data['token'] = private_token
        # data['data'] = 'good morning \nmother fucker'
        data['data'] = line_data.strip()
        print(data['data'])
        url_values = parse.urlencode(data)

        request.urlopen(f'{add_url}?{url_values}')
