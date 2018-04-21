# coding:utf-8

from bottle import route, run,template,request
import urllib2
import youtubeValue
from bs4 import BeautifulSoup

@route('/tag_tube',method="GET")

def send_URL():
    url = request.query.get('URL')
    return template("index")

@route('/tag_tube/result',method=["POST","GET"])

def result():
    movie_tag = ""
    title = ""
    try:
        url =  request.forms.get('URL') 
        html = urllib2.urlopen(url)
    except Exception:
        title = u"エラー URLが不正です"
        return   template("result",title=title,movie_tag=movie_tag)
    if url.find("youtube") == -1:
        title = u"エラー YoutubeのURLを入力して下さい"
        return  template("result",title=title,movie_tag=movie_tag)

    youtube = youtubeValue.youtubeValue(url)
    movie_tag = youtube.scrape_movie_tag()
    title = youtube.scrape_movie_title()

    if title == None and movie_tag == "":
        title = u"この動画は存在しません"
    elif not title == None and movie_tag == "":
        movie_tag = u"なし"
    elif title == None and not movie_tag == "":
        title = u"動画タイトルの読み込みに失敗しました"
    return  template("result",title=title,movie_tag=movie_tag)

run(host='localhost', port=8081, debug=True)