import requests

s=requests.session()
data={'email':'997846481@qq.com','passwd':'shadow2000'}
r=s.post('http://www.yesssr.com/auth/login',data=data)
rch=s.post('http://www.yesssr.com/user/checkin')
print(rch.text)
