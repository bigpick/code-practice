#!/usr/bin/env python

import numpy
from multiprocessing import Value, Pool, Manager
import random

# ruff: noqa

# Area of a circle is pi*r^2
# Estimate pi to 3 decimal places using a Monte Carlo method
#
# Basic equation of a circle is x^2+y^2 = r^2


# unit circle/square
# radius = 1
# square area  = 4*r^2
# circle area  = pi*r^2
#
# ratio of circle-square is = pi / 4
#
# assuming that the entirety of the circle and square were filled up, then the
# basis that pi / 4 = number of points in circle / number of points in square


def random_point_in_circle_numpy():
    return numpy.random.uniform(-1.0, 1.0) ** 2 + numpy.random.uniform(-1.0, 1.0) ** 2 <= 1


def random_point_in_circle():
    return random.uniform(-1.0, 1.0) ** 2 + random.uniform(-1.0, 1.0) ** 2 <= 1.0


if __name__ == "__main__":
    for TO_GENERATE in [
        1,
        10,
        100,
        1000,
        10_000,
        100_000,
        1_000_000,
        10_000_000,
    ]:  # 100_000_000, 1_000_000_000]:
        in_circle = 0
        for _ in range(TO_GENERATE):
            if random_point_in_circle():
                in_circle += 1

        print(
            f"Rough estimate of pi based on {TO_GENERATE} intervals: {4.0*(float(in_circle)/float(TO_GENERATE)):.3f}"
        )
