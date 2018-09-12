# BeautifulSoup 모듈 불러오기
from bs4 import BeautifulSoup

# html 인자 넘겨주기 
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# main()
if __name__  == "__main__":
    soup = BeautifulSoup(html_doc, 'html.parser')
    print('1. ', soup.title)
    # title 태그 전문 출력 
    print('2. ', soup.title.name)
    # title 태그 출력
    print('3. ', soup.title.string)
    # title 태그에 있는 내용 출력 
    print('4. ', soup.title.parent.name)
    # 해당 태그의 부모 태그 출력
    print('5. ', soup.p)
    # p 태그 전문 
    print('6. ', soup.p['class'])
    # 속성이 class인 p 태그 출력 
    print('7. ', soup.a)
    # a 태그 전문 출력 
    print('8. ', soup.find_all('a'))
    # a 태그 전문 출력 
    print('9. ', soup.find(id="link3"))
    # id가 link3인 태그 찾기 
