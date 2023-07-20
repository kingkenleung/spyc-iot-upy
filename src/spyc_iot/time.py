import time

def get_time_string(separator = ':'):
    current_time = time.gmtime()
    hour = f'{current_time[3] + 8:02}'
    minute = f'{current_time[4]:02}'
    
    return f'{hour}{separator}{minute}'