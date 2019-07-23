import tweepy 
import datetime
#Twitter API credentials

class ActualizarTweets:
    consumer_key = "Ggk57p3drEosK9hTSxbhL3CmA"
    consumer_secret = "W9GIt7Y6Yh83EuqjsG7MNwtZagejC4lmR0M85DiI6bSo2ag6W2"
    access_key = "1484656237-LFagke97ZfacrZUb70lFuMoUnltizO9mer45m1K"
    access_secret = "0DPSpJVwecmmmvoj1SK9PNjWUQaJQHgO9YnYNQYmkpZ7r"
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