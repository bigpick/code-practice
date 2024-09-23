#!/usr/bin/env python3

# Given a date, return the corresponding day of the week for that date.
#
# The input is given as three integers representing the day, month and year respectively.
#
# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday",
# "Wednesday", "Thursday", "Friday", "Saturday"}.

from datetime import datetime

TEST_CASES = [(31, 8, 2019, "Saturday"), (18, 7, 1999, "Sunday"), (15, 8, 1993, "Sunday")]


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekdays = {
            6: "Sunday",
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
        }
        return weekdays[datetime(year=year, day=day, month=month).weekday()]


for test_case in TEST_CASES:
    assert Solution().dayOfTheWeek(test_case[0], test_case[1], test_case[2]) == test_case[3]
