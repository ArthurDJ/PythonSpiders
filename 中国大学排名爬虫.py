import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print("get success")
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    # 查找tbody标签并遍历
    # tr即为每一所大学信息，标签类型
    for tr in soup.find('tbody').children:
        # 检测tr标签的类型
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            # 将我们需要的信息加入tds
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    # 20 univs
    printUnivList(uinfo, 20)


if __name__ == '__main__':
    main()
