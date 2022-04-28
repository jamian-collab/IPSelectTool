from urllib.request import urlopen, Request
import json

def getAddress(host):
    myHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }

    myUrl = 'https://opendata.baidu.com/api.php?query=%s&resource_id=6006'%host

    req = Request(url=myUrl, headers=myHeaders)
    res = urlopen(req).read().decode('gbk')

    address = json.loads(res)['data'][0]['location']
    return address

