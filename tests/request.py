from api.send_request import futblot24

page_url = 'https://www.futbol24.com/teamCompare/Thailand/Chonburi-FC/vs/Thailand/Nakhon-Ratchasima/?statTALR-Table=1&' \
           'statTALR-Limit=2&statTBLR-Table=2&statTBLR-Limit=2'

response = futblot24.send_request(page_url)
print(response)
