import csv

from api.fill import fill_match_info
from api.headers import headers

page_url = 'https://www.futbol24.com/teamCompare/Thailand/Chonburi-FC/vs/Thailand/Nakhon-Ratchasima/?statTALR-Table=1&' \
           'statTALR-Limit=2&statTBLR-Table=2&statTBLR-Limit=2'
a = {'home_team': 'asdas',
     'guest_team': 'guest',
     'country': 'georgia',
     'league': 'D1',
     'page_link': page_url}

row = fill_match_info(page_url, a, 0, 25)

with open('results/test_row.csv', "w") as csv_file:
    writer = csv.DictWriter(csv_file, headers)
    writer.writeheader()
    writer.writerow(row)
