import requests

cookies = {
    'Hm_lvt_c99546cf032aaa5a679230de9a95c7db': '1625558342',
    'Hm_lpvt_c99546cf032aaa5a679230de9a95c7db': '1625558439',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://match.yuanrenxue.com/match/1',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('m', 'f6a94d6c39ba5e6cd3adeba59b4beb73\u4E281625658454'),
)

'''
var _0x2268f9 = Date['\x70\x61\x72\x73\x65'](new Date()) + (16798545 + -72936737 + 156138192), _0x57feae = oo0O0(_0x2268f9['\x74\x6f\x53\x74\x72' + '\x69\x6e\x67']()) + window['\x66'];
v_0x2268f9 = str(int(time*1000)+ (16798545 + -72936737 + 156138192))
'''

response = requests.get('http://match.yuanrenxue.com/api/match/1', headers=headers, params=params, cookies=cookies, verify=False)
print(response.text)
'''
window.url = '/api/match/12';
    request = function(){
        //    点击换页后的操作，先得到翻到了几页
        if (window.page){}else {window.page=1}
        var list = {
            "page": window.page,
            "m": btoa('yuanrenxue' + window.page)
        };
        $.ajax({
            url: window.url,
            dataType: "json",
            async: false,
            data: list,
            type: "GET",
            beforeSend: function(request) {
            },
            success: function(data) {

                data = data.data;
                let html = '';
                $.each(data, function(index, val) {
                    html += '<td>'+ val.value + '</td>'
                });
                $('.number').text('').append(html);
            },
            complete: function() {
            },
            error: function() {
                alert('因未知原因，数据拉取失败。可能是触发了风控系统');
                alert('生而为虫，我很抱歉');
                $('.page-message').eq(0).addClass('active');
                $('.page-message').removeClass('active');
            }
        });
    };
    request()
'''