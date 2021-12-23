import requests

'''
cookie的操作：cookie是一个key，value形式。

设置cookie：例如操作cookie username：

获取cookie：document.cookie

添加cookie：document.cookie="username=quanquan"

修改cookie：document.cookie="username=quanquanone"

删除cookie：document.cookie="username="

在ajax请求的时候想携带cookie，只要是同源策略，只要在发送请求前设置cookie就ok

ajax请求携带cookie问题：

1.ajax会自动带上同源的cookie(只要在document.cookie里设置就好)，不会带上不同源的cookie
2.可以通过前端设置withCredentials为true， 后端设置Header的方式让ajax自动带上不同源的cookie，但是这个属性对同源请求没有任何影响。会被自动忽略。
'''

'''
document.cookie=('y')+('u')+('a')+('n')+('r')+('e')+('n')+('x')+('u')+('e')+('_')+('c')+('o')+('o')+('k')+('i')+('e')+('=')+('1')+('6')+('4')+('0')+('1')+('4')+('9')+('3')+('8')+('4')+('|')+('H')+('T')+('i')+('O')+('y')+('p')+('M')+('h')+('K')+('6')+('B')+('h')+('n')+('d')+('t')+('V')+('l')+('b')+('u')+('7')+('k')+('g')+('I')+('9')+('u')+('a')+('a')+('s')+('p')+('n')+('7')+('M')+('v')+('f')+('W')+('O')+('J')+('2')+';path=/';location.href=location.pathname+location.search
'''
cookies = {
    'sessionid': 'm20pyzr9csoa3wsreknw1bcntsvsmpmn',
}

response = requests.get('http://match.yuanrenxue.com/match/13', cookies=cookies, verify=False)
tmp = response.text.split("('")
text = ''
for t in tmp:
    if "')" in t:
        text += t.split("')")[0]

cookies['yuanrenxue_cookie'] = text.split('yuanrenxue_cookie=')[1]

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'yuanrenxue.project',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://match.yuanrenxue.com/match/13',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}



r = 0
for page in range(1,6):
    params = (
        ('page', page),
    )

    response = requests.get('http://match.yuanrenxue.com/api/match/13',headers=headers, params=params, cookies=cookies, verify=False)
    print(response.text)
    for i in response.json()['data']:
        r += i['value']
print(r)


