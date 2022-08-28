import requests
from user_agent import generate_user_agent
import random
req = requests.Sessien()
proxy = open('proxy.txt', 'r').read().splitlines()
proxylist = []
for prox in proxy:
	proxylist.append(prox)
RandomProxy = str(random.choice(proxylist))
ReProx = {
	'http': 'http://{}'.format(RandomProxy),
	'https': 'https://{}'.format(RandomProxy)
} 
req.proxies = ReProx
url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
h = {
	"Accept": "*/*",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate, br",
	"X-CSRFToken": "EtjnnSUrAmHfWDuqBmqIGNkvZWo3BrZh",
	"X-Instagram-AJAX": "416cd3bed162",
	"X-IG-App-ID": "936619743392459",
	"X-ASBD-ID": "198387",
	"X-IG-WWW-Claim": "0",
	"Content-Type": "application/x-www-form-urlencoded",
	"X-Requested-With": "XMLHttpRequest",
	"Content-Length": "365",
	"Origin": "https://www.instagram.com",
	"Connection": "keep-alive",
	"Referer": "https://www.instagram.com/accounts/emailsignup/",
	"Cookie": "csrftoken=EtjnnSUrAmHfWDuqBmqIGNkvZWo3BrZh; mid=YueWuwAEAAG9I-1QsB-ckQ23i7nC; ig_did=81D0FCDD-E1B9-45B6-A8AF-B21B6CF70C48; ig_nrcb=1",
	"Sec-Fetch-Dest": "empty",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Site": "same-origin",
	"TE": "trailers"
}
user = input("enter user")
name = input("enter name")
mail = input("enter email")
password = input("enter password")
d = {
	"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:1613414957:{password}",
	"email": mail,
	"username": user,
	"first_name": name,
	"client_id": "YueWuwAEAAG9I-1QsB-ckQ23i7nC",
	"seamless_login_enabled": "1",
	"opt_into_one_tap": "false"
}
req_sign = requests.post(url, headers=h, data=d)
if 'userId' in req_sign.text:
	co = req_sign.cookies
	coo = co.get_dict()
	csrf = coo['csrftoken']
	cookie = f"csrftoken={coo['csrftoken']};mid={coo['mid']}];ig_did={coo['ig_did']};ig_nrcb={coo['ig_nrcb']};"
else:
	print("false information")
he = {
	"Accept": "*/*",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate, br",
	"X-CSRFToken": "EtjnnSUrAmHfWDuqBmqIGNkvZWo3BrZh",
	"X-Instagram-AJAX": "416cd3bed162",
	"X-IG-App-ID": "936619743392459",
	"X-ASBD-ID": "198387",
	"X-IG-WWW-Claim": "0",
	"Content-Type": "application/x-www-form-urlencoded",
	"X-Requested-With": "XMLHttpRequest",
	"Content-Length": "23",
	"Origin": "https://www.instagram.com",
	"Connection": "keep-alive",
	"Referer": "https://www.instagram.com/accounts/emailsignup/",
	"Cookie": cookie,
	"Sec-Fetch-Dest": "empty",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Site": "same-origin",
	"TE": "trailers",
	"User-Agent": generate_user_agent(),
	"X-ASBD-ID": "198387",
	"X-CSRFToken": csrf,
	"X-IG-App-ID": "936619743392459",
	"X-IG-WWW-Claim": "0",
	"X-Instagram-AJAX": "416cd3bed162",
	"X-Requested-With": "XMLHttpRequest",
}

da = {
	"day": "4",
	"month": "7",
	"year": "2004"
}
url2 = "www.instagram.com/web/consent/check_age_eligibility/"
req_age = requests.post(url2, headers=he, data=da)
cookk = {
	"csrftoken": "EtjnnSUrAmHfWDuqBmqIGNkvZWo3BrZh",
	"ig_did": "81D0FCDD-E1B9-45B6-A8AF-B21B6CF70C48",
	"ig_nrcb": "1",
	"mid": "YueWuwAEAAG9I-1QsB-ckQ23i7nC",
	"rur": '\"ODN\\05455217676343\\0541693132077:01f78d5e517224540cef44a38b79772d7f0fa26018232521dc3f6d5a811e9989997fdc4f\"'
}
url3 = "https://i.instagram.com/api/v1/accounts/send_verify_email/"
dat ={
	"device_id": "YueWuwAEAAG9I-1QsB-ckQ23i7nC",
	"email": "9dcd1a2b54@boxomail.live"
}
req_send = requests.post(url3, headers=he, data=dat)
code = input("enter code")
url4 = "https://i.instagram.com/api/v1/accounts/check_confirmation_code/"
data = {
	"code": code,
	"device_id": "YueWuwAEAAG9I-1QsB-ckQ23i7nC",
	"email": mail
}
req_code = requests.post(url4, headers=he, data=data)

