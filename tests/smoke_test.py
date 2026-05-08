import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from ..main import load_json
from code.solution import Solution

solution = Solution(load_json())

def test_example_1_two_stops_available():
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    solution(n, flights, src=0, dst=3, k=1)
    assert solution.find_cheapest_price() == 700

def test_example_2_enough_stops_for_cheaper_route():
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    solution(n, flights, src=0, dst=3, k=2)
    assert solution.find_cheapest_price() == 400

def test_example_3_direct_flight_no_stops_needed():
    n = 3
    flights = [[0, 1, 50], [1, 2, 50], [0, 2, 200]]
    solution(n, flights, src=0, dst=2, k=0)
    assert solution.find_cheapest_price() == 200
