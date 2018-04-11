#coding=utf8
from bs4 import BeautifulSoup
import requests

email='1018667195@qq.com'
password='shadow2000'
url='www.yesssr.com'
checkin_url= url+'/user'

head={'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip,deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Host':'www.yesssr.com',
'Referer':'http://www.yesssr.com/auth/login',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'
}

login_data={'email':'email',
	    'passwd':'password'}

s=requests.session()
r=s.post('http://www.yesssr.com/auth/login',data=login_data,headers=head)
print(r.text)
print(r)
rch=s.post('http://www.yesssr.com/user/checkin')
print(rch)
if rch.status_code==200:
  print('checkin successfully')
