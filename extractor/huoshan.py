import json
from urllib.parse import urlparse

import requests
import re

def get(url: str) -> dict:
    """
    text、videos
    """
    data = {}
    # headers = {
    #     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "accept-encoding": "gzip, deflate, br",
    #     "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    #     "dnt": "1",
    #     "sec-fetch-dest": "document",
    #     "sec-fetch-mode": "navigate",
    #     "sec-fetch-site": "none",
    #     "upgrade-insecure-requests": "1",
    #     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    # }

    re_item_id = r'.*?item_id=(.*?)&.*?'
    info_url = "https://share.huoshan.com/api/item/info?item_id="
    video_url = 'https://api.huoshan.com/hotsoon/item/video/_playback/?video_id='

    with requests.get(url, timeout=10) as rep:
        if rep.status_code == 200:
            item_id = re.findall(re_item_id, rep.url)[0] # get item_id
            info_url = info_url + str(item_id)
            r = requests.get(info_url, timeout=4)   # get info, request without headers
            if r.status_code == 200:
                info = r.json()
                if info['status_code'] == 0:
                    data["title"] = "huoshan_" + str(item_id)
                    video_id = re.findall('http.*?video_id=(.*?)&.*?',      # get video_id
                                          info['data']['item_info']['url'])[0]
                    data["videos"] = [video_url+str(video_id)] # finally, get the video  without watermark
    if not data:
        data["msg"] = "失败"
    print(data)
    return data


if __name__ == "__main__":
    url = "https://share.huoshan.com/hotsoon/s/asDsse8Fd78/"
    url = "https://share.huoshan.com/hotsoon/s/fCTJlIuUe78/"
    url = "https://share.huoshan.com/hotsoon/s/QfwNi34Te78/"
    print(get(url))
