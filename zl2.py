import pandas as pd
import re
import requests
import time

url_first = 'https://movie.douban.com/subject/26363254/comments?start=0'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
cookies = {'cookie': 'bid=ysQdcEsF1yM; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1503971414%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D3%26rsv_bp%3D1%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E8%25B1%2586%25E7%2593%25A3%25E7%2594%25B5%25E5%25BD%25B1%26oq%3Dpython%252520pandas%252520%2525E5%2525AE%252589%2525E8%2525A3%252585%26rsv_pq%3Df7b36b3400003c24%26rsv_t%3D25c2xT4EdDqVS9weTnkCgC3HLv%252BmytVfoPHdEDPm2UKO5OjJdOjs7qYHT24%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D19%26rsv_sug1%3D11%26rsv_sug7%3D100%26rsv_sug2%3D0%26prefixsug%3Ddouban%26rsp%3D1%26inputT%3D2678%26rsv_sug4%3D2678%22%5D; ll="118172"; __yadk_uid=FP13J4SISa4a4ANtqHVIx6wVxBsTLyBJ; ps=y; ue="571228207@qq.com"; dbcl2="165347070:/zPLopgetfs"; ck=sxTb; _vwo_uuid_v2=04A0A36A6C9825E1C3C5CDE14FFF579D|2981eb7e2a1e37e53ee72404ee77e82e; _pk_id.100001.4cf6=873426b7bae683c0.1503971414.1.1503971689.1503971414.; _pk_ses.100001.4cf6=*; __utma=30149280.1247043664.1503971415.1503971415.1503971415.1; __utmb=30149280.0.10.1503971415; __utmc=30149280; __utmz=30149280.1503971415.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3%E7%94%B5%E5%BD%B1; __utma=223695111.1315973190.1503971415.1503971415.1503971415.1; __utmb=223695111.0.10.1503971415; __utmc=223695111; __utmz=223695111.1503971415.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3%E7%94%B5%E5%BD%B1; push_noty_num=0; push_doumail_num=0'}
html = requests.get(url_first, headers=headers, cookies=cookies)

#下一页
reg = re.compile(r'<a href="(.*?)&amp;.*?class="next">')

#评论内容
result = re.compile(r'<span class="votes">(.*?)</span>.*?comment">(.*?)</a>.*?</span>.*?<span.*?class="">(.*?)</a>.*?<span>(.*?)</span>.*?title="(.*?)"></span>.*?title="(.*?)">.*?class=""> (.*?)\n', re.S)

while html.status_code == 200:
    url_next = 'https://movie.douban.com/subject/26363254/comments' + re.findall(reg, html.text)[0]
    zhanlang2 = re.findall(result, html.text)
    data = pd.DataFrame(zhanlang2)
    data.to_csv(r'D:\files\zl2.csv', header=False, index=False, mode='a+')
    data = []
    zhanlang2= []
    time.sleep(1)
    html = requests.get(url_next, cookies=cookies, headers=headers)