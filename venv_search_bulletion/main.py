from bs4 import BeautifulSoup
from os import mkdir,path,system
from re import sub
import configparser
import requests 

def chooser(words,section):
    list_of_yes=[]
    for i in words:
        if section.getboolean(i):
            list_of_yes.append(i)
    return list_of_yes
    
config = configparser.ConfigParser()
config.sections()
config.read('config.ini',encoding='utf-8')

url=config['address']['url']
output_dir=config['address']['output_dir']
options=config['options']
keyword=options['關鍵字']
year_range=options['年分']
items_per_page=options.getint('每頁項數')
opt=chooser(['招標','決標','公開閱覽及公開徵求','政府採購預告'],options)

def checkAndMkdir(d_path):
    if not path.exists(d_path):
        mkdir(d_path)
    return d_path

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]" # ‘/ \ : * ? " < > |‘
    new_title = sub(rstr, "_", title) # 替換為底線
    return new_title

def param_data(keyword,year_range,opt,page,items_per_page=10):
    tu_par = (('timeRangeTemp',f'{year_range}/1/1-{year_range}/12/31'),
    ('querySentence',keyword),
    ('sym','on'),
    ('sortCol','TENDER_NOTICE_DATE'),
    ('itemPerPage',items_per_page),
    ('tmpQuerySentence',''),
    ('root','tps'),
    ('timeRange',f'{year_range}/1/1-{year_range}/12/31'),
    ('tenderStatusType',opt),
    ('d-7095067-p',page)
    )
    return tu_par
    
def head_of_file(filename='head_of_html.html'):
    f=open(filename,'r',encoding='utf-8')
    hof=f.read()
    f.close
    return hof
    
def print_start(keyword,year_range,opts):
    print(f'搜尋"{keyword}"')
    if opts=='':opts='招標'
    print(f'{year_range}年度{opts}公告')
    print('-'*40)

if __name__ =='__main__':
    now_page=1
    opt_str='、'.join(opt)
    endOfResult=False
    file_path=checkAndMkdir(output_dir)+\
    f'搜尋{validateTitle(keyword)}_{year_range}年{opt_str}列表.html'    
    f=open(file_path,'a',encoding='utf-8')
    f.write(head_of_file())
    req_session=requests.Session()
    print_start(keyword,year_range,opt_str)
    while not endOfResult:
        resp = req_session.get(
        url,
        params=param_data(keyword,year_range,opt,now_page,items_per_page)
        )
        
        soup = BeautifulSoup(resp.text, 'lxml')
        search_result=soup.find(id="searchResult").select_one('tbody')
#        print(resp.status_code)
              
        if search_result.find('tr',{'class':'empty'})!= None:
            print('搜尋完畢')
            if now_page==1:print('查無資料')
            break
        f.write(search_result.prettify())
        print(f'每頁最多{items_per_page}筆，此為第{now_page}頁')

        now_page+=1
        
    f.write('</table>')
    f.close()
    system("pause")