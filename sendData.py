exit()
crt = """curl 'http://canvas.ourscgy.ustc.edu.cn/canvas/update?count=-1' -H 'Pragma: no-cache' -H 'DNT: 1' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36' -H 'Accept: application/json, text/plain, */*' -H 'Cache-Control: no-cache' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: _ga=GA1.3.398996058.1493125830;iPlanetDirectoryPro=ucas-ccfa97864ba5f61ab069223a79d63271' -H 'Connection: keep-alive' -H 'Referer: http://canvas.ourscgy.ustc.edu.cn/' --compressed 2>/dev/null"""
src = """curl 'http://canvas.ourscgy.ustc.edu.cn/canvas/modify' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36' -H 'Content-Type: application/json;charset=UTF-8' -H 'Accept: application/json, text/plain, */*' --data-binary '{"canvas":[{"x":%d,"y":%d,"color":%d}],"count":50000}' --compressed 2>/dev/null"""

from subprocess import check_output as co
from json import loads as parse
from time import sleep
from random import random

def send(x,y,color):
    run = src%(x,y,color)
    # print "Run: ",run
    ans = co(run,shell=True)
    # print "Ans: ",ans
    print "%s paint at (%3d,%3d) with %d"%("Succ" if parse(ans)["flag"] else "Fail",x,y,color)

data=parse(co(crt,shell=True))["data"]

canvas = [[0 for j in xrange(200)] for i in xrange(200)]

for i in data:
    canvas[i["x"]][i["y"]]=i["color"]


with open("output","w") as f:
    for i in canvas:
        for j in i:
            b = (j%256)/256.
            j /= 256
            g = (j%256)/256.
            j /= 256
            r = (j%256)/256.
            f.write("%f %f %f\n"%(r,g,b))


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

l = len(paint)
print "Num: ",ll-l,ll,"Rank: ",100.*(ll-l)/ll,"%"

if l == 0:
    exit()

for i in xrange(10):
    idx = int(random()*l)
    while (paint[idx][2]==16181480) and (canvas[paint[idx][0]][paint[idx][1]]==16382716) and (random()>0.2):
        idx = int(random()*l)
    send(*paint[idx])
