import pandas as pd
import requests

class animeList:
    def __init__(self, year, season):
        self.year = year
        self.season = season

        url = 'http://api.moemoe.tokyo/anime/v1/master/{}/{}'.format(self.year, self.season)
        self.jsonFile = requests.get(url).content
        self.makeList = pd.read_json(self.jsonFile)

    def getInfo (self):
        return self.makeList[['title', 'twitter_account', 'public_url']]

    def output (self):
        tmp = ['冬アニメ', '春アニメ', '夏アニメ', '秋アニメ']
        csvName = '{}年{}.csv'.format(self.year, tmp[self.season -1])
        self.makeList.to_csv(csvName, index=False)

def weeklyFollower (twitter):
    url = 'http://api.moemoe.tokyo/anime/v1/twitter/follower/history/daily?account={}'.format(twitter)
    r = requests.get(url)
    return pd.read_json(r.content)
