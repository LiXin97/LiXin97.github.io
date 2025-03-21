#!/usr/bin/env python3
"""
Publications HTML Generator

This script generates HTML for publications from a JSON file and updates the index.html file.
Run this script whenever you update publications.json to automatically update your website.
It can also import citation data from Google Scholar stats (gs_data.json).
"""

import json
import os
import re
from datetime import datetime


def load_json(file_path):
    """Load and parse the publications JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None


def format_authors(authors):
    """Format the authors list, highlighting the name 'Xin Li'"""
    formatted = []
    for author in authors:
        if "Xin Li" in author:
            formatted.append(f"<strong>{author}</strong>")
        else:
            formatted.append(author)
    return ", ".join(formatted)


def generate_publication_card(pub):
    is_hidden = pub.get('hidden', False)
    """Generate HTML for a single publication card"""
    hidden_class = "hidden-publication" if is_hidden else ""
    equal_contribution = pub.get('equalContribution', False)
    equal_contribution_text = ' <span class="text-secondary">(*equal contribution)</span>' if equal_contribution else ''

    citations = pub.get('num_citations', 0)

    # Format links
    links_html = ""
    if pub.get('links') and len(pub['links']) > 0:
        links = []
        for link in pub['links']:
            links.append(f"""<a href="{link['url']}" class="pub-link" target="_blank" rel="noopener noreferrer">
                <i class="{link['icon']}"></i> {link['text']}
            </a>""")

        # Add BibTeX button
        links.append(f"""<button class="pub-link bibtex-btn">
                <i class="fas fa-quote-right"></i> BibTeX
            </button>""")
        links_html = "\n".join(links)
    else:
        # Only BibTeX button
        links_html = f"""<button class="pub-link bibtex-btn">
                <i class="fas fa-quote-right"></i> BibTeX
            </button>"""
    
    if citations > 0:
        links_html += f"""<button class="pub-link citation-btn">
                Citations {citations}
            </button>"""

    # Generate HTML for the publication card - fixing indentation and whitespace
    html = f"""<div class="card {hidden_class}">
            <h3>{pub['title']}</h3>
            <p>{format_authors(pub['authors'])}{equal_contribution_text}</p>
            <p><em>{pub['venue']}</em>, {pub['year']}</p>
            <div class="pub-links">
                {links_html}
            </div>
            <pre class="bibtex-content">{pub['bibtex']}<button class="copy-bibtex-btn" aria-label="Copy BibTeX"><i class="fas fa-copy"></i></button></pre>
          </div>"""
    return html


def load_scholar_data():
    """Load Google Scholar statistics data if available"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Update path to point to data directory
    scholar_file = os.path.join(os.path.dirname(script_dir), 'data', 'gs_data.json')
    
    if os.path.exists(scholar_file):
        try:
            with open(scholar_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading Google Scholar data: {e}")
    return None


def generate_scholar_stats_html(scholar_data):
    """Generate HTML for Google Scholar statistics"""
    if not scholar_data:
        print("No Google Scholar data available")
        return ""
    
    try:
        print("Generating Google Scholar HTML...")
        
        # Print the keys to help with debugging
        print(f"Available keys in scholar_data: {list(scholar_data.keys())}")
        
        # FIXED: Extract correct citation metrics fields
        citations = scholar_data.get('citation_metrics', {}).get('citations', 0)
        h_index = scholar_data.get('citation_metrics', {}).get('h-index', 0)  # Correct field from GitHub JSON
        i10_index = scholar_data.get('citation_metrics', {}).get('i10-index', 0)  # Correct field from GitHub JSON
        
        # Log for debugging
        print(f"Citation values found: citations={citations}, h-index={h_index}, i10-index={i10_index}")
        
        # Format yearly citations data if available
        yearly_citations = {}
        if 'cites_per_year' in scholar_data and isinstance(scholar_data['cites_per_year'], dict):
            yearly_citations = scholar_data['cites_per_year']
            print(f"Found yearly citations data: {yearly_citations}")
        
        # Get the scholar ID and updated date
        scholar_id = scholar_data.get('scholar_id', '')
        updated = "unknown"
        if 'updated' in scholar_data and scholar_data['updated']:
            updated_parts = str(scholar_data['updated']).split(' ')
            if updated_parts:
                updated = updated_parts[0]
        
        # Create the citation stats HTML with inline styles to ensure proper display
        citation_html = f"""
        <div class="citation-info" style="margin-bottom: 2rem; padding: 1.25rem; background-color: var(--background-alt); border-radius: 0.5rem; box-shadow: var(--shadow); display: block; width: 100%;">
            <div style="display: flex; flex-wrap: wrap; gap: 1.5rem; margin-bottom: 1rem;">
                <div style="flex: 1;">
                    <h3 style="margin-top: 0; margin-bottom: 0.5rem; font-size: 1.25rem; color: var(--text-primary);">Citation Metrics</h3>
                    <div style="display: flex; flex-wrap: wrap; gap: 1.5rem;">
                        <div style="text-align: center; min-width: 80px;">
                            <div style="font-size: 2rem; font-weight: 700; color: var(--primary); line-height: 1.2;">{citations}</div>
                            <div style="font-size: 0.9rem; color: var(--text-secondary);">Citations</div>
                        </div>
                        <div style="text-align: center; min-width: 80px;">
                            <div style="font-size: 2rem; font-weight: 700; color: var(--primary); line-height: 1.2;">{h_index}</div>
                            <div style="font-size: 0.9rem; color: var(--text-secondary);">h-index</div>
                        </div>
                        <div style="text-align: center; min-width: 80px;">
                            <div style="font-size: 2rem; font-weight: 700; color: var(--primary); line-height: 1.2;">{i10_index}</div>
                            <div style="font-size: 0.9rem; color: var(--text-secondary);">i10-index</div>
                        </div>
                    </div>
                </div>
            </div>
            <div style="font-size: 0.875rem; text-align: right; color: var(--text-secondary);">
                Data from <a href="https://scholar.google.com/citations?user={scholar_id}" target="_blank" rel="noopener" style="color: var(--primary);">Google Scholar</a>
                <span style="margin-left: 0.5rem;">(Updated: {updated})</span>
            </div>
        </div>
        """
        print("Successfully generated Google Scholar HTML")
        return citation_html
    except Exception as e:
        print(f"Error generating Scholar HTML: {e}")
        import traceback
        traceback.print_exc()
        return ""


def generate_scholarly_article_json_ld(publications):
    """Generate JSON-LD structured data for publications using ScholarlyArticle schema"""
    scholarly_articles = []
    
    for pub in publications:
        # Create author list in schema.org format
        authors = []
        for author in pub.get('authors', []):
            authors.append({
                "@type": "Person",
                "name": author
            })
        
        # Construct the ScholarlyArticle object
        article = {
            "@type": "ScholarlyArticle",
            "headline": pub.get('title', ''),
            "author": authors,
            "datePublished": str(pub.get('year', '')),
            "name": pub.get('title', ''),
            "publisher": {
                "@type": "Organization",
                "name": pub.get('venue', '')
            }
        }
        
        # Add URL if available
        if pub.get('links'):
            for link in pub.get('links', []):
                if link.get('text') == 'Paper' or link.get('text') == 'PDF':
                    article["url"] = link.get('url')
                    break
                elif link.get('text') == 'Project Homepage':
                    article["url"] = link.get('url')
                    break
        
        # Add DOI if available
        if pub.get('doi'):
            article["identifier"] = f"https://doi.org/{pub.get('doi')}"
        
        scholarly_articles.append(article)
    
    # Create the full JSON-LD object
    json_ld = {
        "@context": "https://schema.org",
        "@graph": scholarly_articles
    }
    
    return json.dumps(json_ld, indent=2)


def generate_publications_html(data):
    citations = data.get("citation_metrics", {}).get("citations", 0)
    h_index = data.get("citation_metrics", {}).get("h-index", 0)
    i10_index = data.get("citation_metrics", {}).get("i10-index", 0)

    last_updated = data.get("citation_metrics", {}).get("last_updated", datetime.now().strftime("%Y-%m-%d"))


    # Generate JSON-LD for ScholarlyArticle structured data
    publications = data.get("publications", [])
    scholarly_article_json_ld = generate_scholarly_article_json_ld(publications)

    """Generate HTML for publications section."""
    publications_html = f"""
    <script type="application/ld+json">
    {scholarly_article_json_ld}
    </script>
    
    <div class="publications-header">
        <h2 class="section-title">Selected Publications</h2>
    </div>
    
    <div class="citation-info" style="margin-bottom: 2rem; padding: 1.25rem; background-color: var(--background-alt); border-radius: 0.5rem; box-shadow: var(--shadow); display: block; width: 100%;">
        <div style="display: flex; flex-wrap: wrap; gap: 1.5rem; margin-bottom: 1rem;">
            <div style="flex: 1;">
                <h3 style="margin-top: 0; margin-bottom: 0.5rem; font-size: 1.25rem; color: var(--text-primary);">Citation Metrics</h3>
                <div style="display: flex; flex-wrap: wrap; gap: 1.5rem;">
                    <div style="text-align: center; min-width: 80px;">
                        <div style="font-size: 2rem; font-weight: 700; color: var(--primary); line-height: 1.2;">{citations}</div>
                        <div style="font-size: 0.9rem; color: var(--text-secondary);">Citations</div>
                    </div>
                    <div style="text-align: center; min-width: 80px;">
                        <div style="font-size: 2rem; font-weight: 700; color: var(--primary); line-height: 1.2;">{h_index}</div>
                        <div style="font-size: 0.9rem; color: var(--text-secondary);">h-index</div>
                    </div>
                    <div style="text-align: center; min-width: 80px;">
                        <div style="font-size: 2rem; font-weight: 700; color: var(--primary); line-height: 1.2;">{i10_index}</div>
                        <div style="font-size: 0.9rem; color: var(--text-secondary);">i10-index</div>
                    </div>
                </div>
            </div>
        </div>
        
        <div style="font-size: 0.875rem; text-align: right; color: var(--text-secondary); margin-top: 1rem;">
            Data from <a href="https://scholar.google.com/citations?user=Hxf8sNkAAAAJ" target="_blank" rel="noopener" style="color: var(--primary);">Google Scholar</a>
            <span style="margin-left: 0.5rem;">(Updated: {last_updated})</span>
        </div>
    </div>
    
    <style>
    /* BibTeX copy button styling */
    .bibtex-content {{
      position: relative;
      padding: 1rem;
      background-color: #f8f9fa;
      border-radius: 4px;
      font-family: monospace;
      font-size: 0.85rem;
      overflow-x: auto;
      white-space: pre-wrap;
      margin-top: 0.5rem;
    }}
    
    .copy-bibtex-btn {{
      position: absolute;
      top: 0.5rem;
      right: 0.5rem;
      background-color: rgba(255, 255, 255, 0.8);
      border: 1px solid #dee2e6;
      border-radius: 4px;
      padding: 0.25rem 0.5rem;
      cursor: pointer;
      transition: all 0.2s ease;
      font-size: 0.8rem;
    }}
    
    .copy-bibtex-btn:hover {{
      background-color: var(--primary-light);
      color: white;
    }}
    
    .copy-bibtex-btn.copied {{
      background-color: #28a745;
      color: white;
    }}
    </style>

    <div class="publications-list">
    """
    
    # Generate HTML for each publication
    for publication in data.get("publications", []):
        publications_html += generate_publication_card(publication)
    
    # Add closing div for publications-list
    publications_html += """
    </div>
    
    <div class="publications-buttons" style="display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1.5rem;">
      <button id="pub-toggle-btn" class="view-all-button"
        style="display: inline-block; padding: 0.5rem 1rem; background-color: var(--primary); color: white; border-radius: 0.375rem; font-weight: 500; border: none; cursor: pointer;"
        onclick="window.location.href='/pubs.html'; return false;">View all publications</button>
    </div>

    <script>
      function togglePublications() {
        var hiddenPubs = document.querySelectorAll('.hidden-publication');
        var toggleBtn = document.getElementById('pub-toggle-btn');
        
        // Check if publications are currently hidden
        if (hiddenPubs[0].style.display === 'none' || hiddenPubs[0].style.display === '') {
          // Show all publications
          for (var i = 0; i < hiddenPubs.length; i++) {
            hiddenPubs[i].style.display = 'block';
          }
          toggleBtn.textContent = 'Show fewer publications';
        } else {
          // Hide publications
          for (var i = 0; i < hiddenPubs.length; i++) {
            hiddenPubs[i].style.display = 'none';
          }
          toggleBtn.textContent = 'View all publications';
        }
        
        return false;
      }
      
      // Hide publications marked as hidden on page load
      document.addEventListener('DOMContentLoaded', function() {
        var hiddenPubs = document.querySelectorAll('.hidden-publication');
        for (var i = 0; i < hiddenPubs.length; i++) {
          hiddenPubs[i].style.display = 'none';
        }
        
        // Ensure the button shows the correct text
        document.getElementById('pub-toggle-btn').textContent = 'View all publications';
        
        // BibTeX buttons functionality
        const bibtexButtons = document.querySelectorAll('.bibtex-btn');
        
        bibtexButtons.forEach(btn => {
            btn.addEventListener('click', function() {
                // Find the closest parent card
                const card = this.closest('.card');
                
                // Find the bibtex content within this card
                const bibtexContent = card.querySelector('.bibtex-content');
                
                // Toggle visibility with !important override
                if (bibtexContent.style.display === 'block') {
                    bibtexContent.style.display = 'none';
                } else {
                    // Force display block with !important by using inline style setAttribute
                    bibtexContent.setAttribute('style', 'display: block !important');
                }
            });
        });
        
        // BibTeX copy buttons functionality
        const copyBibtexButtons = document.querySelectorAll('.copy-bibtex-btn');
        
        copyBibtexButtons.forEach(btn => {
            btn.addEventListener('click', function(e) {
                // Prevent the click from bubbling up and toggling the display
                e.stopPropagation();
                
                // Get the bibtex content (parent element's text content without the button text)
                const bibtexElement = this.parentElement;
                const bibtexText = bibtexElement.textContent.trim();
                
                // Copy to clipboard
                navigator.clipboard.writeText(bibtexText).then(() => {
                    // Visual feedback
                    this.classList.add('copied');
                    const originalIcon = this.innerHTML;
                    this.innerHTML = '<i class="fas fa-check"></i>';
                    
                    // Reset after 2 seconds
                    setTimeout(() => {
                        this.classList.remove('copied');
                        this.innerHTML = originalIcon;
                    }, 2000);
                }).catch(err => {
                    console.error('Could not copy text: ', err);
                });
            });
        });
      });
    </script>
    """
    
    return publications_html, last_updated


def generate_publications_filters_js():
    """Generate JavaScript for publication filters."""
    js_code = """
<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Publication filters
    const filterButtons = document.querySelectorAll('.filter-btn');
    
    filterButtons.forEach(btn => {
      btn.addEventListener('click', function() {
        // Remove active class from all buttons
        filterButtons.forEach(b => b.classList.remove('active'));
        
        // Add active class to clicked button
        this.classList.add('active');
        
        // Get filter value
        const filter = this.getAttribute('data-filter');
        
        // Apply filtering logic
        const publicationCards = document.querySelectorAll('.publications-list .card');
        
        publicationCards.forEach(card => {
          if (filter === 'all') {
            card.style.display = '';
            card.style.opacity = '1';
          } else if (filter === 'first-author') {
            const authorText = card.querySelector('p')?.textContent || '';
            
            if (authorText.indexOf('Xin Li') === 0 || authorText.indexOf('<strong>Xin Li</strong>') === 0) {
              card.style.display = '';
              card.style.opacity = '1';
            } else {
              card.style.opacity = '0.5';
            }
          } else if (filter === 'recent') {
            const yearText = card.querySelector('p:nth-child(3)')?.textContent || '';
            const yearMatch = yearText.match(/\d{4}/);
            const year = yearMatch ? parseInt(yearMatch[0]) : 0;
            
            if (year >= 2023) {
              card.style.display = '';
              card.style.opacity = '1';
            } else {
              card.style.opacity = '0.5';
            }
          }
        });
      });
    });
  });
</script>
"""
    return js_code


def update_html_file(input_file, publications_html, last_updated, output_file=None):
    """Update HTML file with publications section."""
    if output_file is None:
        output_file = input_file
        
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find and replace last updated date
    # <span style="margin-left: 0.5rem;">(Last updated: 2025-03-19)</span>
    # Find this line and replace the date with the new last_updated date
    updated_last_updated_date = f'<span style="margin-left: 0.5rem;">(Last updated: {last_updated})</span>'
    content = re.sub(
        r'<span style="margin-left: 0.5rem;">\(Last updated: \d{4}-\d{2}-\d{2}\)</span>',
        updated_last_updated_date,
        content,
        flags=re.DOTALL
    )
    
    # print update success
    print(f"Updated last updated date to {last_updated}")
    
    # Find and replace publications section
    publications_pattern = r'<section id="publications" class="section">.*?</section>'
    
    # Escape the backlashes in the publications_html to avoid regex issues
    escaped_publications_html = publications_html.replace('\\', '\\\\')
    
    updated_content = re.sub(
        publications_pattern, 
        f'<section id="publications" class="section">{escaped_publications_html}</section>', 
        content, 
        flags=re.DOTALL
    )
    
    # Add the filters JavaScript if it doesn't exist
    filters_js = generate_publications_filters_js()
    if '<script>document.addEventListener(\'DOMContentLoaded\', function() {' not in updated_content:
        # Add before the closing body tag
        updated_content = updated_content.replace('</body>', f'{filters_js}\n</body>')
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"Updated HTML file at {output_file}")


