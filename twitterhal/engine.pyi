import datetime
import queue
import threading
from typing import Any, Dict, List, Optional, Sequence

import twitter
from megahal import MegaHAL
from twitter.ratelimit import EndpointRateLimit

from twitterhal.models import BaseDatabase, Tweet, TweetList
from twitterhal.twitter_api import TwitterApi


class DBInstance(BaseDatabase):
    posted_tweets: TweetList
    mentions: TweetList


class TwitterHAL:
    api: TwitterApi
    db: DBInstance
    force: bool
    generate_random_lock: threading.Lock
    include_mentions: bool
    megahal_open: bool
    megahal: MegaHAL
    mention_queue: queue.Queue[Tweet]
    post_queue: queue.Queue[Tweet]
    post_status_limit: EndpointRateLimit
    random_post_times: Sequence[datetime.time]
    screen_name: str
    test: bool

    def __enter__(self) -> "TwitterHAL": ...
    def __exit__(self, *args, **kwargs): ...
    def __init__(
        self,
        screen_name: Optional[str],
        random_post_times: Optional[Sequence[datetime.time]],
        include_mentions: Optional[bool],
        init_megahal: bool,
        force: bool,
        test: bool,
        **kwargs
    ): ...
    def _init_post_status_limit(self): ...
    def _post_tweet(self, tweet: Tweet): ...
    def _set_post_status_limit(self, subtract: int): ...
    def _time_for_random_post(self) -> bool: ...
    def can_do_request(self, url: str, count: int = 1) -> bool: ...
    def can_post(self, count: int = 1) -> bool: ...
    def close(self): ...
    def generate_random(self): ...
    def generate_tweet(self, in_reply_to: Optional[Tweet], prefixes: List[str], suffixes: List[str]) -> Tweet: ...
    def get_megahal_api_kwargs(self, **kwargs) -> Dict[str, Any]: ...
    def get_new_mentions(self): ...
    def get_twitter_api_kwargs(self, **kwargs) -> Dict[str, Any]: ...
    def init_db(self): ...
    def mark_mentions_answered(self): ...
    def open(self): ...
    def pop_mention_and_generate_reply(self): ...
    def post_from_queue(self): ...
    def post_random_tweet(self): ...
    def post_tweets_worker(self, restart: bool): ...
    def process_new_mention(self, mention: Tweet) -> Tweet: ...
    def register_loop_tasks(self): ...
    def register_post_loop_tasks(self): ...
    def register_workers(self): ...
