import re
from random import random
from time import sleep
import traceback
import requests
import json


def parse_text(js_tweet_text_container,
               is_remove_url=False,
               is_remove_mentions=False,
               is_remove_hashtags=False,
               is_remove_cashtags=False,
               is_remove_emojis=False,
               ):

    hashtags = []
    cashtags = []
    mentions = []
    emojis = dict()

    try:
        a_hrefs = js_tweet_text_container.p(['a', 'img'])

        for s in a_hrefs:
            if s.has_attr('data-expanded-url'):
                if is_remove_url:
                    s.extract()
            elif s.has_attr('data-query-source'):
                if s.attrs['data-query-source'] == 'cashtag_click':
                    cashtags.append(s.text.strip())
                    if is_remove_cashtags:
                        s.extract()
                elif s.attrs['data-query-source'] == 'hashtag_click':
                    hashtags.append(s.text.strip())
                    if is_remove_hashtags:
                        s.extract()

            elif s.has_attr('data-mentioned-user-id'):
                mentions.append(s.text.strip())
                if is_remove_mentions:
                    s.extract()
            elif s.has_attr('class') and 'Emoji--forText' in s.attrs['class']:
                emoji_alt = s.attrs['alt']
                emoji_title = '_'.join(s.attrs['title'].split())
                emojis[emoji_title] = emoji_alt
                if is_remove_emojis:
                    s.extract()
                else:
                    s.append(emoji_title)
    except TypeError:
        pass

    text = js_tweet_text_container.getText(separator=' ').encode('utf-8')
    text = re.sub('"|\n', ' ', text)
    text = re.sub(' +', ' ', text).strip()

    hashtags = '|'.join(hashtags).encode('utf-8')
    cashtags = '|'.join(cashtags).encode('utf-8')
    mentions = '|'.join(mentions).encode('utf-8')
    emojis = json.dumps(emojis) if emojis else ''

    return [text, hashtags, cashtags, mentions, emojis]



def parse_footer(stream_item_footer):
    # retweets = stream_item_footer.find('div', attrs={'title': 'Retweet'}).text
    retweets = stream_item_footer.find('span', class_=re.compile('retweet$')).text
    retweets = re.sub('[^0-9]', '', retweets)
    if retweets == '': retweets = u'0'

    # likes = stream_item_footer.find('div', attrs={'title': 'Like'}).text
    likes = stream_item_footer.find('span', class_=re.compile('favorite$')).text
    likes = re.sub('[^0-9]', '', likes)
    if likes == '': likes = u'0'


    return [retweets, likes]


def parse_fixer(js_tweet_details_fixer):
    # time = js_tweet_details_fixer.find('div', class_='client-and-actions').text.strip()
    stats = js_tweet_details_fixer.find('div', class_='js-tweet-stats-container tweet-stats-container ')
    try:
        retweets = stats.find('a', class_='request-retweeted-popup').text
        retweets = re.sub('[^0-9]', '', retweets)
    except AttributeError:
        retweets = '0'

    try:
        likes = stats.find('a', class_='request-favorited-popup').text
        likes = re.sub('[^0-9]', '', likes)
    except AttributeError:
        likes = '0'

    return [retweets, likes]


def parse_header(header_soup):
    timestamp = header_soup.find('span', class_=re.compile('timestamp$')).attrs.get('data-time')
    return [timestamp]


def parse_properties(soup):
    try:
        tweet_wrap = soup.find('div', class_=re.compile('js-stream-tweet|permalink-tweet'))
    except:
        return [False, False, False, False]
    properties = tweet_wrap.attrs
    uid = properties.get('data-user-id')
    tid = properties.get('data-item-id')
    screen_name = properties.get('data-screen-name')
    rid = properties.get('data-retweet-id', '')
    return [uid, screen_name, tid, rid]

def parse_quotetweet(quotetweet_container):
    try:
        properties = quotetweet_container.find('div', class_=re.compile('QuoteTweet-innerContainer')).attrs
        screen_name = properties.get('data-screen-name')
        tid = properties.get('data-item-id')
        text = quotetweet_container.find('div', class_='tweet-content').get_text(separator=' ', strip=True).encode('utf-8')
        return [screen_name, tid, text]
    except:
        return ['', '', '']

def get_html(url, n_retry=5):
    for i in xrange(n_retry):
        try:
            html = requests.request('GET', url).text
            return html
        except requests.ConnectionError:
            sleep(random() * 60)
            print 'Connection error', i,
        except requests.TooManyRedirects:
            sleep(60 * random())
            return None
    return None
