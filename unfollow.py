import instaloader
from instagram_private_api import Client, ClientCompatPatch
import time
from credentials import username, password  # Import your Instagram credentials

# Initialize Instaloader
L = instaloader.Instaloader()

# Login to Instagram using Instaloader
L.login(username, password)
myusername = username
mypassword = password
# Load the user's profile
profile = instaloader.Profile.from_username(L.context, username)

# Get followers and followees
followers = set(profile.get_followers())
followees = set(profile.get_followees())

# Calculate who is not following you back
not_following_back = followees - followers

# Extract usernames of users not following back
not_following_back_usernames = [user.username for user in not_following_back]

# Print results
print(f"Number of people not following back: {len(not_following_back_usernames)}")
print("Users not following back:")
for username in not_following_back_usernames:
    print(username)

print(username)
# Initialize Instagram Private API Client
api = Client(myusername, mypassword)

# Function to unfollow users who are not following back
def unfollow_non_followers(usernames):
    for username in usernames:
        user_info = api.username_info(username)
        user_id = user_info['user']['pk']
        try:
            api.friendships_destroy(user_id)
            print(f"Unfollowed user: {username}")
            time.sleep(2)  # Sleep to avoid rate limits
        except Exception as e:
            print(f"Error unfollowing user {username}: {e}")

# Unfollow users who are not following back
unfollow_non_followers(not_following_back_usernames)