def generate_standalone_publications_page(data):
    """Generate a standalone HTML page with all publications"""
    citations = data.get("citation_metrics", {}).get("citations", 0)
    h_index = data.get("citation_metrics", {}).get("h-index", 0)
    i10_index = data.get("citation_metrics", {}).get("i10-index", 0)
    last_updated = data.get("citation_metrics", {}).get("last_updated", datetime.now().strftime("%Y-%m-%d"))

    # Generate JSON-LD for ScholarlyArticle structured data
    publications = data.get("publications", [])
    scholarly_article_json_ld = generate_scholarly_article_json_ld(publications)

    # Create the complete HTML documentf"""
    scholarly_article_json_ld = f"""
    <script type="application/ld+json">
    {scholarly_article_json_ld}
    </script>
    """
    html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
  <title>Xin Li - Publications</title>

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="/images/icon.png">

  <!-- CSS -->
  <link rel="stylesheet" href="/styles/academic-profile.css">

  <!-- Google Fonts -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
  
  <!-- Font Awesome for icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <!-- Meta tags for SEO -->
  <meta name="description" content="Publications by Xin Li, PhD Student at Nanyang Technological University (NTU), Singapore.">
  <meta name="keywords" content="Xin Li, Publications, Research, NTU, SLAM, Embodied AI, LLMs, Wireless Communications">

  <style>
    /* Additional custom styles for visual enhancement */
    .hero {
      position: relative;
      overflow: hidden;
      border-radius: 12px;
      box-shadow: 0 8px 20px rgba(0, 50, 150, 0.08);
      background-color: #ffffff;
    }

    .hero::before {
      content: none;
      /* Remove the patterned background */
    }

    .hero>* {
      position: relative;
      z-index: 1;
    }
    
    /* Header styling with margin */
    header {
      margin-bottom: 2.5rem;
      padding: 1.5rem 0;
      border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .header-content {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
    }
    
    .logo {
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--primary);
      text-decoration: none;
      transition: all 0.3s ease;
    }
    
    .logo:hover {
      color: var(--primary-dark);
    }
    
    nav {
      display: flex;
      gap: 1.25rem;
      flex-wrap: wrap;
    }
    
    /* Mobile menu button */
    .mobile-menu-button {
      display: none;
      background: none;
      border: none;
      font-size: 1.5rem;
      color: var(--primary);
      cursor: pointer;
      padding: 0.5rem;
    }
    
    @media (max-width: 768px) {
      .mobile-menu-button {
        display: block;
      }
      
      nav {
        display: none;
        width: 100%;
        flex-direction: column;
        margin-top: 1rem;
        gap: 0.5rem;
      }
      
      nav.active {
        display: flex;
      }
      
      .header-content {
        flex-direction: row;
        flex-wrap: wrap;
      }
      
      .nav-link {
        padding: 0.75rem !important;
        border-bottom: 1px solid var(--border-color);
      }
      
      .publications-header {
        flex-direction: column;
        align-items: flex-start;
      }
      
      .publications-list {
        grid-template-columns: 1fr !important;
      }
      
      .filter-btn {
        padding: 0.75rem 1rem;
      }
    }
    
    .nav-link {
      position: relative;
      color: var(--text-primary);
      text-decoration: none;
      font-weight: 500;
      padding: 0.5rem 0;
      transition: all 0.3s ease;
    }
    
    .nav-link:hover {
      color: var(--primary);
    }
    
    .nav-link::after {
      content: '';
      position: absolute;
      width: 0;
      height: 2px;
      bottom: 0;
      left: 0;
      background-color: var(--primary);
      transition: width 0.3s ease;
    }
    
    .nav-link:hover::after {
      width: 100%;
    }

    .section {
      position: relative;
      border-radius: 12px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
      background-color: #ffffff;
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .section:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
    }

    .section-title {
      position: relative;
      margin-bottom: 2rem;
      padding-bottom: 0.5rem;
      color: var(--primary-dark);
    }

    .section-title::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 80px;
      height: 3px;
      background: linear-gradient(90deg, var(--primary) 0%, var(--primary-light) 100%);
      border-radius: 3px;
    }

    /* Enhance cards */
    .card {
      border: none;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
      transition: all 0.3s ease;
      overflow: hidden;
      background: #ffffff;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
    }

    .card:hover {
      box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
    }

    /* Publication buttons enhancement */
    .pub-link {
      transition: all 0.3s ease;
      padding: 0.5rem 0.75rem !important;
      margin: 0.25rem !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 0.5rem !important;
      font-size: 0.9rem !important;
      border-radius: 4px !important;
      cursor: pointer !important;
      background-color: var(--background-alt) !important;
      color: var(--text-primary) !important;
      text-decoration: none !important;
      border: none !important;
    }

    .pub-link:hover {
      transform: translateY(-3px);
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      background-color: var(--primary-light) !important;
      color: white !important;
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
      width: 8px;
    }

    ::-webkit-scrollbar-track {
      background: #f1f1f1;
    }

    ::-webkit-scrollbar-thumb {
      background: var(--primary-light);
      border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
      background: var(--primary);
    }

    /* Education items enhancement */
    .education-item {
      border-left: 3px solid var(--primary);
      padding-left: 1.5rem;
      position: relative;
    }

    .education-item::before {
      content: '';
      position: absolute;
      left: -6px;
      top: 0;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background-color: var(--primary);
    }

    /* Social links enhancement */
    .social-links {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
    }

    .social-link {
      padding: 0.75rem 1rem;
      border-radius: 8px;
      transition: all 0.3s ease;
      background-color: rgba(240, 245, 255, 0.7);
    }

    .social-link:hover {
      background-color: var(--primary);
      color: white;
      transform: translateY(-3px);
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    /* Research interests enhancement */
    .interests-container {
      gap: 2rem;
    }

    .interest-item {
      border-radius: 10px;
      transition: all 0.3s ease;
      background: #ffffff;
      box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);
    }

    .interest-item:hover .interest-icon {
      transform: translateY(-10px);
      color: var(--accent);
    }

    .interest-icon {
      font-size: 2.5rem;
      transition: all 0.3s ease;
      margin-bottom: 1.5rem;
    }

    /* News section enhancement */
    .news-list::before {
      background: linear-gradient(to bottom, var(--primary-light), var(--primary-dark));
    }

    .news-list li::before {
      box-shadow: 0 0 0 4px rgba(30, 64, 175, 0.2);
    }

    /* Footer enhancement */
    footer {
      background: #ffffff;
      border-top: 1px solid rgba(0, 0, 0, 0.05);
      padding: 3rem 0 2rem;
      text-align: center;
      color: var(--text-secondary);
    }

    /* Page background enhancement */
    body {
      background: #ffffff;
      position: relative;
    }

    body::before {
      content: none;
      /* Remove the patterned background */
    }

    .container {
      max-width: 1100px;
      padding: 2rem 1.5rem; /* Increased top/bottom padding */
      margin: 0 auto;
    }

    @media (min-width: 768px) {
      .hero {
        flex-direction: row;
        align-items: center;
        gap: 4rem;
      }

      .profile-image-container {
        margin: 0;
      }
      
      .publications-list {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(450px, 1fr));
        gap: 1.5rem;
      }
    }
    
    /* Mobile optimizations */
    @media (max-width: 600px) {
      .container {
        padding: 1rem;
      }
      
      .card {
        padding: 1rem;
      }
      
      .card h3 {
        font-size: 1.1rem;
      }
      
      .pub-links {
        flex-wrap: wrap;
      }
      
      .citation-info {
        padding: 1rem !important;
      }
      
      .page-title {
        font-size: 1.5rem !important;
      }
      
      .section-title {
        font-size: 1.3rem;
      }
    }

    /* Citation data enhancements */

    /* Add transition for smoother appearance */
    .section,
    .card {
      animation: fadeIn 0.8s ease-out forwards;
    }

    @keyframes fadeIn {
      from {
        opacity: 0;
        transform: translateY(20px);
      }

      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    /* Publications section header enhancement */
    .publications-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;
      flex-wrap: wrap;
      gap: 1rem;
    }
    
    .page-title {
      margin-bottom: 2rem;
      font-size: 2rem;
      color: var(--primary-dark);
      text-align: center;
    }

    .publication-filters {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .filter-btn {
      padding: 0.5rem 1rem;
      border: 1px solid var(--border-color);
      border-radius: 4px;
      background: white;
      font-size: 0.9rem;
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .filter-btn:hover,
    .filter-btn.active {
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }

    .profile-image-container {
      flex-shrink: 0;
      width: 250px;
      height: 250px;
      border-radius: 50%;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      margin: 0 auto;
      border: 4px solid var(--primary-light);
      transition: var(--transition-standard);
      position: relative;
    }

    /* BibTeX copy button styling */
    .bibtex-content {
      position: relative;
      padding: 1rem;
      background-color: #f8f9fa;
      border-radius: 4px;
      font-family: monospace;
      font-size: 0.85rem;
      overflow-x: auto;
      white-space: pre-wrap;
      margin-top: 0.5rem;
      display: none;
    }
    
    .copy-bibtex-btn {
      position: absolute;
      top: 0.5rem;
      right: 0.5rem;
      background-color: rgba(255, 255, 255, 0.8);
      border: 1px solid #dee2e6;
      border-radius: 4px;
      padding: 0.25rem 0.5rem;
      cursor: pointer;
      transition: all 0.2s ease;
      font-size: 0.8rem;
    }
    
    .copy-bibtex-btn:hover {
      background-color: var(--primary-light);
      color: white;
    }
    
    .copy-bibtex-btn.copied {
      background-color: #28a745;
      color: white;
    }
    
    /* Mobile-optimized pub links */
    .pub-links {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 1rem;
    }
    
    /* Citation info mobile friendly */
    .citation-info {
      margin-bottom: 2rem;
      padding: 1.25rem;
      background-color: var(--background-alt);
      border-radius: 0.5rem;
      box-shadow: var(--shadow);
      width: 100%;
    }
  </style>
"""
    html += scholarly_article_json_ld
    html += r"""
</head>
<body>
  <div class="container">
    <!-- Header/Navigation -->
    <header style="margin-bottom: 3rem; padding: 1.5rem 0; border-bottom: 1px solid rgba(0, 0, 0, 0.08); box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);">
      <div class="header-content">
        <a href="/" class="logo">
          Xin Li @ NTU
        </a>
        <button class="mobile-menu-button" aria-label="Toggle mobile menu">
          <i class="fas fa-bars"></i>
        </button>
        <nav>
          <a href="/" class="nav-link" style="color: var(--primary-dark); padding: 0.5rem 0.75rem; font-weight: 500; text-decoration: none; transition: all 0.3s ease; border-radius: 4px;">Home</a>
          <a href="/#about" class="nav-link" style="color: var(--primary-dark); padding: 0.5rem 0.75rem; font-weight: 500; text-decoration: none; transition: all 0.3s ease; border-radius: 4px;">About</a>
          <a href="/#research" class="nav-link" style="color: var(--primary-dark); padding: 0.5rem 0.75rem; font-weight: 500; text-decoration: none; transition: all 0.3s ease; border-radius: 4px;">Research</a>
        </nav>
      </div>
    </header>

    <main>
      <h1 class="page-title">Publications</h1>
"""
    citation_info = f"""      <div class="citation-info">
        <div style="display: flex; flex-wrap: wrap; gap: 1.5rem; margin-bottom: 1rem;">
          <div style="flex: 1;">
            <h3 style="margin-top: 0; margin-bottom: 0.5rem; font-size: 1.25rem; color: var(--text-primary);">Citation Metrics</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 1.5rem;">
              <div style="text-align: center; min-width: 80px;">
                <div style="font-size: 2rem; font-weight: 700; color: var(--primary); line-height: 1.2;">{citations}</div>
                <div style="font-size: 0.9rem; color: var(--text-secondary);">Citations</div>
              </div>
              <div style="text-align: center; min-width: 80px;">
                <div style="font-size: 2rem; font-weight: 700; color: var(--primary); line-height: 1.2;">{h_index}</div>
                <div style="font-size: 0.9rem; color: var(--text-secondary);">h-index</div>
              </div>
              <div style="text-align: center; min-width: 80px;">
                <div style="font-size: 2rem; font-weight: 700; color: var(--primary); line-height: 1.2;">{i10_index}</div>
                <div style="font-size: 0.9rem; color: var(--text-secondary);">i10-index</div>
              </div>
            </div>
          </div>
        </div>

        <div style="font-size: 0.875rem; text-align: right; color: var(--text-secondary); margin-top: 1rem;">
          Data from <a href="https://scholar.google.com/citations?user=Hxf8sNkAAAAJ" target="_blank" rel="noopener" style="color: var(--primary);">Google Scholar</a>
          <span style="margin-left: 0.5rem;">(Updated: {last_updated})</span>
        </div>
      </div>
      
      <div class="publications-header">
        <h2 class="section-title">All Publications</h2>
        <div class="publication-filters">
          <button class="filter-btn active" data-filter="all">All</button>
          <button class="filter-btn" data-filter="first-author">First Author</button>
          <button class="filter-btn" data-filter="recent">Recent</button>
        </div>
      </div>
      
      <div class="publications-list">
    """
    html += citation_info
    # Add all publications to the page
    for publication in publications:
        # For the standalone page, we don't need the hidden class
        publication['hidden'] = False
        html += generate_publication_card(publication)
    
    # Add the closing HTML tags and scripts
    html += """
      </div>
    </main>
    
    <footer>
      <p>&copy; <span id="current-year"></span> Xin Li. All rights reserved.</p>
    </footer>
  </div>
  
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // Set current year in the footer
      document.getElementById('current-year').textContent = new Date().getFullYear();
      
      // Mobile menu functionality
      const mobileMenuButton = document.querySelector('.mobile-menu-button');
      const nav = document.querySelector('nav');
      
      if (mobileMenuButton) {
        mobileMenuButton.addEventListener('click', function() {
          nav.classList.toggle('active');
          const isExpanded = nav.classList.contains('active');
          this.setAttribute('aria-expanded', isExpanded);
        });
        // Add event listener to close menu when a link is clicked
        nav.addEventListener('click', function(event) {
          if (event.target.tagName === 'A') {
            nav.classList.remove('active');
            mobileMenuButton.setAttribute('aria-expanded', 'false');
          }
        });
      }
      
      // Publication filters
      const filterButtons = document.querySelectorAll('.filter-btn');
      
      filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
          // Remove active class from all buttons
          filterButtons.forEach(b => b.classList.remove('active'));
          
          // Add active class to clicked button
          this.classList.add('active');
          
          // Get filter value
          const filter = this.getAttribute('data-filter');
          
          // Apply filtering logic
          const publicationCards = document.querySelectorAll('.publications-list .card');
          
          publicationCards.forEach(card => {
            if (filter === 'all') {
              card.style.display = '';
              card.style.opacity = '1';
            } else if (filter === 'first-author') {
              const authorText = card.querySelector('p')?.textContent || '';
              
              if (authorText.includes("Xin Li*") || authorText.startsWith("Xin Li,")) {
                card.style.display = '';
                card.style.opacity = '1';
              } else {
                card.style.display = 'none';
              }
            } else if (filter === 'recent') {
              const yearText = card.querySelector('p:nth-child(3)')?.textContent || '';
              const yearMatch = yearText.match(/\\d{4}/);
              const year = yearMatch ? parseInt(yearMatch[0]) : 0;
              
              if (year >= 2023) {
                card.style.display = '';
                card.style.opacity = '1';
              } else {
                card.style.display = 'none';
              }
            }
          });
        });
      });
      
      // BibTeX buttons functionality
      const bibtexButtons = document.querySelectorAll('.bibtex-btn');
      
      bibtexButtons.forEach(btn => {
        btn.addEventListener('click', function() {
          // Find the closest parent card
          const card = this.closest('.card');
          
          // Find the bibtex content within this card
          const bibtexContent = card.querySelector('.bibtex-content');
          
          // Toggle visibility with !important override
          if (bibtexContent.style.display === 'block') {
            bibtexContent.style.display = 'none';
          } else {
            // Force display block with !important by using inline style setAttribute
            bibtexContent.setAttribute('style', 'display: block !important');
          }
        });
      });
      
      // BibTeX copy buttons functionality
      const copyBibtexButtons = document.querySelectorAll('.copy-bibtex-btn');
      
      copyBibtexButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
          // Prevent the click from bubbling up and toggling the display
          e.stopPropagation();
          
          // Get the bibtex content (parent element's text content without the button text)
          const bibtexElement = this.parentElement;
          const bibtexText = bibtexElement.textContent.trim();
          
          // Copy to clipboard
          navigator.clipboard.writeText(bibtexText).then(() => {
            // Visual feedback
            this.classList.add('copied');
            const originalIcon = this.innerHTML;
            this.innerHTML = '<i class="fas fa-check"></i>';
            
            // Reset after 2 seconds
            setTimeout(() => {
              this.classList.remove('copied');
              this.innerHTML = originalIcon;
            }, 2000);
          }).catch(err => {
            console.error('Could not copy text: ', err);
          });
        });
      });
    });
  </script>
</body>
</html>
"""
    return html


def main():
    """Main function to generate and update publications HTML"""
    # Update file paths to use the correct directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    json_file = os.path.join(root_dir, 'data', 'publications.json')
    html_file = os.path.join(root_dir, 'index.html')
    pubs_file = os.path.join(root_dir, 'pubs.html')
    
    print(f"Loading publications data from {json_file}")
    data = load_json(json_file)
    
    if not data:
        print("Failed to load publications data. Exiting.")
        return
    
    print("Generating publications HTML...")

    # Generate publications section for index.html
    publications_html, last_updated = generate_publications_html(data)
    
    print(f"Updating HTML file at {html_file}")
    update_html_file(html_file, publications_html, last_updated)
    print(f"Successfully updated publications section in {html_file}")
    
    # Generate standalone publications page
    print(f"Generating standalone publications page at {pubs_file}")
    pubs_html = generate_standalone_publications_page(data)
    with open(pubs_file, 'w', encoding='utf-8') as file:
        file.write(pubs_html)
    print(f"Successfully generated standalone publications page at {pubs_file}")
    
    print(f"Last updated: {last_updated}")


if __name__ == "__main__":
    main()
