# 1538442000 - 05:00
#     1538444100 - 05:35
#     1538467200 12:00


def get_time(time_string):
    start_time = 1538510400
    difference = time_string - start_time
    hours = (difference % 86400) // 3600
    minutes = (difference % 3600) // 60

    return hours, minutes


print(get_time(1538499600))