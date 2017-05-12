crt = """curl 'http://canvas.ourscgy.ustc.edu.cn/canvas/update?count=-1' -H 'Pragma: no-cache' -H 'DNT: 1' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36' -H 'Accept: application/json, text/plain, */*' -H 'Cache-Control: no-cache' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: _ga=GA1.3.398996058.1493125830;iPlanetDirectoryPro=ucas-ccfa97864ba5f61ab069223a79d63271' -H 'Connection: keep-alive' -H 'Referer: http://canvas.ourscgy.ustc.edu.cn/' --compressed 2>/dev/null"""

from subprocess import check_output as co
from json import loads as parse
from time import sleep
from random import random
import sys

data=parse(co(crt,shell=True))["data"]

canvas = [[-1 for j in xrange(300)] for i in xrange(300)]

for i in data:
    canvas[i["x"]][i["y"]]=i["color"]

paint = []

ll = 0

for i in open("data","r"):
    ll += 1
    p = i.split("\t")
    if len(p) is not 3:
        continue
    data = map(int,i.split("\t"))
    if canvas[data[0]][data[1]] != data[2]:
        paint.append(data)

#l = len(paint)
#print "Num: ",ll-l,ll,"Rank: ",100.*(ll-l)/ll,"%"


for i in paint:
    print i[0],i[1],i[2]