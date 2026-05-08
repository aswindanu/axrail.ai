import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from src.solution import Solution

def test_no_route_exists():
    n = 3
    flights = [[0, 1, 100]]
    solution = Solution({"n": n, "flights": flights, "src": 0, "dst": 2, "k": 1})
    assert solution.find_cheapest_price() == -1

def test_route_exists_but_k_too_small():
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100]]
    solution = Solution({"n": n, "flights": flights, "src": 0, "dst": 3, "k": 1})
    assert solution.find_cheapest_price() == -1

def test_k_zero_no_direct_flight():
    n = 3
    flights = [[0, 1, 50], [1, 2, 50]]
    solution = Solution({"n": n, "flights": flights, "src": 0, "dst": 2, "k": 0})
    assert solution.find_cheapest_price() == -1

def test_no_flight_at_all():
    n = 0
    flights = []
    solution = Solution({"n": n, "flights": flights, "src": 0, "dst": 2, "k": 0})
    assert solution.find_cheapest_price() == -1

def test_no_source_available():
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100]]
    solution = Solution({"n": n, "flights": flights, "src": 4, "dst": 2, "k": 0})
    assert solution.find_cheapest_price() == -1

def test_no_destination_available():
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100]]
    solution = Solution({"n": n, "flights": flights, "src": 2, "dst": 5, "k": 0})
    assert solution.find_cheapest_price() == -1

def test_not_enough_transit():
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [3, 4, 100], [4, 0, 100]]
    solution = Solution({"n": n, "flights": flights, "src": 4, "dst": 3, "k": 1})
    assert solution.find_cheapest_price() == -1
