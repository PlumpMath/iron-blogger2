"""Utility module for dealing with dates.

Most of the Iron Blogger specific logic is book keeping about dates;
unsurprisingly there are a few generic helpers we need that aren't in the
standard library.
"""
from datetime import timedelta
import arrow
from ironblogger import config

ROUND_LEN = timedelta(weeks=1)


def set_tz(dt):
    return arrow.get(dt).to('UTC').datetime


def duedate(post_date):
    """The due date for which a post published on ``post_date`` counts.

    preconditions:

        isinstance(post_date, datetime)
    """

    post_date = arrow.get(post_date).to(config.cfg['timezone'])
    # Luckily, the arrow library considers Sunday to be the last day of the
    # week, so we don't need to do any special adjustment. NOTE: we need to
    # return an actual datetime object; sqlalchemy won't store an Arrow in the
    # database.
    return post_date.ceil('week').to('UTC').datetime


def rssdate(date_obj, cfg=None):
    """Format ``date_obj`` as needed by rss.

    This is *almost* as specified in rfc822, but the year is 4 digits instead
    of two.
    """
    if cfg is None:
        cfg = config.cfg
    return arrow.get(date_obj).to(cfg['timezone']).strftime('%d %b %Y %T %z')


def divide_timedelta(numerator, denominator):
    """Divide two timedelta objects.

    The timedelta type doesn't have it's own divide operator, which
    is something we need in a few places.

    The return value is of type int, not timedelta.
    """
    return numerator.total_seconds()/denominator.total_seconds()
