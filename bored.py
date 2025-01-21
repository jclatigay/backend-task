import requests
import json
import csv
import argparse
from typing import List, Dict

def fetch_activities(number: int) -> List[Dict]:
    url = "https://bored.api.lewagon.com/api/activity"
    activities = []
    
    try:
        for _ in range(number):
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                activities.append(data)
            else:
                raise Exception(f"API returned status code {response.status_code}")
                
        return activities
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Network error: {str(e)}")
    except json.JSONDecodeError as e:
        raise Exception(f"Invalid JSON response: {str(e)}")

def save_as_json(data: List[Dict], filename: str = "bored_activities.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")

def save_as_csv(data: List[Dict], filename: str = "bored_activities.csv"):
    if not data:
        return
    
    headers = data[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")

def print_to_console(data: List[Dict]):
    for item in data:
        print(json.dumps(item, indent=2))

def main():
    parser = argparse.ArgumentParser(
        description='A program to fetch random activities from the Bored API'
    )
    
    parser.add_argument(
        '-n',
        type=int,
        required=True,
        help='Number of activities you want to fetch (example: 5)'
    )
    parser.add_argument(
        '-f',
        choices=['json', 'csv', 'console'],
        required=True, 
        help='How do you want to see the results? Choose json (save to file), csv (save to file), or console (print to screen)'
    )
    
    args = parser.parse_args()
    
    try:
        print("Fetching activities from the API...")
        data = fetch_activities(args.n)
        
        print(f"Processing data in {args.f} format...")
        if args.f == 'json':
            save_as_json(data)
        elif args.f == 'csv':
            save_as_csv(data)
        else:
            print_to_console(data)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
