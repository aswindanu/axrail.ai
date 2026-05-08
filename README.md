### Axrail Technical Test 
---

# Cheapest Flights Within K Stops

This project is a Python console application solution for the LeetCode problem:

[LeetCode - Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/?utm_source=chatgpt.com)

The application reads flight data from a JSON file and calculates the cheapest flight price based on:

* Source
* Destination
* Maximum number of stops

# Project Structure

```bash
.
|- main.py
|- data.json
|- src/
    - solution.py
|- tests/
    - smoke_test.py
    - negative_test.py
|- docker-compose.yml
|- Dockerfile
|- .gitignore
|- README.md
```

# Running the Application

### Run Locally

Make sure Python is installed.

```bash
python main.py
```

---

### Run with Docker

```bash
docker compose up -d
docker exec -it flight_dev sh
python main.py
```

# Available Input Modes

### Type 1 - JSON Calculation

Uses predefined flight data from `data.json`.

Example:

```bash
[1] Use data.json  [2] Custom input
> 1

Available flights:
0 -> 1 $100
1 -> 2 $100
2 -> 0 $100
1 -> 3 $600
2 -> 3 $200

Cheapest price from 0 to 3 with max 1 stop(s): 700

Best result : 700
```

The application will automatically process the JSON file and display the cheapest flight result.

### Type 2 - Custom Calculation

Allows user to manually input:

Example:

```bash
[1] Use data.json  [2] Custom input
> 2
Source: 2
Destination: 1
Max stops: 1

Available flights:
0 -> 1 $100
1 -> 2 $100
2 -> 0 $100
1 -> 3 $600
2 -> 3 $200

Cheapest price from 2 to 1 with max 1 stop(s): 200

Best result : 200
```

# Unit Testing

This project includes:

* Smoke Unit Test
* Negative Unit Test

Run tests using:

```bash
pytest
```

# Implementation Notes

* Class-based implementation
* JSON file input handling
* Input handling
* Docker Compose

---

# Author

Aswindanu Anwar
