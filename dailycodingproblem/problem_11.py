#!/usr/bin/env python

from time import sleep
from typing import Callable

def schedule(n: int, f: Callable, *args, **kwargs):
    sleep(n / 1000)
    f(*args, **kwargs)

def dummy():
    print("Hello!!")

def dummy_greet(name: str):
    print(f"Hello, {name}!!")


schedule(1000, dummy)

schedule(1000, dummy_greet, "world")
