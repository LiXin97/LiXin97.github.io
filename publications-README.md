# Publications Management System

This system allows you to easily update your academic publications by editing a single JSON file, which will then automatically update your website.

## How It Works

1. All publication data is stored in `publications.json`
2. The JavaScript file `scripts/publications.js` loads this data and renders it to your webpage
3. When you update the JSON file, the changes will automatically appear on your site

## How to Update Your Publications

### 1. Edit the publications.json file

The `publications.json` file has the following structure:

```json
{
  "citations": {
    "count": "100+",
    "lastUpdated": "2024-10"
  },
  "publications": [
    {
      "title": "Publication Title",
      "authors": ["Author 1", "Xin Li", "Author 3"],
      "venue": "Conference or Journal Name",
      "year": "2025",
      "links": [
        {
          "type": "project",
          "url": "https://example.com/project",
          "icon": "fas fa-external-link-alt",
          "text": "Project"
        }
      ],
      "bibtex": "@inproceedings{key2025,\n  title={Publication Title},\n  author={Author1 and Li, Xin and Author3},\n  booktitle={Conference Name},\n  year={2025}\n}",
      "hidden": false,
      "equalContribution": false
    }
  ],
  "manuscripts": [
    {
      "title": "Manuscript Title",
      "authors": ["Xin Li", "Author 2"],
      "venue": "Under review",
      "year": "2024",
      "links": [],
      "bibtex": "@article{li2024manuscript,\n  title={Manuscript Title},\n  author={Li, Xin and Author2},\n  journal={arXiv preprint},\n  year={2024}\n}",
      "hidden": false
    }
  ]
}
```

### 2. Field Explanations

- `citations`: Information about your citation count
  - `count`: Your total citation count (e.g., "100+")
  - `lastUpdated`: When you last updated the citation count (e.g., "2024-10")

- `publications`: An array of your published papers
  - `title`: The full title of the paper
  - `authors`: Array of authors' names (your name will be automatically highlighted)
  - `venue`: Where the paper was published (conference/journal name)
  - `year`: Publication year
  - `links`: Array of links related to the paper (code, project page, PDF, etc.)
    - `type`: Type of link (project, code, pdf, etc.)
    - `url`: URL of the link
    - `icon`: Font Awesome icon class (e.g., "fas fa-external-link-alt")
    - `text`: Text to display for the link
  - `bibtex`: BibTeX citation for the paper (include newlines with \n)
  - `hidden`: Whether the publication should be hidden initially (shown when "View all" is clicked)
  - `equalContribution`: (Optional) Set to true if the publication has equal contribution authors

- `manuscripts`: Similar structure to publications, but for papers under review

### 3. Adding a New Publication

To add a new publication:

1. Open `publications.json`
2. Add a new object to either the `publications` or `manuscripts` array
3. Fill in all the required fields
4. Save the file
5. Your website will automatically update with the new publication

### 4. Updating Citation Count

To update your citation count:

1. Open `publications.json`
2. Update the `count` and `lastUpdated` fields in the `citations` object
3. Save the file

### 5. Hiding/Showing Publications

- Publications with `"hidden": true` will be hidden by default
- Visitors can click "View all publications" to see these hidden publications
- This is useful for keeping your page focused on your most important work while still listing everything

## Notes

- Your name is automatically highlighted in bold in the author list
- Equal contribution publications can be marked with the `equalContribution` flag
- The system handles BibTeX copying automatically
- The page maintains the same visual style as your original design

## Troubleshooting

If publications are not showing up:

1. Check that `publications.json` is valid JSON (use a JSON validator)
2. Ensure that `scripts/publications.js` is being loaded properly
3. Check the browser console for any JavaScript errors 