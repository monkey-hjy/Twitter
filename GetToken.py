# author:   Spider
# datetime: 2021/1/13 15:29
# software: PyCharm
import requests
import re


class GetToken(object):
    def __init__(self):
        self.get_token_url = 'http://mobile.twitter.com/'
        self.get_token_headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Upgrade-Insecure-Requests': '1',
        }

    def get_token(self, proxies_ip):
        proxies = {
            'http': f'http://{proxies_ip}',
            'https': f'http://{proxies_ip}',
        }
        err_count = 0
        while err_count < 5:
            try:
                response = requests.get(url=self.get_token_url, headers=self.get_token_headers, timeout=10,
                                        proxies=proxies)
                print(response)
                print(response.text)
                result = re.findall(r'document.cookie.*gt=(.*?); Max-Age', response.text)
                return result[0]
            except:
                err_count += 1
