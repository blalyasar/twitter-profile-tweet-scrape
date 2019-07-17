"""
GURAY YILDIRIM YAZILIMCILARA 
TAVSİYE TWEETLERINI CEKME

BİLAL YAŞAR TARAFINDAN YAZILDI
BUGRA ISGUZARA ÇOK TESEKKURLER
 
"""
from lib.twitter_scraper import get_tweets # gerekli kutuphaneyi ice aktar

for tweet in get_tweets("GurayYildirimTR"): # kullanicinin tum tweetlerini cek ve liste halinde donguye sok
    if not tweet['isRetweet'] and tweet['text'].startswith('['): # eger bu bir RT degilse ve [ ile baslıyorsa
        print(tweet['text'])	

