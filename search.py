from requests import get
from bs4 import BeautifulSoup as Bs
from urllib.parse import unquote as uq

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}

if __name__ == "__main__":
    while True:
        try:
            q = uq(input("搜索内容："), encoding="utf-8")
            page1 = 1
            page2 = 1

            page = get(url="https://cn.bing.com/search?q=" + q + "&first=" + str(page2), headers=headers)
            page.encoding = "utf-8"
            page = page.text
            page = Bs(page, "html5lib")

            num = 0
            while True:
                for tag in page.findAll(class_="b_algo"):
                    num += 1
                    print(str(num) + "." + tag.h2.a.text, end="\t")
                    print(tag.h2.a.attrs["href"])  # 提取链接
                    print("")  # 打印一个空行
                    for t in tag.findAll("a"):
                        print(t.text, t.attrs["href"])
                        t.clear()  # 清除内容避免被再次显示
                    for t in tag.findAll("p"):
                        print(t.text)
                    for t in tag.findAll("li"):
                        print(t.text)
                    print("=" * 50)  # 打印两个空行

                while True:
                    ch = input("要继续搜索吗？如是，输入“n”；如否，输入“e”：")
                    if ch == "n":
                        page1 += 1
                        if page1 == 2:
                            page2 = 6
                            break
                        else:
                            page2 = 6 * page1
                            break
                    elif ch == "e":
                        break
                    else:
                        continue
        except:
            print("错误")
            continue
