#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv
import codecs
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
topnum=1

def GetUrl(first_url):
    try:
        # 模拟浏览器
        req = urllib2.Request(first_url)
        req.add_header("User-Agent",
                       " Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134")
        page = urllib2.urlopen(req)
        page_info = page.read()#.decode("utf-8")
        # print page_info
    except:
        print("Failed to PageInfo ")
        return ''
    else:
        return page_info


#爬取书名
def GetTitle(page_info):
    global topnum
    nameList=re.findall(r'<a href="https:\/\/book.*?".*?target="_blank">(.*?)</a>',page_info,re.S)
    newNameList=[]
    for index,item in enumerate(nameList):
        if item.find("img")==-1:#通过检测img,只保留中文标题
            if topnum%26 !=0:
                out=re.sub(u"\\（.*?\\）|\\《.*?\\》", '', item)
                newNameList.append(out)
            topnum+=1
    return newNameList

#每本书的评价总数
def GetComtNum(page_info):
    CtList =re.findall(r'<span>(.*?)</span>',page_info,re.S)  #<span>(1064人评价)</span> #返回一个查询的列表
    newCtList=[]
    for index,item in enumerate(CtList):
        if item.find("评价") >= 1:#如果“评价”出现的位置不在开头，即前面有数字
            newCtList.append(item)
    return newCtList

#爬取评分
def GetScore(page_info):
    ScoreList=re.findall(r'<span.*?class="rating_nums">(.*?)</span>',page_info,re.S)
    return ScoreList

#爬取作者
def GetWriter(page_info):
    # WriterList=re.findall(r'<div class="pl">作者(.*?)<br>', html, re.S)
    # return WriterList
    WriterList = re.findall(r'<div class="abstract">(.*?)<br', page_info, re.S)  # 包含书的作者，出版社等信息的div标签

    return  WriterList



#保存爬到的信息：
def SaveInfotoCsv(allInfo):
        with open("D:/book_spiderInfo.csv",'wb') as fp:
            fp.write(codecs.BOM_UTF8)#encode = 'gb18030'
            #excel打开csv文件，可以识别编码“GB2312”，但是不能识别“utf-8”
            a=csv.writer(fp,delimiter=',')#delimiter是插入到csv文件中的一行记录以它分隔开
            a.writerow(['书名', '评分', '评价人数'])
            a.writerows(allInfo)
            print("Successfully Write to File")

def SaveInfotiTxt(nameList):
    f=codecs.open("D:/spider.txt",'w', encoding="utf-8")
    for item in nameList:
        f.write(item.encode("utf-8"))
        f.write('\n')
    f.close()



# -------------------------------主程序----------------------
# 翻页

nameUrl=[]#存放书名
scoreUrl=[]#存放评分
commtUrl=[]#评价人数
writerUrl=[]#作者
allInfo = []#总信息列表,形式为[[书名，评分，人数],[...],[...]]
for n in range(0,100,25):
    first_url="https://www.douban.com/doulist/1264675/?start="+str(n) #目标网页
    page_info = GetUrl(first_url).decode("UTF-8");
    if page_info == '':
        nameUrl.extend('none')
        scoreUrl.extend('none')
        commtUrl.extend('none')
        writerUrl.extend('none')
    else:
        nameUrl.extend(GetTitle(page_info))
        scoreUrl.extend(GetScore(page_info))
        commtUrl.extend(GetComtNum(page_info))
        writerUrl.extend( (GetWriter(page_info)) )

nameUrl.pop()#删除最后一个无用的元素


for i in range(0,len(nameUrl)):
    tmp=[]
    tmp.append(nameUrl[i])
    tmp.append(scoreUrl[i])
    tmp.append(commtUrl[i])
    tmp.append(writerUrl[i])
    allInfo.append(tmp)

SaveInfotoCsv(allInfo)
SaveInfotiTxt(nameUrl)











