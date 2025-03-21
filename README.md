# Academic Homepage Publication Generator

This project generates and maintains a publications section for an academic homepage.

## Project Structure

```
academic-homepage/
│
├── data/                   # Data files
│   ├── publications.json   # Your publication data
│   └── gs_data.json        # Google Scholar citation metrics (auto-downloaded)
│
├── scripts/                # Python scripts
│   ├── generate_publications.py  # Main script to generate HTML
│   └── refresh_and_view.py       # Helper script to refresh and serve the page
│
└── index.html              # Your main HTML page
```

## How to Use

### Quick Start

1. Navigate to the `scripts` directory: 
   ```
   cd scripts
   ```

2. Run the refresh script:
   ```
   python refresh_and_view.py
   ```
   
   This will:
   - Download the latest Google Scholar data (if available)
   - Generate the HTML for your publications
   - Start a web server on port 8000
   - Open a browser to view your page

### Manual Process

1. Edit the publication data in `data/publications.json`

2. Run the generator script:
   ```
   cd scripts
   python generate_publications.py
   ```

3. View your website:
   ```
   python -m http.server 8000
   ```
   
   Then open http://localhost:8000 in your browser

## Features

- Automatically formats publication entries from JSON data
- Integrates Google Scholar citation metrics
- Separate section for citations and publications
- BibTeX copying functionality
- Mobile-responsive design
- Dark mode support

## Customization

You can customize the HTML generation by editing the `generate_publications.py` script. 
The script uses inline styles for maximum compatibility, but you can modify it to use CSS classes. 