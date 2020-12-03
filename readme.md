# PC Component Tracker
Created and maintained by [theGingerbreadMan](https://github.com/aidan-gbm). Displays live updates for selected items for sale on [Newegg](https://www.newegg.com/).

## Usage
Pre-requisite: [Python 3](https://www.python.org/downloads/)

1. Clone this repository
2. Install the requirements with `pip install -r requirements.txt`
3. Set your desired PC components in [tracker.py](tracker.py)
4. Run the application with `python app.py`
5. Browse to http://localhost:8050

## TODO

- Implement Config File
    - Configurable refresh interval
    - Add/remove components from the browser
- Add notification when price drops
- Add direct link to item page on Newegg