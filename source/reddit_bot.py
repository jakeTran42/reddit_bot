import praw
import config
import time
from datetime import datetime
import os

zero_two_alias = ['Zero Two', 'zerotwo', 'ZeroTwo', 'zero two', 'Zerotwo', '002']


def bot_login():
    reddit = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "002-Post-Responder v0.1")
    return reddit

def run_bot(r, comment_replied_list):
    for comment in r.subreddit('AlphaHunter').comments(limit=50):
        if 'Zero Two'in comment.body or 'zerotwo' in comment.body or 'ZeroTwo' in comment.body or 'zero two' in comment.body or 'Zerotwo' in comment.body or '002' in comment.body:
            if comment.id not in comment_replied_list and comment.author != r.user.me():
                comment.upvote()
                comment.reply('[Must Protecc!!](https://imgur.com/gallery/p6hKI)')
                print('Replied to ' + comment.id)
                comment_replied_list.append(comment.id)
                writing_to_list(comment.id)


def  get_comment_list():
    with open('comment_list.txt', "r") as file:
            comment_list = file.read().split('\n')
            comment_list = filter(None, comment_list)
    return list(comment_list)
            

def writing_to_list(content):

    with open('comment_list.txt', 'a') as file:
        file.write('{}'.format(content) + '\n')
    file.close()

def main():
    r = bot_login()
    comment_list = get_comment_list()
    while True:
        run_bot(r, comment_list)
        print('Done Running At --', time.ctime())
        # datetime.now().strftime('%m/%d/%Y - %H:%M:%S PST')
        time.sleep(10)


main()