from google_play_scraper import search, app
import pandas as pd

def get_app_downloads(app_name):
    try:
        print(f"Searching for '{app_name}' on Google Play Store...")
        result = search(
            app_name,
            lang='en',
            country='us'
        )
        
        if not result:
            print("No results found for the app.")
            return
            
        app_id = result[0]['appId']
        print(f"Found app with ID: {app_id}")
        
        app_details = app(
            app_id,
            lang='en',
            country='us'
        )
        
        installs = app_details.get('installs', 'Not available')
        real_installs = app_details.get('realInstalls', None)
        
        print(f"\nApp Name: {app_details.get('title', 'N/A')}")
        print(f"Developer: {app_details.get('developer', 'N/A')}")
        print(f"Installs: {installs}")
        if real_installs is not None:
            print(f"Real Installs: {real_installs:,}")
        
        score = app_details.get('score', 'N/A')
        ratings = app_details.get('ratings', 0)
        if ratings is None:
            ratings = 0
        print(f"Score: {score} ({ratings:,} ratings)")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app_name = "Deerwalk Learning Center"
    get_app_downloads(app_name)
