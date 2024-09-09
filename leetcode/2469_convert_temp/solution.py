#!/usr/bin/env python3

# You are given a non-negative floating point number rounded to two decimal places
# celsius, that denotes the temperature in Celsius.
#
# You should convert Celsius into Kelvin and Fahrenheit and return it as an array
# ans = [kelvin, fahrenheit].
#
# Return the array ans. Answers within 10-5 of the actual answer will be accepted.

# Note that:
#
#    Kelvin = Celsius + 273.15
#    Fahrenheit = Celsius * 1.80 + 32.00

TEST_CASES = [(36.50, [309.65000, 97.70000]), (122.11, [395.26000, 251.79800])]


class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        def _to_kelvin(celsius: float) -> float:
            return round(celsius + 273.15, 5)

        def _to_farenheit(celius: float) -> float:
            return round(celsius * 1.8 + 32.0, 5)

        return [_to_kelvin(celsius), _to_farenheit(celsius)]


for test_case in TEST_CASES:
    assert Solution().convertTemperature(test_case[0]) == test_case[1]
