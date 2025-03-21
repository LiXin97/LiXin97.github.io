# Publications HTML Generator with Google Scholar Integration

This system automatically converts your publication data from JSON format into static HTML for your academic homepage, with the option to include Google Scholar citation statistics.

## Features

- Generates publication cards from a JSON data source
- Supports Google Scholar citation metrics integration
- Creates responsive HTML that works on all devices
- Handles BibTeX copying with visual feedback
- Organizes publications with toggle for "hidden" papers
- No JavaScript dependencies (works with JavaScript disabled)

## How It Works

1. **Data Management**:
   - `publications.json`: Contains your publication data
   - `gs_data.json`: Contains Google Scholar citation data (optional)

2. **HTML Generation**:
   - `generate_publications.py`: Reads the JSON files and generates HTML
   - Detects and uses Google Scholar data if available
   - Inserts the generated HTML into the `index.html` file

3. **Display**:
   - Publications appear as cards with links and BibTeX copying
   - Google Scholar citation metrics shown at the top (if available)
   - Hidden publications can be toggled with a button

## Usage

### Quick Start (Recommended)

Run the refresh script:

```bash
python refresh_and_view.py
```

This script will:
1. Download the latest Google Scholar data (if available)
2. Generate the HTML for your publications
3. Start a web server on port 8000
4. Open your browser to view the results

### Manual Process

1. **Update your data**:
   - Edit `publications.json` to update your publication information
   - Optionally place `gs_data.json` in the same directory for citation stats

2. **Generate HTML**:
   ```bash
   python generate_publications.py
   ```

3. **View the website**:
   ```bash
   python -m http.server 8000
   ```
   Then visit http://localhost:8000 in your browser

## Google Scholar Integration

### Adding Google Scholar Data

There are two ways to include Google Scholar citation metrics:

1. **Manual**: Place a `gs_data.json` file in the same directory
2. **Automatic**: The refresh script will download the latest data from your GitHub repository

### Expected Format

The `gs_data.json` file should contain at least these fields:
```json
{
  "scholar_id": "YOUR_SCHOLAR_ID",
  "citedby": 120,
  "hindex": 4,
  "i10index": 4,
  "updated": "2025-03-21"
}
```

## Requirements

- Python 3.6 or higher
- For the refresh script with auto-download: `requests` library

## Why Static HTML?

This approach has several advantages over a JavaScript-based solution:

1. **SEO**: Search engines can index your publications
2. **Performance**: Faster initial page load
3. **Reliability**: Works even with JavaScript disabled
4. **Simplicity**: No need for complex JavaScript frameworks

## Common Issues and Solutions

### Publications Not Displaying

- **Try hard refreshing**: Press Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)
- **Check file paths**: Ensure all files are in the correct directory
- **Validate JSON**: Make sure your JSON files are properly formatted

### Citation Data Not Showing

- **Check gs_data.json**: Ensure the file exists and has the correct format
- **Run with refresh script**: Use `python refresh_and_view.py` to auto-download the latest data
- **Check console errors**: Look for any JavaScript errors in the browser console

## Customization

You can customize the appearance by:

1. **Editing the HTML generation**: Modify the functions in `generate_publications.py`
2. **Adding CSS**: Update your stylesheet to style the publication cards and citation display

## Automation

For automatic updates, consider:

1. **Git hooks**: Update your website whenever you push changes to your repository
2. **GitHub Actions**: Set up a workflow to periodically fetch citation data
3. **Cron jobs**: Schedule regular updates on your server

## License

This project is open source and available under the MIT License. 