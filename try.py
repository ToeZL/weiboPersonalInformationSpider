#coding=utf-8
import requests
import re
from bs4 import BeautifulSoup

#获取的cookie值存放在这
myHeader = {"Cookie":"_T_WM=7baf7462c672f84f26e64421b220ede5; ALF=1519958782; SCF=AgNknec4_f6zBsz6KGkzy6m21FLzb33RS4VZWlKwNqkVXETFweKy_Lf9cgoDuD3IgxLdlhIL7IfsDDUVUEqsoBE.; SUB=_2A253dSzoDeRhGeBK6FAQ9inMzjSIHXVUmbSgrDV6PUJbktAKLUPakW1NR9PKhEgnAjocLauDNmHG_JQSbOTvdRU6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhJG8csW7YL6sIHZqwLBfcR5JpX5K-hUgL.FoqXe0zpSoM7SKn2dJLoI74uIc_uI02Ee0z7eKM7entt; SUHB=0pHB9cU4AbKzqK; SSOLoginState=1517378744"}

weiboList = [
'5484511719',
'2658495375'
]

for weibo in weiboList:
    url = 'https://weibo.cn/'+str(weibo)+'/info'
    r = requests.get(url ,headers=myHeader).content
    soup = unicode(BeautifulSoup(r, 'html.parser'))
    #soup.prettify()
    #divTag = soup.find_all('div', attrs={"class" : "c"})
    #print(str(divTag))
    #for tag in divTag:
        #for c in tag.find_all(text=True):
    nickname = re.findall(u'\u6635\u79f0[:|\uff1a](.*?)<br', soup)   #昵称
    gender = re.findall(u'\u6027\u522b[:|\uff1a](.*?)<br', soup)  # 性别
    address = re.findall(u'\u5730\u533a[:|\uff1a](.*?)<br', soup)  # 地区（包括省份和城市）
    birthday = re.findall(u'\u751f\u65e5[:|\uff1a](.*?)<br', soup)  # 生日
    desc = re.findall(u'\u7b80\u4ecb[:|\uff1a](.*?)<br', soup)  # 简介
    sexorientation = re.findall(u'\u6027\u53d6\u5411[:|\uff1a](.*?)<br', soup)  # 性取向
    marriage = re.findall(u'\u611f\u60c5\u72b6\u51b5[:|\uff1a](.*?)<br', soup)  # 婚姻状况
    homepage = re.findall(u'\u4e92\u8054\u7f51[:|\uff1a](.*?)<br', soup) #首页
    url2 = 'https://weibo.cn/'+str(weibo)
    r2 = requests.get(url2, headers=myHeader).content
    soup2 = unicode(BeautifulSoup(r2, 'html.parser'))
    tweets_count = re.findall(u'\u5fae\u535a\[(\d+)\]', soup2)
    follows_count = re.findall(u'\u5173\u6ce8\[(\d+)\]', soup2)
    fans_count = re.findall(u'\u7c89\u4e1d\[(\d+)\]', soup2)
    web_page = 'https://weibo.cn/'+str(weibo)+'/info'
    reg_date = re.findall(r"\d{4}-\d{2}-\d{2}", web_page)
    tag_url = 'https://weibo.cn/account/privacy/tags/?uid='+str(weibo)
    r3 = requests.get(tag_url, headers=myHeader).content
    soup_tag = BeautifulSoup(r3, 'html.parser')
    res = soup_tag.find_all('div', {"class": "c"})
    tags = "|".join([elem.text for elem in res[2].find_all("a")])
    userinfo = {}
    userinfo["uid"] = str(weibo)
    userinfo["nickname"] = nickname[0] if nickname else ""
    userinfo["gender"] = gender[0] if gender else ""
    userinfo["address"] = address[0] if address else ""
    userinfo["birthday"] = birthday[0] if birthday else ""
    userinfo["desc"] = desc[0] if desc else ""
    userinfo["sex_orientation"] = sexorientation[0] if sexorientation else ""
    userinfo["marriage"] = marriage[0] if marriage else ""
    userinfo["homepage"] = homepage[0] if homepage else ""
    userinfo["tweets_count"] = tweets_count[0] if tweets_count else "0"
    userinfo["follows_count"] = follows_count[0] if follows_count else "0"
    userinfo["fans_count"] = fans_count[0] if fans_count else "0"
    userinfo["reg_date"] = reg_date[0] if reg_date else ""
    userinfo["tags"] = tags if tags else ""
    x = userinfo.get('uid') +','+ userinfo.get('nickname') +','+ userinfo.get('gender') +','+ userinfo.get('address') +','+ userinfo.get('birthday') +','+userinfo.get('desc') +','+ userinfo.get('sex_orientation') +','+ userinfo.get('marriage') +','+ userinfo.get('homepage') +','+ userinfo.get('tweets_count') +','+userinfo.get('follows_count') +','+ userinfo.get('reg_date') +','+ userinfo.get('tags')
    print("Recording text")
    f = open("weibo.txt", "a")
    f.write(x.encode('utf-8') + '\n')
    f.close
