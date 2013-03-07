# -*- coding: utf-8 -*-
"""Management commands for PyTips."""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division


import requests
from twitter import Twitter
from flask.ext.script import Manager


import pytips
from pytips.models import Tip
from pytips.util import extract_publication_date, timeout
from pytips import app


manager = Manager(app)


def _get_embedded(tweet_id):
    """Get the embedded version of the tweet at ``tweet_id``."""
    payload = {'id': tweet_id}
    r = requests.get('https://api.twitter.com/1/statuses/oembed.json',
                     params=payload)
    return r.json()


def _is_oldstyle_rt(tweet):
    """Determine whether ``tweet`` is an old-style retweet."""
    return tweet['text'].startswith('RT @')


def _is_newstyle_rt(embedded_tweet):
    """Determine whether ``embedded_tweet` is a new-style retweet."""
    return requests.get(embedded_tweet['url']).status_code == 302


def _scrape_twitter_for_latest():
    """Scrape Twitter for interesting, new Python tips."""
    # This is the secret sauce: search Twitter for '#python tip' tweets that
    # are newer than our current newest.
    new_tweet = Tip.query.newest_tip()
    tweet_id = new_tweet.url.split('/')[-1] if new_tweet else None
    twitter_search = Twitter(domain='search.twitter.com')
    hits = twitter_search.search(q='#python tip', since_id=tweet_id)['results']
    # And now filter out all the retweets.
    not_old_rts = [t for t in hits if not _is_oldstyle_rt(t)]
    embedded_tweets = [_get_embedded(t['id_str']) for t in not_old_rts]
    return [t for t in embedded_tweets if not _is_newstyle_rt(t)]


def _tip_from_tweet(embedded):
    """Convert a ``dict`` we got from Twitter into a ``Tip``."""
    t = Tip()
    t.author_name = embedded['author_name']
    t.author_url = embedded['author_url']
    t.publication_date = extract_publication_date(embedded['html'])
    t.rendered_html = embedded['html']
    t.url = embedded['url']
    return t


@manager.command
@timeout(30)
def importnew():
    """Pull in new Python tips from select sources around the internet."""
    latest_from_twitter = _scrape_twitter_for_latest()
    tips = [_tip_from_tweet(tweet) for tweet in latest_from_twitter]
    pytips.db.session.add_all(tips)
    pytips.db.session.commit()


if __name__ == "__main__":
    manager.run()
