"""
GURAY YILDIRIM YAZILIMCILARA 
TAVSİYE TWEETLERINI CEKME

BİLAL YAŞAR TARAFINDAN YAZILDI
 
"""
import requests # python3x request kütüphanesi
from bs4 import BeautifulSoup

twitsayfasi = "https://twitter.com/GurayYildirimTR"# imdb-url olmadı ımdburl yaptın

r = requests.get(twitsayfasi)#sayfa kaynagı r nın ıcende

soup = BeautifulSoup(r.content,"html.parser")

gelen_veri = soup.find_all("p",{"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
#print(gelen_veri)

for i in gelen_veri:
	#print(i.text)
	if i.text[0] == "[":
		print(i.text)





