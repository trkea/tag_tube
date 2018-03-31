# coding:utf-8

import urllib2
from bs4 import BeautifulSoup

def get_HTML(url):
    
    html = urllib2.urlopen(url)

    soup = BeautifulSoup(html, "html.parser")

    return soup

class youtubeValue():

    def __init__(self,url):

        self.url = url

    def get_movie_tag(self):

        get_tag = ""

        soup = get_HTML(self.url)

        meta = soup.find_all("meta")

        for tag in meta:

            try:
                string_ = tag.get("name")

                if not string_ == None and string_ in "keywords":
                    get_tag = tag.get("content")
                    break

            except AttributeError:
                pass

        return get_tag

    def get_movie_title(self):

        soup = get_HTML(self.url)

        title = soup.find("title").string

        get_title= title.rstrip(" - YouTube")

        return get_title
