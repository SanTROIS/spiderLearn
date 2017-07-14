import re
import urllib.request
import bs4

def craw(url,page):
    html = urllib.request.urlopen(url).read()
    html = str(html)
    urllib.request.unquote(html)
    pat1 = '<ul class="bang_list clearfix bang_list_mode">.+</ul>'
    res1 = re.compile(pat1).findall(html)
    res1 = res1[0]
    #print(res1)
    pat2 = '<img src="http://(.+?\.jpg)" .*?>'
    imglist = re.compile(pat2).findall(res1)
    print(imglist)
    x = 1
    for img in imglist:
        imgname = 'E://spider/'+str(page)+str(x)+'.jpg'
        imgurl = "http://"+img
        try:
            urllib.request.urlretrieve(imgurl,filename=imgname)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x+=1
            if hasattr(e, "reason"):
                x+=1
        x+=1

for i in range(1,25):
    url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-"+str(i)
    craw(url, i)
