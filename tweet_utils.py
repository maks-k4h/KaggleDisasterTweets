import re


def process_tweet(tweet, lower=True, rm_weblinks=False, keep_usernames=True, keep_hashtags=True):
    """
    Removes and modifies the tweet.

    :param tweet: the tweet's text.
    :type lower: the result will be converted to lower case if set.
    :param rm_weblinks: Entirely removes hyperlinks if set, leaves hostnames otherwise.
    :param keep_usernames: if False entire username is removed, otherwise only eliminates '@' symbol.
    :param keep_hashtags: if False entire hashtag is removed, otherwise only eliminates '#' symbol.
    :return: processed contents without redundant whitespaces.
    """

    res = tweet

    if lower:
        res = res.lower()

    # weblinks
    res = re.sub(r'https?://([\w.-]+)(/\S+)?', '' if rm_weblinks else r'\g<1>', res)

    # usernames
    res = re.sub(r'@(\S*)', r'\g<1>' if keep_usernames else '', res)

    # hashtags
    res = re.sub(r'#(\S*)', r'\g<1>' if keep_hashtags else '', res)

    # punctuation
    res = re.sub(r'(\S+?)[.,:;!?]+\s|'
                 r'(\S+?)[.,:;!?]+$',
                 r'\g<1>\g<2> ',
                 res)

    # parentheses
    res = re.sub(r'[\[\](){}]|'
                 r'\s\[\'\"]+|'
                 r'[\'\"]+\s|'
                 r'[\'\"]+$', ' ', res)

    return re.sub(r'\s', ' ', res).strip()

