import tweepy 
import datetime
import configparser

class ActualizarTweets:
    #Twitter API credentials
    config = configparser.ConfigParser()
    config.read('twitterApi.ini')
    consumer_key = config['API']['consumer_key']
    consumer_secret = config['API']['consumer_secret']
    access_key = config['API']['access_key']
    access_secret = config['API']['access_secret']
    def nombreLinea(tweet_texto):
        linea=""
        for caracter in tweet_texto:
            if caracter == " ":
                return linea
            linea+=caracter

    def get_all_tweets(screen_name):
        #Twitter only allows access to a users most recent 3240 tweets with this method
        
        #authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(ActualizarTweets.consumer_key, ActualizarTweets.consumer_secret)
        auth.set_access_token(ActualizarTweets.access_key, ActualizarTweets.access_secret)
        api = tweepy.API(auth)
        #initialize a list to hold all the tweepy Tweets
        alltweets = []
        #make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200)
        #save most recent tweets
        alltweets.extend(new_tweets)
        #save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        #keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            print ("getting tweets before "+str(oldest))
            #all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
            #save most recent tweets
            alltweets.extend(new_tweets)
            #update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1
            print ("... "+str(len(alltweets))+" tweets downloaded so far")
        outtweets = [[tweet.created_at, tweet.text] for tweet in alltweets]
        return outtweets