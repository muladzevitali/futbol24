import csv
from multiprocessing import Pool

import xmltodict

from api.fill import fill_match_info
from api.headers import headers
from api.send_request import futblot24
from scripts.utils import parse_leagues
from tables.countries import countries
import os
from api.utils import get_time
_FIELD_NAMES = headers
if not os.path.isdir('results'):
    os.mkdir('results')


def save_matches_to_csv(date, csv_file_path, start_time=0, end_time=25):
    """
    Parses main page and saves matches in csv
    :param end_time:
    :param start_time:
    :param date: string -- '20180929'
    :param csv_file_path: string -- path to string file
    :return:
    """
    csv_file = open(csv_file_path, "w")
    writer = csv.DictWriter(csv_file, _FIELD_NAMES)
    writer.writeheader()
    csv_file.flush()

    url = f'https://www.futbol24.com/matchDayXml/?Day={date}'
    response = futblot24.send_request(url)

    dict_response = xmltodict.parse(response.content.decode('utf-8'))
    json_response = dict(dict_response)
    desired_teams = dict(dict(json_response["F24"])["Mecze"])['M']

    leagues = parse_leagues(json_response)

    pool_arguments = [(each, leagues, start_time, end_time, csv_file_path) for each in desired_teams]
    pool = Pool()
    pool.map(fill_multiple, pool_arguments)

    csv_file.close()


def fill_multiple(_tuple):

    _BASE_URL = 'https://www.futbol24.com/teamCompare'
    team, leagues = _tuple[:2]
    start_time, end_time = _tuple[2:4]
    csv_file_path = _tuple[4]
    csv_file = open(csv_file_path, "a")
    writer = csv.DictWriter(csv_file, _FIELD_NAMES)

    if team['@S1']:
        return 0
    country_id = int(team['@KId'])
    country = countries[country_id]['name'].replace(' ', '-')

    league_id = int(team['@LId'])
    league = leagues[league_id]['sname']

    home_team = team['@HN'].replace(' ', '-')
    guest_team = team['@GN'].replace(' ', '-')
    time_string = team['@C0']
    print(f'Getting details of match {home_team} vs {guest_team}')

    page_link = f'{_BASE_URL}/{country}/{home_team}/vs/{country}/{guest_team}/' \
                f'?statTALR-Table=1&statTALR-Limit=2&statTBLR-Table=2&statTBLR-Limit=2'
    page_link = page_link.replace(')', '').replace('(', '')
    row_dict = {'home_team': home_team,
                'time': get_time(time_string),
                'guest_team': guest_team,
                'country': country,
                'league': league,
                'page_link': page_link}

    row = fill_match_info(page_link, row_dict, start_time, end_time)

    writer.writerow(row)
    csv_file.flush()


