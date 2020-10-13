import urllib.request
from bs4 import BeautifulSoup
import re

def main():
    url = 'http://baike.baidu.com/view/284853.html'
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,"html.parser")

    for each in soup.find_all(href = re.compile("view")):
        print(each.text,"->",''.join(["http://baike.baidu.com",each["href"]]))

if __name__ == "__main__":
    main()