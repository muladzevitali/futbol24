import json


def parse_leagues(json_response):
    """
    52133: {'name': 'Prim B Metropolitana', 'sname': 'D3M'}
    :param json_response:
    :return:
    """
    desired_teams = dict(dict(json_response["F24"])["Kraje"])['K']
    _dict = json.loads(json.dumps(desired_teams))

    all_leagues = {}
    for country in _dict:
        leagues = country['L']
        if type(leagues) == dict:
            all_leagues.update({int(leagues['@LId']): {'name': leagues['@LN'], 'sname': leagues['@LNK']}})
            if leagues.get('PL'):
                sub_leagues = leagues.get('PL')
                if type(sub_leagues) == dict:
                    all_leagues.update(
                        {int(sub_leagues['@LId']): {'name': sub_leagues['@LN'], 'sname': sub_leagues['@LNK']}})
                else:
                    for sub_league in sub_leagues:
                        all_leagues.update(
                            {int(sub_league['@LId']): {'name': sub_league['@LN'], 'sname': sub_league['@LNK']}})

        else:
            for league in leagues:
                all_leagues.update({int(league['@LId']): {'name': league['@LN'], 'sname': league['@LNK']}})

                if league.get('PL'):
                    sub_leagues = league.get('PL')
                    if type(sub_leagues) == dict:
                        all_leagues.update(
                            {int(sub_leagues['@LId']): {'name': sub_leagues['@LN'], 'sname': sub_leagues['@LNK']}})
                    else:
                        for sub_league in sub_leagues:
                            all_leagues.update(
                                {int(sub_league['@LId']): {'name': sub_league['@LN'], 'sname': sub_league['@LNK']}})

    return all_leagues
