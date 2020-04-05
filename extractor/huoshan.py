import json
from urllib.parse import urlparse

import requests
import re

def get(url: str) -> dict:
    """
    text、videos
    """
    data = {}
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        # "cookie": "tt_webid=6812140250611090957; SLARDAR_WEB_ID=122f7989-b43b-41d2-8e71-f1d4190dba9e",
        "dnt": "1",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    }

    re_item_id = r'.*?item_id=(.*?)&.*?'
    video_url = 'https://api.huoshan.com/hotsoon/item/video/_reflow/?item_id='

    with requests.get(url, headers=headers, timeout=10) as rep:
        if rep.status_code == 200:
            item_id = re.findall(re_item_id, rep.url)[0]
            video = video_url + str(item_id)
            # print("title:", title)
            data["title"] = "huoshan_" + str(item_id)
            data["videos"] = [video]
        else:
            data["msg"] = "失败"
    return data


if __name__ == "__main__":
    url = "https://share.huoshan.com/hotsoon/s/asDsse8Fd78/"
    print(get(url))

    # https://api.huoshan.com/hotsoon/item/video/_reflow/?video_id=v0200c920000bq0pcbr2ap9a6qh022r0&line=0&app_id=0&vquality=normal&watermark=2&long_video=0&sf=5&ts=1586076166&item_id=6809889252898393352
    # https://share.huoshan.com/pages/item/index.html?item_id=6809889252898393352&tag=10615&timestamp=1586074912&watermark=2&media_type=4&schema_url=sslocal://item?id=6809889252898393352
