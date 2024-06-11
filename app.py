import tweetpy

# Twitter API anahtarlarınızı burada tanımlayın
api_key = 'YOUR_API_KEY'
api_secret_key = 'YOUR_API_SECRET_KEY'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Tweepy ile oturum açma
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Bloklanacak anahtar kelimeler
keywords = ['keyword1', 'keyword2', 'keyword3']

def block_users_with_keywords(keywords):
    for keyword in keywords:
        print(f"Searching for keyword: {keyword}")
        for user in tweepy.Cursor(api.search_users, q=keyword).items():
            try:
                if keyword.lower() in user.description.lower():
                    print(f"Blocking user: {user.screen_name}")
                    api.create_block(user.id)
            except tweepy.TweepError as e:
                print(f"Error blocking user: {e.reason}")
            except StopIteration:
                break

if __name__ == "__main__":
    block_users_with_keywords(keywords)