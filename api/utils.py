import praw
from django.http import HttpResponse

from api.config import praw_config


def send_reddit_message(msg):
    try:
        data = praw_config()
        if data is None:
            raise NotImplementedError()

        r = praw.Reddit(username=data["un"], password=data["pw"], client_id=data["cid"], client_secret=data["cs"],
                        user_agent=data["ua"])
        r.redditor('Ttime5').message(msg)
        return HttpResponse(status=200)
    except Exception as e:
        response = HttpResponse(
            "<h1>Error</h1>Something went wrong.")
        response.status_code = 500
        print(e)
        return response

def send_email():
    pass