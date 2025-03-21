#!/usr/bin/env python3
"""
Publication Website Refresh and View Script

This script:
1. Checks for and downloads Google Scholar data if available
2. Generates the publications HTML from the JSON
3. Starts a web server
4. Provides instructions for hard refreshing the browser
"""

import os
import subprocess
import webbrowser
import time
import json
import sys
from datetime import datetime

# Get the root directory (parent of scripts directory)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(ROOT_DIR, 'data')

def print_with_border(message):
    """Print a message with a decorative border"""
    width = max(len(line) for line in message.split('\n')) + 4
    border = '=' * width
    print(f"\n{border}")
    for line in message.split('\n'):
        print(f"| {line.ljust(width - 4)} |")
    print(f"{border}\n")

def check_requirements():
    """Check if all required packages are installed"""
    try:
        import requests
        return True
    except ImportError:
        print("\n⚠️ The 'requests' package is required but not installed.")
        install = input("Install it now? (y/n): ")
        if install.lower() == 'y':
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
                return True
            except Exception as e:
                print(f"Failed to install 'requests': {e}")
                return False
        else:
            print("Cannot proceed without the 'requests' package.")
            return False

def download_scholar_data():
    """Try to download the latest Google Scholar data if available"""
    print("\n🔍 Checking for Google Scholar data...")
    try:
        # Ensure we're using the raw GitHub URL (not the blob URL)
        github_url = "https://raw.githubusercontent.com/LiXin97/LiXin97.github.io/google-scholar-stats/gs_data.json"
        
        print(f"📥 Downloading from: {github_url}")
        
        # Now import requests after we've checked for it
        import requests
        response = requests.get(github_url, timeout=15)
        
        if response.status_code == 200:
            content = response.text
            print(f"✅ Downloaded {len(content)} bytes of data")
            
            # Save the raw content first for debugging - update file paths
            raw_data_path = os.path.join(DATA_DIR, 'gs_data_raw.json')
            with open(raw_data_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            # Now try to parse it as JSON to validate
            try:
                json_data = json.loads(content)
                # If we get here, JSON is valid
                
                # Update file path for gs_data.json
                gs_data_path = os.path.join(DATA_DIR, 'gs_data.json')
                with open(gs_data_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                
                # Print some of the data to confirm it looks right
                print("🎓 Google Scholar data summary:")
                print(f"  - Name: {json_data.get('name', 'N/A')}")
                print(f"  - Citations: {json_data.get('citedby', 'N/A')}")
                print(f"  - h-index: {json_data.get('hindex', 'N/A')}")
                print(f"  - i10-index: {json_data.get('i10index', 'N/A')}")
                print(f"  - Updated: {json_data.get('updated', 'N/A').split(' ')[0]}")
                return True
            except json.JSONDecodeError as e:
                print(f"❌ Downloaded content is not valid JSON: {e}")
                print(f"First 100 characters of content: {content[:100]}...")
                return False
        else:
            print(f"❌ Could not download Google Scholar data: HTTP {response.status_code}")
            print(f"Response content: {response.text[:100]}...")
            return False
    except Exception as e:
        print(f"❌ Error downloading Google Scholar data: {e}")
        return False

print("\n🚀 Academic Homepage Refresh Tool")
print("-----------------------------------")

# Check if requirements are met
if not check_requirements():
    sys.exit(1)

# Try to download the latest Google Scholar data
download_scholar_data()

# Generate the publications HTML - update to use proper path
print("\n📝 Generating publications HTML...")
generate_script = os.path.join(SCRIPT_DIR, 'generate_publications.py')
os.system(f'python {generate_script}')

# Print instructions
instructions = f"""
🌐 WEBSITE IS READY!

1. Your page is running at: http://localhost:8000

2. If publications still don't display correctly:
   - Chrome/Edge: Press Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)
   - Firefox: Press Ctrl+F5 (Windows/Linux) or Cmd+Shift+R (Mac)
   - Safari: Hold Shift and click the reload button

3. To stop the server: Press Ctrl+C in this terminal window

Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

print_with_border(instructions)

# Open the browser after a short delay
time.sleep(1)
print("🌐 Opening browser at http://localhost:8000")
webbrowser.open('http://localhost:8000')

# Start the web server
try:
    print("🖥️ Starting web server on port 8000...")
    subprocess.run(['python', '-m', 'http.server', '8000'])
except KeyboardInterrupt:
    print("\n⏹️ Server stopped") 