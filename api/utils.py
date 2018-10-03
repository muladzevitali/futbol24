import time

import scrapy

from api.send_request import futblot24

_BASE_URL = 'https://www.futbol24.com'


def get_all_matches(page_url, current_league):
    time.sleep(10)
    response = futblot24.send_request(page_url)
    home_team_urls = get_home_team_matches_from_link(response, current_league)
    away_team_urls = get_guest_team_matches_from_link(response, current_league)

    return {'home_team_matches': home_team_urls, 'guest_team_matches': away_team_urls}


def get_home_team_matches_from_link(response, current_league):
    """
    Returns First table from match url:
        'https://www.futbol24.com/teamCompare/Thailand/Chonburi-FC/vs/Thailand/Nakhon-Ratchasima/
        ?statTALR-Table=1&statTALR-Limit=2&statTBLR-Table=2&statTBLR-Limit=2'
    :param response:
    :param current_league:string -- league short name: D1, 	LC etc...
    :return: list -- links of popups from each match
    """
    page = scrapy.Selector(response)
    current_league_matches = []

    all_matches = page.xpath("""//div[@id="statTALR"]//div[@class="table loadingContainer"]//tr""")

    for match in all_matches:
        match_league = match.xpath(""".//td[@class='comp']/a/text()""").extract_first()
        if not match_league:
            continue
        if match_league == current_league:
            match_link = match.xpath(""".//td[@class='dash']/a/@href""").extract_first()
            current_league_matches.append(_BASE_URL + match_link)

    return current_league_matches


def get_guest_team_matches_from_link(response, current_league):
    """
    Returns First table from match url:
        'https://www.futbol24.com/teamCompare/Thailand/Chonburi-FC/vs/Thailand/Nakhon-Ratchasima/
        ?statTALR-Table=1&statTALR-Limit=2&statTBLR-Table=2&statTBLR-Limit=2'
    :param response:
    :param current_league:string -- league short name: D1, 	LC etc...
    :return: list -- links of popups from each match
    """
    page = scrapy.Selector(response)
    current_league_matches = []

    all_matches = page.xpath("""//div[@id="statTBLR"]//div[@class="table loadingContainer"]//tr""")

    for match in all_matches:
        match_league = match.xpath(""".//td[@class='comp']/a/text()""").extract_first()
        if not match_league:
            continue
        if match_league == current_league:
            match_link = match.xpath(""".//td[@class='dash']/a/@href""").extract_first()
            current_league_matches.append(_BASE_URL + match_link)

    return current_league_matches


def get_match_info_from_link(page_link):
    """
    Get match details
    :param page_link: string -- page url of match details
    :return: list -- [{minute: {'home_team': home_team_score, 'guest_team': guest_team_score,
                                    first_half': first_half, 'second_half': second_half}}]
    """
    time.sleep(10)
    response = futblot24.send_request(page_link)
    page = scrapy.Selector(response)
    actions = page.xpath(""".//tbody/tr""")
    # Dictionary for writing match actions
    actions_list = []

    number_of_goals = {}
    for _index in range(len(actions)):

        minute = actions[_index].xpath(""".//td[@class='status']/text()""").extract_first()
        score = actions[_index].xpath(""".//td[@class='result']/text()""").extract_first()
        if _index > 0 and score == actions[_index - 1].xpath(""".//td[@class='result']/text()""").extract_first():
            continue

        if score.strip() == '-':
            continue

        first_team_score = int(score.split('-')[0].strip())
        second_team_score = int(score.split('-')[1].strip())

        # Check for extra time in halves

        if '+' in minute:
            minute = int(minute.split('+')[0])
            if number_of_goals.get(minute):
                number_of_goals[minute] += 1
            else:
                number_of_goals[minute] = 1

            actions_list.append(
                {minute: {'home_team': first_team_score, 'guest_team': second_team_score,
                          'number_of_goals': number_of_goals}})
            continue
        # If no extra time
        elif minute.isdigit():
            minute = int(minute)
            # If extra time
            if minute > 90:
                minute = 90
                if number_of_goals.get(minute):
                    number_of_goals[minute] += 1
                else:
                    number_of_goals[minute] = 1

                actions_list.append(
                    {minute: {'home_team': first_team_score, 'guest_team': second_team_score,
                              'number_of_goals': number_of_goals}})
                continue
        else:
            continue

        # Add if normal time
        number_of_goals[minute] = 1
        actions_list.append(
            {minute: {'home_team': first_team_score, 'guest_team': second_team_score, 'number_of_goals': 1}})

    return sorted(actions_list, key=lambda x: list(x.keys())[0])


# Tested
def matching_matches(actions_list, start_time=0, end_time=200):
    """
    Check if goal was in the interval: [start_time, end_time]
    :param actions_list: list -- list of match actions
    :param start_time: int -- start time
    :param end_time: int -- end time
    :return: bool -- if there was any goal in that interval
    """
    minutes_of_goals = [list(each.keys())[0] for each in actions_list]
    for each in minutes_of_goals:
        if start_time <= each <= end_time:
            return True
    return False


# Tested
def number_of_goals_in_interval(actions_list, start_time=0, end_time=200):
    """
    Counts number of goals in the interval: [start_time, end_time]
    :param actions_list: list -- list of match actions
    :param start_time: int -- start time
    :param end_time: int -- end time
    :return: int -- number of goals from start time to end time
    """
    minutes_of_goals = [list(each.keys())[0] for each in actions_list]
    number_of_goals = 0
    for each in minutes_of_goals:
        if start_time <= each <= end_time:
            number_of_goals += actions_list[each]['number_of_goals']

    return number_of_goals


# Tested
def number_of_goals_team(actions, team, start_time=0, end_time=200):
    """
    Counts number of goals of home or guest team in the interval: [start_time, end_time]
    :param actions: list -- list of matches actions
    :param team: string -- 'home_team' or 'guest_team'
    :param start_time: int -- start time
    :param end_time: int -- end time
    :return: int -- number of goals from start time to end time from that specific team
    """
    number_of_goals = 0
    for actions_list in actions:
        goals_in_match = 0
        # Filter only goals in interval
        actions_list = [action for action in actions_list if start_time <= list(action.keys())[0] <= end_time]
        actions_dict = {}
        for each in actions_list:
            actions_dict.update(each)

        for minute, action in actions_dict.items():
            if actions_dict[minute][team] != number_of_goals:
                goals_in_match = actions_dict[minute][team]

        number_of_goals += goals_in_match
    return number_of_goals


def get_time(time_string):
    """
    Get time from string representation
    :param time_string: string -- time numbers
    :return: string -- time of the format 23:20
    """
    end_time = int(time_string)
    start_time = 1538510400
    difference = end_time - start_time

    hours = (difference % 86400) // 3600
    minutes = (difference % 3600) // 60

    hours = str(hours) if hours > 0 else '00'
    minutes = str(minutes) if minutes > 0 else '00'
    _time = """{}:{}""".format(hours, minutes)

    return _time
