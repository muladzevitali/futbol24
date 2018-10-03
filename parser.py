from api.get_matches import save_matches_to_csv

_DATE = '20181002'
START_TIME = 0
END_TIME = 25
save_matches_to_csv(_DATE, f'results/demo_{_DATE}.csv', start_time=START_TIME, end_time=END_TIME)
