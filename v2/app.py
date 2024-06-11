import tweetpy

# (Replace with your actual Twitter API credentials)
api_key = 'YOUR_API_KEY'
api_secret_key = 'YOUR_API_SECRET_KEY'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Improved authentication handling
def authenticate_api():
    try:
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        return tweepy.API(auth)
    except tweepy.TweepyError as e:
        print(f"Error during authentication: {e}")
        return None  # Indicate authentication failure

# Bloklanacak anahtar kelimeler (list)
keywords = ['keyword1', 'keyword2', 'keyword3']

def block_users_with_keywords(api, keywords):
    for keyword in keywords:
        print(f"Searching for keyword: {keyword}")
        try:
            for user in tweepy.Cursor(api.search_users, q=keyword).items(100):  # Limit to 100 users per iteration for API rate limiting
                try:
                    if keyword.lower() in user.description.lower():
                        print(f"Blocking user: {user.screen_name}")
                        api.create_block(user.id)
                except tweepy.TweepError as e:
                    print(f"Error blocking user {user.screen_name}: {e.reason}")
        except StopIteration:
            break

if __name__ == "__main__":
    # Authenticate before blocking
    api = authenticate_api()
    if api is not None:
        block_users_with_keywords(api, keywords)
    else:
        print("Authentication failed. Please check your credentials.")
