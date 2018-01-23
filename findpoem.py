#!/usr/bin/env python
# coding: latin-1


import pymongo, subprocess, pyqrcode
from pymongo import MongoClient
from random import randint
from escpos import *
from PIL import Image

client = MongoClient()
db = client.pfoundation_data
poems = db.poems
count = poems.count()
print(count)
random = randint(1, count)

poem = poems.find_one({"number": random})

file = open('index.html', 'w')
file.truncate()

file.write("<!DOCTYPE html><head><link href='index.css' type='text/css' rel='stylesheet' /></head><body><img src='magazine-heading.png' class='logo'>")

print(poem["number"])

file.write("<div id='title'>" + poem["title"][0].encode("ascii", "xmlcharrefreplace") + "</div>")
file.write("<div id='author'>by " + poem["author"][0].encode("ascii", "xmlcharrefreplace") + "</div>")
file.write("<div id='poem'>" + poem["poem_text"] + "</div>")
file.write("<div id='credit'>" + poem["credit"] + "</div>")

url = pyqrcode.create("http://poetryfoundation.org" + poem["url"])
url.png('poemqrcode.png', scale=3)

file.write("<div class='qrcode'><img src='poemqrcode.png'><p>Scan this QR Code to visit this poem online, or visit poetryfoundation.org " + poem["url"] + "</p></div>")

url = pyqrcode.create("http://poetryfoundation.org" + poem["author_link"][0])
url.png('authorqrcode.png', scale=3)

file.write("<div class='qrcode'><img src='authorqrcode.png'><p>Scan this QR Code for more by this author, or visit poetryfoundation.org " + poem["author_link"][0] + "</p></div>")

file.write("</body></html>")

file.close()

subprocess.call(["phantomjs", "phantom.js"])

im = Image.open("poem.png")
im = im.convert('1')
width, height = im.size
if width > 512:
	box = (0, 0, 512, height)
	im = im.crop(box)
im.save("poem.png")
subprocess.call("png2pos -c -s 1 poem.png > /dev/usb/lp0", shell=True)