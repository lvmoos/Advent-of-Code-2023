import time
import requests

from config.config import path_session_cookie

# Helper functions
def timer_function(func, data, n_run=1):
    ti = time.time()
    for i in range(n_run):
        func(data)
    tf = time.time()
    
    print(f'Runtime: {(tf - ti)/n_run} s')

def aoc_input_fetch(day, year):
    """
    fetches the input data from the website
    day: the day of december to fetch
    """
    # Fetch session cookie value from local file
    with open(path_session_cookie,'r') as f:
        key = f.read()
    cookie = {'session': key}
    url= f"https://adventofcode.com/{year}/day/{day}/input"

    with requests.Session() as s:
        r = s.get(url, cookies = cookie).text
        if 'Please log in' in r:
            print(r)
            input_lst = None
        else:
            # Data always end with a blanc line. Data is split on line change
            txt = r[:-1]
            input_lst = txt.split('\n')

    return input_lst, txt

def list_str_to_num(lst_str, num_type):
    if num_type == 'int':
        lst_num = list(map(int, lst_str))
    elif num_type == 'float':
        lst_num = list(map(float, lst_str)) 
        
    return lst_num
