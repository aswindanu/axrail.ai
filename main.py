import json
import sys
from src.solution import Solution

def load_json(path="data.json") -> dict:
    with open(path) as f:
        return json.load(f)

def add_input(label: str, type_data: str = "int") -> int:
    try:
        if type_data == "int":
            return int(input(f'{label}: ').strip())
        return input(f'{label}: ').strip()
    except ValueError:
        print(f"Please enter data as type '{type_data}'.")

def custom_input_user() -> dict:
    initial_data = load_json()
    n = initial_data.get("n")
    flights = initial_data.get("flights")

    # user input
    src = add_input("Source")
    dst = add_input("Destination")
    k = add_input("Max stops")
    return {
        "n": n, 
        "flights": flights, 
        "src": src, 
        "dst": dst, 
        "k": k
    }

def show_flights(flights: list) -> None:
    print("\nAvailable flights:")
    for src, dst, price in flights:
        print(f"{src} -> {dst} ${price}")

def show_result(**args: dict) -> dict | int:
    # show flight price
    show_flights(args["flights"])

    # find the best price here
    solution = Solution(args)
    result = solution.find_cheapest_price()
    answer = result if result != -1 else "No route found"

    # summarize the result
    if answer == -1:
        print(f'\nWrong input source / destination: {answer}\n')
    else:
        print(f'\nCheapest price from {args.get("src")} to {args.get("dst")} with max {args.get("k")} stop(s): {answer}\n')
    return answer

def main() -> None:
    print("Cheapest Flights Within K Stops\n")
    while True:
        mode = input("[1] Use data.json  [2] Custom input\n> ").strip()
        answer = None
        match mode:
            # 1. handle flight solution with sample from data.json
            case "1":
                answer = show_result(**load_json())
            # 2. handle flight solution with user input
            case "2":
                answer = show_result(**custom_input_user())
            case _:
                continue
        print(f'Best result : {answer}')

        # resubmit the data
        is_submit_again = input("Submit again? (Y/N): ").strip().upper()
        if is_submit_again != "Y":
            break

# Base APP
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
        sys.exit(0)
