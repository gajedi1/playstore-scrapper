from google_play_scraper import search, app
from datetime import datetime
import os

def save_to_file(filename, content):
    """Safely save content to a file"""
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(content + '\n')
        return True
    except Exception as e:
        print(f"Error saving to file: {e}")
        return False

def get_app_info(app_name):
    """Get app information from Google Play Store"""
    try:
        # Search for the app
        print(f"Searching for '{app_name}'...")
        results = search(app_name, lang='en', country='us')
        
        if not results:
            print("No results found.")
            return None
            
        # Get first result
        app_id = results[0]['appId']
        print(f"Found app ID: {app_id}")
        
        # Get app details
        details = app(app_id, lang='en', country='us')
        return details
        
    except Exception as e:
        print(f"Error getting app info: {e}")
        return None

def format_output(details, timestamp):
    """Format the output string"""
    if not details:
        return None
        
    # Format numbers safely
    def fmt_num(n):
        return f"{n:,}" if isinstance(n, (int, float)) else str(n or 'N/A')
        
    # Get values with defaults
    title = details.get('title', 'N/A')
    developer = details.get('developer', 'N/A')
    installs = details.get('installs', 'N/A')
    real_installs = fmt_num(details.get('realInstalls'))
    score = details.get('score', 'N/A')
    ratings = fmt_num(details.get('ratings'))
    
    # Create output string
    return f"""
{'='*50}
Timestamp: {timestamp}
App: {title}
Developer: {developer}
Installs: {installs}
Real Installs: {real_installs}
Score: {score} ({ratings} ratings)
{'='*50}
"""

def main():
    app_name = "Deerwalk Learning Center"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = 'app_install_log.txt'
    
    # Get app details
    details = get_app_info(app_name)
    
    if details:
        # Format and display output
        output = format_output(details, timestamp)
        if output:
            print(output.strip())
            
            # Save to file
            if save_to_file(log_file, output.strip()):
                print(f"\nData saved to '{log_file}'")
            else:
                print("\nCould not save to file")
    else:
        print("Failed to get app information")

if __name__ == "__main__":
    main()
