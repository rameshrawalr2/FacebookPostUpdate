# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 03:00:26 2018
UpdateFacebookStatus
@author: ramesh rawal
Update facebook status written python program
"""

import facebook
def main():
    cfg = {
    "page_id": "735450933311179",
    "access_token": "EAACCPkOPeagBAKRCAH530jNEVZC6EyZBwIff29oZBTR9OZAGvXYqZCZAHQC6J1vHw5hrfpHAoFpmpCnjEJS9ZCG8wAw7ZCHeFanhoIZCWZCbaxLmWFgN1jMyhKzYTgjaT9wBAUnni4G7ZBDfMkz0mkB33RkxGG5u2V1P5h8ZBTZCnEK2A6VvK87fUBVqrnmPP6p4wYdSYzvlpS0YrJQZDZD"
    }
    api = get_api(cfg)
    msg = raw_input("Enter your post: ")
    status = api.put_wall_post(msg)

def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    """
    resp = graph.get_object('me/rawal.ramesh391')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
    graph = facebook.GraphAPI(page_access_token)
    """
    return graph


if __name__ == "__main__":
    main()
