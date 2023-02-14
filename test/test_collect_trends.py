from src.tweet_collect.collect_trends import trends


def test():
    assert trends(615702) is not None
