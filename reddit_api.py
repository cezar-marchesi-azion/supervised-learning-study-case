import praw
import config
import os
from dotenv import load_dotenv

load_dotenv()

api_reddit = praw.Reddit(
    client_id=os.environ.get('REDDIT_CLIENT_ID'),
    client_secret=os.environ.get('REDDIT_CLIENT_SECRET'),
    password=os.environ.get('REDDIT_PASSWORD'),
    user_agent=os.environ.get('REDDIT_USER_AGENT'),
    username=os.environ.get('REDDIT_USER_NAME'),
)
