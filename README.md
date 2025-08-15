# Google Play Store App Info Scrapers

This workspace contains two Python scripts for retrieving and displaying app information from the Google Play Store using the [`google_play_scraper`](https://github.com/JoMingyu/google-play-scraper) library.

## Files

- [`raw scraper.py`](raw%20scraper.py):  
  A basic script that searches for an app by name, fetches its details, and prints information such as installs, real installs, score, and ratings to the console.

- [`scraper_fixed.py`](scraper_fixed.py):  
  An improved version of [`raw scraper.py`](raw%20scraper.py) that adds error handling, output formatting, and saves the results to a log file (`app_install_log.txt`).

## Usage

### Prerequisites

- Python 3.x
- Install dependencies:
  ```sh
  pip install google-play-scraper pandas
  ```

### Running the Scripts

#### Raw Scraper

```sh
python "raw scraper.py"
```

- Prompts for the app name in the code (default: "Deerwalk Learning Center").
- Outputs app info to the console.

#### Scraper Fixed

```sh
python scraper_fixed.py
```

- Prompts for the app name in the code (default: "Deerwalk Learning Center").
- Outputs app info to the console and appends it to `app_install_log.txt`.

## Output Example

```
==================================================
Timestamp: 2025-08-15 14:15:45
App: Deerwalk Learning Center
Developer: Deerwalk
Installs: 100+
Real Installs: 272
Score: None (N/A ratings)
==================================================
```

## Customization

- To search for a different app, change the `app_name` variable in each script.

## License

This project is for educational and personal
