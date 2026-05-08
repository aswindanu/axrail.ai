import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from ..main import load_json
from code.solution import Solution

solution = Solution(load_json())

def test_no_route_exists():
    n = 3
    flights = [[0, 1, 100]]
    solution(n, flights, src=0, dst=2, k=1)
    assert solution.find_cheapest_price() == -1

def test_route_exists_but_k_too_small():
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100]]
    solution(n, flights, src=0, dst=3, k=1)
    assert solution.find_cheapest_price() == -1

def test_k_zero_no_direct_flight():
    n = 3
    flights = [[0, 1, 50], [1, 2, 50]]
    solution(n, flights, src=0, dst=2, k=0)
    assert solution.find_cheapest_price() == -1
