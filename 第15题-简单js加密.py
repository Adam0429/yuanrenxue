import requests
import execjs
import pywasm
import datetime
import random

runtime = pywasm.load('/Users/wangfeihong/Downloads/main.wasm')

t1 = round(datetime.datetime.now().timestamp())/2
t2 = round(datetime.datetime.now().timestamp())/2 - int(random.random()*50+1)
t1 = int(t1)
t2 = int(t2)
m = str(runtime.exec('encode', [t1,t2])) + '|' + str(t1) + '|' + str(t2)

print(m)

"""
       window.url = '/api/match/15';
        fetch('/static/match/match15/main.wasm').then(response =>
            response.arrayBuffer()
        ).then(bytes => WebAssembly.instantiate(bytes)).then(results => {
            instance = results.instance;
            window.q = instance.exports.encode;
            window.m = function (){
                t1 = Date.parse(new Date())/1000/2;
                t2 = Date.parse(new Date())/1000/2 - Math.floor(Math.random() * (50) + 1);
                return window.q(t1, t2).toString() + '|' + t1 + '|' + t2;
            }
            window.finish = true;
        }).catch(console.error);
"""




headers = {
    'authority': 'match.yuanrenxue.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'yuanrenxue.project',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://match.yuanrenxue.com/match/15',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1640075857; qpfccr=true; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1640075874; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1640076299; tk=-6299560775612618509; sessionid=6gyxplyr65qflo1sjcp1kefoggtmfucr; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1640081843'
}

result = 0
for page in range(1,6):
    params = (
        ('m', m),
        ('page', str(page)),
    )
    # 17741311|820040921|820040882
    # 17741161|820040958.5|820040916.5

    response = requests.get(f'https://match.yuanrenxue.com/api/match/15', headers=headers,params=params)
    print(response.text)
    for i in response.json()['data']:
        result += i['value']

print(result)