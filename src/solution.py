from typing import List


class Solution:
    def __init__(self, data):
        self.cities: int = data["n"]
        self.flights: List[List[int]] = data["flights"]
        self.source: int = data["src"]
        self.destination: int = data["dst"]
        self.stops: int = data["k"]

    def list_available_flight(self) -> list:
        """
        Grouping list of available flights that
        user can purchase e.g.
        return:
            [
                [(1, 500)], # 1 flight dest with total 500
                [(2, 200), (1, 200)], # 2 flights dest with total 400
                ...
            ]
        """
        available_flights = []

        # Journey city filter
        # - current_city  : the city of current user
        # - stops_used    : transit count that used during flight
        # - journey       : list of cities that user get transit
        # - cities_visited: set of cities that has been visited
        queue = [{
            "current_city": self.source,
            "stops_used": 0,
            "journey": [],
            "cities_visited": {self.source},
        }]
        while queue:
            state = queue.pop(0)
            current_city = state["current_city"]
            stops_used = state["stops_used"]
            journey = state["journey"]
            cities_visited = state["cities_visited"]

            # if the destination is reached, the journey will be added to available_flights
            if current_city == self.destination:
                available_flights.append(journey)
                continue
            # if exceeded max stops we need to break it
            if stops_used > self.stops:
                continue
            # Try getting every possible flight journey from the current city
            for src, dst, price in self.flights:
                is_current_city = src == current_city
                dest_already_visited = dst in cities_visited
                # if the dst never been there (1st time visit), 
                # we consider it to add to queue as transit
                if is_current_city and not dest_already_visited:
                    cities_visited.add(dst)
                    queue.append({
                        "current_city": dst,
                        "stops_used": stops_used + 1,
                        "journey": journey + [(dst, price)], # add new journey here
                        "cities_visited": set(cities_visited),
                    })
        return available_flights

    def find_cheapest_price(self) -> int:
        """
        This will try to define each stop of the flight
        and find the cheapest flight together with
        considering the transit request (k).

        This is handled by getting the best deal based on list of
        available flights that user can purchase e.g.
        [
            [(1, 500)], # 1 flight dest with total 500
            [(2, 200), (1, 200)], # 2 flights dest with total 400 (this func will return 400 as the best deal)
        ]

        return:
            integer e.g 400 OR -1 (if didn't find any relevant flight)
        """
        # get all relevant flight to destination
        available = self.list_available_flight()
        if not available:
            return -1

        # find the best deal -> [index, total_price]
        cheapest_price = [None, None]
        for idx, avail in enumerate(available):
            total = sum(price for _, price in avail)
            set_price = False
            if not cheapest_price[-1]:
                set_price = True
            else:
                if cheapest_price[-1] > total:
                    set_price = True
            if set_price:
                cheapest_price = [idx, total]

        return cheapest_price[-1] or -1
