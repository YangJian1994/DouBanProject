import pandas as pd
import re
import requests
import time

url_first = 'https://movie.douban.com/subject/26363254/comments?start=0'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
cookies = {'cookie': 'your cookies'}
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
