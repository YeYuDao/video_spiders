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
        # ":authority": "m.tiktok.com",
        # ":method": "GET",
        # ":path": "/v/6807062880429624581.html?u_code=0&preview_pb=0&language=en&timestamp=1585971382&utm_campaign=client_share&app=musically&utm_medium=ios&tt_from=copy&utm_source=copy",
        # ":scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        # "cookie": "tt_webid_v2=6808327775670945285; _ga=GA1.2.1193159756.1585881199; bm_mi=C7AD3F94D9461EFA6A9FC749A9AE25EF~3jBHXfKJikx4FGGHMc+KrjtymxXQkEtoBsTFkZSdcslYlshcyswgqXyeYJ0Q+fq4eXPeFpSrXJ8SO2dIBIZlISLzlxwcfHleUW+IvEHlJBsFz+Q3m+uClp3ZZiAS2fgIUmbeC6J/SWR4EwnuvgS+IR3kKyrVvYxr9BqvEAN6L/Jeq3nHj3kiYe9HCiNXraICVwkPSTVxSFcfOyvXWPfNHMv2rueRyuoA/+6S0pvn86UKc3Orqp8OHiln0cByWcpoX1MzRsknqYpTHCVBaepbx8x3Gw3pS+ll4pEowD5ZQNFjH6dP9k7r+2ii9vkn7INzjYB0G3uJuAGTcT8mokniAA==; ak_bmsc=7444E80E7CBFCCD2FF47DE0333B7F879173FF046D32C00000501885E050EE915~plPznWuDYSnhR66NBaymBRyzFz92J/J3dI0M61LYDCiMUMNZWElNmFeLJEvsOh0hPyRlMfsJYwKT4h9xKhGfduAbt4lwrNt6weslVqie8cK6+sd6+b6ei7qbmJV19grFC9YX3pSvoZac2t5S6pTa+u2HBDgQ/GDez5hBTb2MvJ+iSKBDdma+8MnNR+50lnJUjaLwKrja9Opt8lK65DD2EzEUczwwi0lDhnJbVizTV2Ugoe6Z4eaKhw9LvTagWGuuVn; _gid=GA1.2.130434010.1585971469; bm_sv=2BB8D2E3B724B1CB27BC411E4BF8CBA9~lIgoXhgR9467OTnfGwTXT+GRKeZZfYZzx84VxChkKWQIS1u5a1wrYAjU4VnTRCqbyilWMPsJLjtzlKq7gRRoo4Rj/N6B6nn5eAj6TvDo0yYDbw02RHmP28ADGcYGiFlGnqCh75CePEiAnVGOeQDTiCsev6vHqx5HagETxrLgSj0=; _gat_gtag_UA_144727112_1=1",
        "dnt": "1",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    re_video = r'<video.*? src="(.*?)".*?></video>'
    re_title = r'<h1 class="jsx-1038045583 jsx-861547433 jsx-3645511632 video-meta-title"><strong>(.*?)</strong>.*?</h1>'

    with requests.get(url, headers=headers, timeout=10) as rep:
        if rep.status_code == 200:
            title = re.findall(re_title, rep.text)
            video = re.findall(re_video, rep.text)
            if title:
                data["title"] = title[0]
            if video:
                data["videos"] = video
        else:
            data["msg"] = "失败"
    return data


if __name__ == "__main__":
    url = "https://vm.tiktok.com/tSHtv6/"
    print(get(url))
