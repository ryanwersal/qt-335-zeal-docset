#!/bin/env python2

import os, re, sqlite3
from bs4 import BeautifulSoup, NavigableString, Tag

def clean_path(path):
	return path.strip().split("#")[0]
def clean_url(url):
	return "html/%s" % url.strip()
def read_file(path):
	with open(os.path.join(docpath, path)) as f:
		return f.read()

db = sqlite3.connect("qt335.docset/Contents/Resources/docSet.dsidx")
cur = db.cursor()

try:
	cur.execute("DROP TABLE searchIndex;")
except:
	pass

cur.execute("CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);")
cur.execute("CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);")

docpath = "qt335.docset/Contents/Resources/Documents/html"

page = read_file("classes.html")
soup = BeautifulSoup(page)

class_info = [(a.text.strip(), clean_path(a.attrs["href"]), clean_url(a.attrs["href"])) for a in soup.find_all("table")[1].find_all("a") if a.text.strip()]
for class_name, path, url in class_info:
	cur.execute("INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?, ?, ?);", (class_name, "Class", url))

	page = read_file(path)
	soup = BeautifulSoup(page)
	fn_info = [(a.text.strip(), a.attrs["href"].strip()) for a in soup.select("li.fn a") if a.text.strip()]
	for fn_name, fn_url in fn_info:
		entry_name = "%s::%s" % (class_name, fn_name)
		entry_url = url + fn_url
		cur.execute("INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?, ?, ?);", (entry_name, "Method", entry_url))

db.commit()
db.close()
