from urllib import request
from bs4 import BeautifulSoup
import requests
import os

root = "D://照片//头像//爬取//"
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
}
# url = 'http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book'
url = "https://www.woyaogexing.com/touxiang/katong/2018/704657.html"
name = "动漫情侣头像"


def cbk(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print
    "%.2f%%" % percent


def getHtmlCode(url):
    url1 = request.Request(url, headers=headers)
    page = request.urlopen(url1).read().decode()
    return page


def getImg(page, name):
    soup = BeautifulSoup(page, 'html.parser')  # 按照html格式解析页面
    # book_list = soup.find(attrs={"id": "book"})  # 找到id为book的标签,这是包含所有书名信息的最底层标签

    img_list = soup.find(attrs={"class": "artCont cl"})
    img_list_img = img_list.find_all('a')
    i = 1
    for img_one in img_list_img:
        img_url = img_one.get('href')
        # print(img_url)
        img_url = "https:" + img_url
        print(img_url)
        path = root + name + str(i) + ".jpeg"
        download(img_url, path)
        i += 1


def download(url, path):
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url, headers=headers)
            r.raise_for_status()
            with open(path, 'wb') as f:
                f.write(r.content)
            f.close()
            print("Save " + path + " success!")
        else:
            print("文件已存在")
    except:
        print("Fail")


page = getHtmlCode(url)
getImg(page, name)
