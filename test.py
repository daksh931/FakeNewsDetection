from ScrapeTweets import scrapedata
from predictions import pre

df = scrapedata()


output = pre(list(df['text']))

print(output)