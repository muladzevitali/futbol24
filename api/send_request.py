from tables.proxies import proxies
import requests
import random
import sys
random.seed(17)


class ProxyRequest:
    """
    Class for sending proxy requests
    """
    def __init__(self):

        self._id = random.randint(0, len(proxies))
        self._current_proxy = proxies[self._id]

    def send_request(self, page_url):
        response = requests.get(page_url)
        if response.status_code == 200:
            return response
        else:

            for proxy in proxies[:]:
                try:
                    response = requests.get(page_url, proxies=self._current_proxy)
                    if response.status_code == 200:
                        return response
                    else:
                        self._id = random.randint(0, len(proxies))
                        self._current_proxy = proxies[self._id]
                        continue

                except Exception:

                    self._id = random.randint(0, len(proxies))
                    self._current_proxy = proxies[self._id]
                    continue
            print('No proxies left')
            sys.exit(0)


futblot24 = ProxyRequest()
