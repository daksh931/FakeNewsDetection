def scrapedata():
    import tweepy
    import pandas as pd
    import time
    from datetime import datetime
    # tweepy version -- Tweepy-3.10.0
    # it scrape data for last 7 days

    access_key = "VBp1CHESKBmyxoINLTYEmwoKV"
    access_secret = "duc3R3I23N87aeDU8JGRlLej3HQ4vU6Ed5CJh52Ila90HQdzcS"

    consumer_key = "1580398407398539264-sP6yHHAQ1RswLEQbJZPuqwOnSnA1n2"
    consumer_secret = "RtxaUNEzTwC7qVT0hwNjOlFmTBpLlkZZ6rPMhCEDK7suw"


    # Twitter Authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key , consumer_secret)

    # Creating API
    api =  tweepy.API(auth,wait_on_rate_limit=True)

    #until:2022-10-28 since:2022-10-27
    tweets_df = pd.DataFrame()
    text_query = "news (news OR crypto OR latest ) lang:en "
    count = 5
    try:
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.search,q=text_query).items(count)
        
        # Pulling information from tweets iterable object
        tweets_list= []
        for tweet in tweets:
            
            

            refined_tweet = {"user_name" : tweet.user.screen_name,
                            'text' : tweet.text,
                            'favourite_count' : tweet.favorite_count,
                            'retweet_count' : tweet.retweet_count,
                            'created_at' : tweet.created_at ,
                            "followers_count": tweet.user.followers_count,
                                "friends_count": tweet.user.friends_count, 
                                'location' : tweet.user.location,
                                'total_tweets' : tweet.user.statuses_count
                                }

            tweets_list.append(refined_tweet)


        #  tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
        
        # Creation of dataframe from tweets list
        # Add or remove columns as you remove tweet information
        tweets_df = pd.DataFrame(tweets_list)
        # print(tweets_df)
        # tweets_df.to_csv('TwitterDataNew.csv')
    
    except BaseException as e:
        print('failed on_status,',str(e))
        time.sleep(3)


    return tweets_df
# df = scrapedata()    
# df.to_csv('TwitterData-15-13.csv')