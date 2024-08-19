#!/usr/bin/env python3

"""
res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

bob@dylan:~$ ./0-main.py
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
"""


def index_range(page: int, page_size: int) -> tuple:
    """function that takes the page and page_number then retruns the range """
    y = page * page_size   
    range = y - page_size 
    return (range, y)
