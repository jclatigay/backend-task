# Backend-Task

A command-line utility that fetches random activities from the Bored API.

## Setup

### Requirements
- Python 3.6+
- `requests` library (`pip install requests`)

### Installation```
git clone https://github.com/jclatigay/backend-task.git
cd backend-task
```

## Usage

```
python bored.py -n [number] -f [format]
```

Parameters:
- `-n`: Number of activities to fetch
- `-f`: Output format (`json`, `csv`, or `console`)

Examples (use one at a time):
```
python bored.py -n 10 -f json    # Creates activities.json
python bored.py -n 5 -f csv      # Creates activities.csv
python bored.py -n 15 -f console  # Displays in terminal
```

## Note
This utility uses the Bored API endpoint at `https://bored.api.lewagon.com/api/activity` as the original endpoint was not accessible.
