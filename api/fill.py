from api.utils import *


def fill_match_info(page_url, match_info, start_time=0, end_time=90):
    all_matches = get_all_matches(page_url, match_info['league'])
    home_team_matches, guest_team_matches = all_matches['home_team_matches'], all_matches['guest_team_matches']

    home_team_actions_list = []
    guest_team_actions_list = []

    TotalHome = len(home_team_matches)
    TotalAway = len(guest_team_matches)
    HomePositive = 0
    HomeNegative = 0
    AwayPositive = 0
    AwayNegative = 0
    Home_HT_1 = 0
    Away_HT_1 = 0

    for action in home_team_matches:
        actions_list = get_match_info_from_link(action)
        home_team_actions_list.append(actions_list)
        if matching_matches(actions_list, start_time, end_time):
            HomePositive += 1
        else:
            HomeNegative += 1

        if matching_matches(actions_list, 0, 45):
            Away_HT_1 += 1
    for action in guest_team_matches:
        actions_list = get_match_info_from_link(action)
        guest_team_actions_list.append(actions_list)
        if matching_matches(actions_list, start_time, end_time):
            AwayPositive += 1
        else:
            AwayNegative += 1
        if matching_matches(actions_list, 0, 45):
            Home_HT_1 += 1

    ForHome1_5 = number_of_goals_team(home_team_actions_list, 'home_team', 0, 5)
    ForHome6_10 = number_of_goals_team(home_team_actions_list, 'home_team', 6, 10)
    ForHome11_15 = number_of_goals_team(home_team_actions_list, 'home_team', 11, 15)
    ForHome16_20 = number_of_goals_team(home_team_actions_list, 'home_team', 16, 20)
    ForHome21_25 = number_of_goals_team(home_team_actions_list, 'home_team', 21, 25)
    ForHome26_30 = number_of_goals_team(home_team_actions_list, 'home_team', 26, 30)
    ForHome31_35 = number_of_goals_team(home_team_actions_list, 'home_team', 31, 35)
    ForHome36_40 = number_of_goals_team(home_team_actions_list, 'home_team', 36, 40)
    ForHome41_45 = number_of_goals_team(home_team_actions_list, 'home_team', 41, 45)
    ForHome46_50 = number_of_goals_team(home_team_actions_list, 'home_team', 46, 50)
    ForHome51_55 = number_of_goals_team(home_team_actions_list, 'home_team', 51, 55)
    ForHome56_60 = number_of_goals_team(home_team_actions_list, 'home_team', 56, 60)
    ForHome61_65 = number_of_goals_team(home_team_actions_list, 'home_team', 61, 65)
    ForHome66_70 = number_of_goals_team(home_team_actions_list, 'home_team', 66, 70)
    ForHome71_75 = number_of_goals_team(home_team_actions_list, 'home_team', 71, 75)
    ForHome76_80 = number_of_goals_team(home_team_actions_list, 'home_team', 76, 80)
    ForHome81_85 = number_of_goals_team(home_team_actions_list, 'home_team', 81, 85)
    ForHome86_90 = number_of_goals_team(home_team_actions_list, 'home_team', 86, 90)
    AgainstHome1_5 = number_of_goals_team(home_team_actions_list, 'guest_team', 0, 5)
    AgainstHome6_10 = number_of_goals_team(home_team_actions_list, 'guest_team', 6, 10)
    AgainstHome11_15 = number_of_goals_team(home_team_actions_list, 'guest_team', 11, 15)
    AgainstHome16_20 = number_of_goals_team(home_team_actions_list, 'guest_team', 16, 20)
    AgainstHome21_25 = number_of_goals_team(home_team_actions_list, 'guest_team', 21, 25)
    AgainstHome26_30 = number_of_goals_team(home_team_actions_list, 'guest_team', 26, 30)
    AgainstHome31_35 = number_of_goals_team(home_team_actions_list, 'guest_team', 31, 35)
    AgainstHome36_40 = number_of_goals_team(home_team_actions_list, 'guest_team', 36, 40)
    AgainstHome41_45 = number_of_goals_team(home_team_actions_list, 'guest_team', 41, 45)
    AgainstHome46_50 = number_of_goals_team(home_team_actions_list, 'guest_team', 46, 50)
    AgainstHome51_55 = number_of_goals_team(home_team_actions_list, 'guest_team', 51, 55)
    AgainstHome56_60 = number_of_goals_team(home_team_actions_list, 'guest_team', 56, 60)
    AgainstHome61_65 = number_of_goals_team(home_team_actions_list, 'guest_team', 61, 65)
    AgainstHome66_70 = number_of_goals_team(home_team_actions_list, 'guest_team', 66, 70)
    AgainstHome71_75 = number_of_goals_team(home_team_actions_list, 'guest_team', 71, 75)
    AgainstHome76_80 = number_of_goals_team(home_team_actions_list, 'guest_team', 76, 80)
    AgainstHome81_85 = number_of_goals_team(home_team_actions_list, 'guest_team', 81, 85)
    AgainstHome86_90 = number_of_goals_team(home_team_actions_list, 'guest_team', 86, 90)
    ForAway1_5 = number_of_goals_team(guest_team_actions_list, 'home_team', 0, 5)
    ForAway6_10 = number_of_goals_team(guest_team_actions_list, 'home_team', 6, 10)
    ForAway11_15 = number_of_goals_team(guest_team_actions_list, 'home_team', 11, 15)
    ForAway16_20 = number_of_goals_team(guest_team_actions_list, 'home_team', 16, 20)
    ForAway21_25 = number_of_goals_team(guest_team_actions_list, 'home_team', 21, 25)
    ForAway26_30 = number_of_goals_team(guest_team_actions_list, 'home_team', 26, 30)
    ForAway31_35 = number_of_goals_team(guest_team_actions_list, 'home_team', 31, 35)
    ForAway36_40 = number_of_goals_team(guest_team_actions_list, 'home_team', 36, 40)
    ForAway41_45 = number_of_goals_team(guest_team_actions_list, 'home_team', 41, 45)
    ForAway46_50 = number_of_goals_team(guest_team_actions_list, 'home_team', 46, 50)
    ForAway51_55 = number_of_goals_team(guest_team_actions_list, 'home_team', 51, 55)
    ForAway56_60 = number_of_goals_team(guest_team_actions_list, 'home_team', 56, 60)
    ForAway61_65 = number_of_goals_team(guest_team_actions_list, 'home_team', 61, 65)
    ForAway66_70 = number_of_goals_team(guest_team_actions_list, 'home_team', 66, 70)
    ForAway71_75 = number_of_goals_team(guest_team_actions_list, 'home_team', 71, 75)
    ForAway76_80 = number_of_goals_team(guest_team_actions_list, 'home_team', 76, 80)
    ForAway81_85 = number_of_goals_team(guest_team_actions_list, 'home_team', 81, 85)
    ForAway86_90 = number_of_goals_team(guest_team_actions_list, 'home_team', 86, 90)
    AgainstAway1_5 = number_of_goals_team(guest_team_actions_list, 'guest_team', 0, 5)
    AgainstAway6_10 = number_of_goals_team(guest_team_actions_list, 'guest_team', 6, 10)
    AgainstAway11_15 = number_of_goals_team(guest_team_actions_list, 'guest_team', 11, 15)
    AgainstAway16_20 = number_of_goals_team(guest_team_actions_list, 'guest_team', 16, 20)
    AgainstAway21_25 = number_of_goals_team(guest_team_actions_list, 'guest_team', 21, 25)
    AgainstAway26_30 = number_of_goals_team(guest_team_actions_list, 'guest_team', 26, 30)
    AgainstAway31_35 = number_of_goals_team(guest_team_actions_list, 'guest_team', 31, 35)
    AgainstAway36_40 = number_of_goals_team(guest_team_actions_list, 'guest_team', 36, 40)
    AgainstAway41_45 = number_of_goals_team(guest_team_actions_list, 'guest_team', 41, 45)
    AgainstAway46_50 = number_of_goals_team(guest_team_actions_list, 'guest_team', 46, 50)
    AgainstAway51_55 = number_of_goals_team(guest_team_actions_list, 'guest_team', 51, 55)
    AgainstAway56_60 = number_of_goals_team(guest_team_actions_list, 'guest_team', 56, 60)
    AgainstAway61_65 = number_of_goals_team(guest_team_actions_list, 'guest_team', 61, 65)
    AgainstAway66_70 = number_of_goals_team(guest_team_actions_list, 'guest_team', 66, 70)
    AgainstAway71_75 = number_of_goals_team(guest_team_actions_list, 'guest_team', 71, 75)
    AgainstAway76_80 = number_of_goals_team(guest_team_actions_list, 'guest_team', 76, 80)
    AgainstAway81_85 = number_of_goals_team(guest_team_actions_list, 'guest_team', 81, 85)
    AgainstAway86_90 = number_of_goals_team(guest_team_actions_list, 'guest_team', 86, 90)

    return {'Country': match_info['country'], 'Start': match_info['time'], 'League': match_info['league'],
            'Home': match_info['home_team'], 'Away': match_info['guest_team'], 'TotalHome': TotalHome,
            'TotalAway': TotalAway,
            'HomePositive': HomePositive, 'HomeNegative': HomeNegative, 'AwayPositive': AwayPositive,
            'AwayNegative': AwayNegative,
            'Home_HT_1': Home_HT_1, 'Away_HT_1': Away_HT_1,
            'ForHome1_5': ForHome1_5, 'ForHome6_10': ForHome6_10, 'ForHome11_15': ForHome11_15,
            'ForHome16_20': ForHome16_20, 'ForHome21_25': ForHome21_25,
            'ForHome26_30': ForHome26_30, 'ForHome31_35': ForHome31_35, 'ForHome36_40': ForHome36_40,
            'ForHome41_45': ForHome41_45, 'ForHome46_50': ForHome46_50,
            'ForHome51_55': ForHome51_55, 'ForHome56_60': ForHome56_60, 'ForHome61_65': ForHome61_65,
            'ForHome66_70': ForHome66_70, 'ForHome71_75': ForHome71_75,
            'ForHome76_80': ForHome76_80, 'ForHome81_85': ForHome81_85, 'ForHome86_90': ForHome86_90,
            'AgainstHome1_5': AgainstHome1_5, 'AgainstHome6_10': AgainstHome6_10,
            'AgainstHome11_15': AgainstHome11_15, 'AgainstHome16_20': AgainstHome16_20,
            'AgainstHome21_25': AgainstHome21_25, 'AgainstHome26_30': AgainstHome26_30,
            'AgainstHome31_35': AgainstHome31_35, 'AgainstHome36_40': AgainstHome36_40,
            'AgainstHome41_45': AgainstHome41_45, 'AgainstHome46_50': AgainstHome46_50,
            'AgainstHome51_55': AgainstHome51_55, 'AgainstHome56_60': AgainstHome56_60,
            'AgainstHome61_65': AgainstHome61_65, 'AgainstHome66_70': AgainstHome66_70,
            'AgainstHome71_75': AgainstHome71_75, 'AgainstHome76_80': AgainstHome76_80,
            'AgainstHome81_85': AgainstHome81_85, 'AgainstHome86_90': AgainstHome86_90, 'ForAway1_5': ForAway1_5,
            'ForAway6_10': ForAway6_10, 'ForAway11_15': ForAway11_15, 'ForAway16_20': ForAway16_20,
            'ForAway21_25': ForAway21_25, 'ForAway26_30': ForAway26_30,
            'ForAway31_35': ForAway31_35, 'ForAway36_40': ForAway36_40, 'ForAway41_45': ForAway41_45,
            'ForAway46_50': ForAway46_50, 'ForAway51_55': ForAway51_55,
            'ForAway56_60': ForAway56_60, 'ForAway61_65': ForAway61_65, 'ForAway66_70': ForAway66_70,
            'ForAway71_75': ForAway71_75, 'ForAway76_80': ForAway76_80,
            'ForAway81_85': ForAway81_85, 'ForAway86_90': ForAway86_90, 'AgainstAway1_5': AgainstAway1_5,
            'AgainstAway6_10': AgainstAway6_10, 'AgainstAway11_15': AgainstAway11_15,
            'AgainstAway16_20': AgainstAway16_20, 'AgainstAway21_25': AgainstAway21_25,
            'AgainstAway26_30': AgainstAway26_30, 'AgainstAway31_35': AgainstAway31_35,
            'AgainstAway36_40': AgainstAway36_40, 'AgainstAway41_45': AgainstAway41_45,
            'AgainstAway46_50': AgainstAway46_50, 'AgainstAway51_55': AgainstAway51_55,
            'AgainstAway56_60': AgainstAway56_60, 'AgainstAway61_65': AgainstAway61_65,
            'AgainstAway66_70': AgainstAway66_70, 'AgainstAway71_75': AgainstAway71_75,
            'AgainstAway76_80': AgainstAway76_80, 'AgainstAway81_85': AgainstAway81_85,
            'AgainstAway86_90': AgainstAway86_90}
