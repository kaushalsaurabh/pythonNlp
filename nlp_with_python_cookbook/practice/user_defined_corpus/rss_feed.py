'''This program reads from an RSS feed.
A Rich Site Summary (RSS) feed is a computer-readable format in which regularly changing content on the Internet is delivered.
Most of the websites that provide information in this format give updates, for example, news articles, online publishing and so on.
It gives the listeners access to the updated feed at regular intervals in a standardized format.
pip install feedparser '''

import feedparser

# Load the content in memory
myFeed = feedparser.parse("http://feeds.mashable.com/Mashable")

#Check the title and count the number of posts in the current feed
print('Feed Title:', myFeed['feed']['title'])
print('Number of posts:', len(myFeed.entries))

# Title of the very first post
post = myFeed.entries[0]
print('First post title:', post.title)

# Access the raw HTML content
print('\nRaw HTML content:', post.content[0].value)

