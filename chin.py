import requests

s=requests.session()
data={'email':'1018667195@qq.com','passwd':'shadow2000'}
r=s.post('http://www.yesssr.com/auth/login',data=data)
rch=s.post('http://www.yesssr.com/user/checkin')
print(rch.text)
