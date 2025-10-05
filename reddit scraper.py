import praw
import sys

print("Authenticating...")

reddit = praw.Reddit(
    client_id="vHaTXPxLWxZOJs-LdCJ9jQ",
    client_secret="1bdLqpaKe9Ai2ZjIhPV3YkbGmpRUAw",
    user_agent="python"
)

print("Getting subreddit...")

subreddit = reddit.subreddit("askreddit")

total = ""

numSub = int(input("How many submissions do you want to scrape: "))

print("Getting submissions...")
for submission in subreddit.hot(limit=numSub):
    submission.comments.replace_more(limit=0)
    if submission.comments:
        total += submission.title + " ||| "
        top_comment = submission.comments[0]
        total += top_comment.body + " ### "

print("Writing file...")
with open("reddit_file.txt", "w", encoding="utf-8") as f:
    f.write(total)