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
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "n.miaopai.com",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    re_title = r'<div class="SharePostCard__content"><span.*?</span>(.*?)</div>'
    re_video = r'<video src="(.*?)".*?></video>'

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "DNT": "1",
        "Host": "n.miaopai.com",
        "Proxy-Connection": "keep-alive",
        "Referer": url,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    smid = url.split('/')[-1].replace('.htm', '')
    _jsonp = "_jsonp65jwe4k5nc6"
    info_url = "http://n.miaopai.com/api/aj_media/info.json?smid=%s&appid=530&_cb=%s" % (smid, _jsonp)

    re_info = f'window.{_jsonp}.*?{_jsonp}\((.*?)\)'

    with requests.get(info_url, headers=headers, timeout=10) as rep:
        if rep.status_code == 200:

            info = re.findall(re_info, rep.text)
            if info:
                info = json.loads(info[0])
                if info['code'] == 200:
                    data["title"] = info['data']['description']
                    data["videos"] = [info['data']['meta_data'][0]['play_urls']['m']]

                
        if not data:
            data["msg"] = "失败"

    return data


if __name__ == "__main__":
    url = "http://n.miaopai.com/media/80WTYF~Zvnv6Cmy30o1aLwM6KQ40y~uG.htm"
    print(get(url))
