import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from src.solution import Solution

def test_example_1_two_stops_available():
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    solution = Solution({"n": n, "flights": flights, "src": 0, "dst": 3, "k": 1})
    assert solution.find_cheapest_price() == 700

def test_example_2_enough_stops_for_cheaper_route():
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    solution = Solution({"n": n, "flights": flights, "src": 0, "dst": 3, "k": 2})
    assert solution.find_cheapest_price() == 400

def test_example_3_direct_flight_no_stops_needed():
    n = 3
    flights = [[0, 1, 50], [1, 2, 50], [0, 2, 200]]
    solution = Solution({"n": n, "flights": flights, "src": 0, "dst": 2, "k": 0})
    assert solution.find_cheapest_price() == 200
