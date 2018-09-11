import os
import re
import time
from selenium import webdriver


c1 = {
    'name': 'STUDY_INFO',
    'value': '"g586268@163.com|-1|1136111566|1527246786180"',
    'domain': '.icourse163.org',
    'path': '/',
    'httponly': True,
    'secure': False
}
c2 = {
    'name': 'NTES_PASSPORT',
    'value': 'g3TAjYXZbnZUzM2aUQ4ElRTVHdJt.1NteokquAroTryqjKoGNj5ophTDmTbzXv4R6EEooNctaP8V_XgfsoFK1rS1w89aBE.Y1cVAau.Aom.DCkfsc2dwigogTsFzKwiphnE4_E2W1rhab6x9rEvCDq4XXWKr7Rlwk',
    'domain': '.icourse163.org',
    'path': '/',
    'httponly': True,
    'secure': False
}
c3 = {
    'name': 'NTESSTUDYSI',
    'value': '0f2e1e8b2aa344a8a7828bef042689fe',
    'domain': '.icourse163.org',
    'path': '/',
    'httponly': True,
    'secure': False
}
c4 = {
    'name': 'NTES_SESS',
    'value': '8.1GSh1kmb.WTRZkSPnmHbIpxEemtJ2d7te_AHnvblHrE_XDPEyXqNBWi835oe3gZ75BsvxkD9WvnM3cReHW9WaJNwm399WhVFjntDl.MfQfqFZi3ktPMYvex9wdCn0rwkVMoNP2SczDp61BVQd0YZYozB.ZWP7cqsmXoStsUVag6bn2b88sikFum',
    'domain': '.icourse163.org',
    'path': '/',
    'httponly': True,
    'secure': False
}
c5 = {
    'name': 'P_INFO',
    'value': 'g586268@163.com|1527246786|1|imooc|00&99|zhj&1526899889&imooc#zhj&330100#10#0#0|&0|cloudmusic&imooc|g586268@163.com',
    'domain': '.icourse163.org',
    'path': '/',
    'httponly': True,
    'secure': False
}
c6 = {
    'name': 'STUDY_PERSIST',
    'value': '"ev43caKG4G2DJjFGf3tUGQuuTVBNJbARQJqjcsneb2SryOPMnf4Cck+cTjyNV4XlYZDBg+SrsDnBjTayu/4+lkpiy0siJV9JVuCj3OD6L1gNPLeq0EebVsgFtW9Zny8dWa4O/lRUHndSsL6IMEIFVc8MhgBy6n325joucUWNTNHkGpLaMS98V8c2PWuDit1fbBgMKYutm2mclBf+1iCcuqerrzfin1SwA7cBFulC07YtbbMCuQrcAiDbfyn/qhOQ8WQLi3xTJ45sq/acjsEWiA=="',
    'domain': '.icourse163.org',
    'path': '/',
    'httponly': True,
    'secure': False
}
c7 = {
    'name': 'STUDY_SESS',
    'value': '"0HQzjmh0ZCr3FiQbjV0UqqpofI/F2SJ2jrS+EHPWwP10LL+BGGYnikLekJNz1zaHotnUYCTim4oAfWHuINXQ1FzHv0gKJhOns5GJDLbuPCY19N5UlLbZmvM8Y9ubPxt8fa/S0/WSMZC7TKcS1Cioit03PmL2UVwi49J5Xeb6B2CAB324xXcBe7qOJTRrr0/A"',
    'domain': '.icourse163.org',
    'path': '/',
    'httponly': True,
    'secure': False
}
c8 = {
    'name': 'S_INFO',
    'value': '1527246786|0|3&20##|g586268',
    'domain': '.icourse163.org',
    'path': '/',
    'httponly': True,
    'secure': False
}
c9 = {
    'name': 'NETEASE_WDA_UID',
    'value': '1136111566#|#1519893318339',
    'domain': '.icourse163.org',
    'path': '/',
    'httponly': True,
    'secure': False
}
if __name__ == "__main__":
    url = []
    with open('./in_url1.txt', 'r') as f:
        for line in f.readlines():
            curline = line.split('\n')
            url.append(curline[0])
    print(url)
    driver = webdriver.PhantomJS()
    driver.customHeaders = {
        'Host': 'www.icourse163.org',
        'Referer': 'https://www.icourse163.org/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    print('2')
    driver.get('https://www.icourse163.org/home.htm?userId=1136111566#/home/course')
    print('3')
    driver.add_cookie(c1)
    driver.add_cookie(c2)
    driver.add_cookie(c3)
    driver.add_cookie(c4)
    driver.add_cookie(c5)
    driver.add_cookie(c6)
    driver.add_cookie(c7)
    driver.add_cookie(c8)
    driver.add_cookie(c9)
    driver.refresh()
    time.sleep(10)
    driver.implicitly_wait(2)
    content = driver.page_source.encode('utf-8')
    with open('out_test.txt', 'wb') as f:
        f.write(content)
    for i in range(len(url)):
        print('1')
        print(url[i])
        driver.get(url[i])
        time.sleep(20)
        print('4')
        content = driver.page_source.encode('utf-8')
        filename = re.findall('tid=.*#', url[i])[0][:-1]
        with open('./web_ans/' + filename + '.txt', 'wb') as f:
            f.write(content)