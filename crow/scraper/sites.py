class Site(object):
  def __init__(self, name, urls):
    self.name = name
    self.urls = urls

class Article(object):
  def __init__(self, title, site, url):
    self.title = title
    self.site = site
    self.url = url
    self.content = ""

class Author(object):
  def __init__(self, name):
    self.name = name
    self.articles = []