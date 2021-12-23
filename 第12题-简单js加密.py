import requests
import base64

def str_to_base64(string):
    bytes_url = string.encode("utf-8")
    str_url = base64.b64encode(bytes_url)  # 被编码的参数必须是二进制数据
    return str_url

cookies = {
    'sessionid': 'u45ypd8xs0moqs4yjxj7vnf74mkfuah5',
    'vaptchaNetway': '1',
    'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f': '1625038003,1625053508',
    'Hm_lvt_c99546cf032aaa5a679230de9a95c7db': '1625024980,1625025118,1625038049,1625053929',
    'm': 'e460beb3e9387dc2d2762449653ce4f1|1625053929000',
    'vaptchaNetwayTime': '1625053945934',
    'tk': '9029674401987588603',
    'qpfccr': 'true',
    'no-alert3': 'true',
    'Hm_lvt_9bcbda9cbf86757998a2339a0437208e': '1625024702,1625054009',
    'Hm_lpvt_9bcbda9cbf86757998a2339a0437208e': '1625054009',
    'Hm_lpvt_c99546cf032aaa5a679230de9a95c7db': '1625054016',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'yuanrenxue.project',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://match.yuanrenxue.com/match/12',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

params = (
    ('page', '2'),
    ('m', 'eXVhbnJlbnh1ZTI='),
)

r = 0
for page in range(1,6):
    params = (
        ('page', str(page)),
        ('m', str_to_base64('yuanrenxue'+str(page))),
    )

    response = requests.get('http://match.yuanrenxue.com/api/match/12',cookies=cookies,headers=headers, params=params)
    print(response.text)
    for i in response.json()['data']:
        r += i['value']
print(r)

