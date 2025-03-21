/**
 * Publications Manager 
 * This script loads publication data from a JSON file and renders it to the page
 */

class PublicationsManager {
  constructor() {
    this.publicationsData = null;
    this.publicationsSection = document.getElementById('publications');
    
    // Check if publications section exists
    if (!this.publicationsSection) {
      console.error('Publications section not found in the DOM');
    } else {
      console.log('Publications section found:', this.publicationsSection);
    }
    
    // Use relative path instead of absolute path
    this.jsonPath = '/data/publications.json';
  }

  /**
   * Initialize the publications manager
   */
  async init() {
  }

  /**
   * Load the publications data from the JSON file
   */
  async loadPublicationsData() {
    try {
      console.log(`Attempting to load publications from: ${this.jsonPath}`);
      const response = await fetch(this.jsonPath);
      
      if (!response.ok) {
        throw new Error(`Failed to load publications data: ${response.status} ${response.statusText}`);
      }
      
      const data = await response.json();
      console.log('Publications data loaded successfully:', data);
      this.publicationsData = data;
    } catch (error) {
      console.error('Error loading publications data:', error);
      throw error;
    }
  }

  /**
   * Render the publications section
   */
  renderPublications() {
    if (!this.publicationsData || !this.publicationsSection) return;

    // Clear existing content
    this.publicationsSection.innerHTML = '';
    
    // Create section title
    const titleElement = document.createElement('h2');
    titleElement.className = 'section-title';
    titleElement.textContent = 'Publications';
    this.publicationsSection.appendChild(titleElement);

    // Create citation info
    if (this.publicationsData.citations) {
      const citationInfo = document.createElement('div');
      citationInfo.className = 'citation-info';
      citationInfo.innerHTML = `
        <p class="stats">
          Citations: ${this.publicationsData.citations.count}
          <span class="update-date">(Last updated: ${this.publicationsData.citations.lastUpdated})</span>
        </p>
      `;
      this.publicationsSection.appendChild(citationInfo);
    }

    // Add introductory text
    const introText = document.createElement('p');
    introText.textContent = 'Selected publications:';
    this.publicationsSection.appendChild(introText);

    // Render publications list
    this.renderPublicationsList(
      this.publicationsData.publications,
      'publications-list'
    );

    // Render manuscripts if they exist
    if (this.publicationsData.manuscripts && this.publicationsData.manuscripts.length > 0) {
      const manuscriptsTitle = document.createElement('div');
      manuscriptsTitle.className = 'section-subtitle';
      manuscriptsTitle.style = 'margin-top: 2rem; font-weight: 600; font-size: 1.25rem;';
      manuscriptsTitle.textContent = 'Manuscripts Under Review';
      this.publicationsSection.appendChild(manuscriptsTitle);
      
      this.renderPublicationsList(
        this.publicationsData.manuscripts,
        'publications-list manuscripts-list'
      );
    }

    // Add toggle button if there are hidden publications
    const hasHiddenPubs = this.hasHiddenPublications();
    if (hasHiddenPubs) {
      const buttonsContainer = document.createElement('div');
      buttonsContainer.className = 'publications-buttons';
      buttonsContainer.innerHTML = `
        <button id="pub-toggle-btn" class="view-all-button">View all publications</button>
      `;
      this.publicationsSection.appendChild(buttonsContainer);
    }
  }

  /**
   * Check if there are any hidden publications
   */
  hasHiddenPublications() {
    const publications = this.publicationsData.publications || [];
    const manuscripts = this.publicationsData.manuscripts || [];
    
    return [...publications, ...manuscripts].some(pub => pub.hidden);
  }

  /**
   * Render a list of publications
   * @param {Array} publications - The publications to render
   * @param {String} containerClass - The CSS class for the container
   */
  renderPublicationsList(publications, containerClass) {
    const container = document.createElement('div');
    container.className = containerClass;
    
    publications.forEach(pub => {
      const card = this.createPublicationCard(pub);
      container.appendChild(card);
    });
    
    this.publicationsSection.appendChild(container);
  }

  /**
   * Create a publication card
   * @param {Object} publication - The publication data
   * @returns {HTMLElement} - The publication card element
   */
  createPublicationCard(publication) {
    const card = document.createElement('div');
    card.className = `card ${publication.hidden ? 'hidden-pub' : ''}`;
    
    // Title
    const title = document.createElement('h3');
    title.textContent = publication.title;
    card.appendChild(title);
    
    // Authors (highlight your name)
    const authors = document.createElement('p');
    authors.innerHTML = this.formatAuthors(publication.authors);
    if (publication.equalContribution) {
      authors.innerHTML += ' <span class="text-secondary">(*equal contribution)</span>';
    }
    card.appendChild(authors);
    
    // Venue and year
    const venue = document.createElement('p');
    venue.innerHTML = `<em>${publication.venue}</em>, ${publication.year}`;
    card.appendChild(venue);
    
    // Links
    if (publication.links && publication.links.length > 0) {
      const linksDiv = document.createElement('div');
      linksDiv.className = 'pub-links';
      
      publication.links.forEach(link => {
        const linkElement = document.createElement('a');
        linkElement.href = link.url;
        linkElement.className = 'pub-link';
        linkElement.target = '_blank';
        linkElement.rel = 'noopener noreferrer';
        linkElement.innerHTML = `<i class="${link.icon}"></i> ${link.text}`;
        linksDiv.appendChild(linkElement);
      });
      
      // Always add BibTeX button
      const bibtexBtn = document.createElement('button');
      bibtexBtn.className = 'pub-link bibtex-btn';
      bibtexBtn.innerHTML = '<i class="fas fa-quote-right"></i> BibTeX';
      linksDiv.appendChild(bibtexBtn);
      
      card.appendChild(linksDiv);
    } else {
      // If no links, just add BibTeX button
      const linksDiv = document.createElement('div');
      linksDiv.className = 'pub-links';
      
      const bibtexBtn = document.createElement('button');
      bibtexBtn.className = 'pub-link bibtex-btn';
      bibtexBtn.innerHTML = '<i class="fas fa-quote-right"></i> BibTeX';
      linksDiv.appendChild(bibtexBtn);
      
      card.appendChild(linksDiv);
    }
    
    // BibTeX content (hidden by default)
    const bibtexContent = document.createElement('pre');
    bibtexContent.className = 'bibtex-content';
    bibtexContent.textContent = publication.bibtex;
    card.appendChild(bibtexContent);
    
    return card;
  }

  /**
   * Format the authors list, highlighting your name
   * @param {Array} authors - The list of author names
   * @returns {String} - The formatted HTML for authors
   */
  formatAuthors(authors) {
    if (!authors || !Array.isArray(authors)) return '';
    
    return authors.map(author => {
      // Highlight your name with bold
      if (author.includes('Xin Li')) {
        return `<strong>${author}</strong>`;
      }
      return author;
    }).join(', ');
  }

  /**
   * Setup event listeners for the publications section
   */
  setupEventListeners() {
    // BibTeX toggle
    document.addEventListener('click', (e) => {
      if (e.target.closest('.bibtex-btn')) {
        this.handleBibtexClick(e);
      }
    });

    // Publications toggle button
    const pubToggleBtn = document.getElementById('pub-toggle-btn');
    if (pubToggleBtn) {
      pubToggleBtn.addEventListener('click', () => {
        this.toggleAllPublications();
      });
    }
  }

  /**
   * Handle BibTeX button click
   * @param {Event} e - The click event
   */
  async handleBibtexClick(e) {
    e.preventDefault();
    e.stopPropagation();
    
    // Get the parent card
    const button = e.target.closest('.bibtex-btn');
    const card = button.closest('.card');
    
    // Get the BibTeX content
    const bibtexContent = card.querySelector('.bibtex-content').textContent;
    
    try {
      // Try to use the modern clipboard API
      await navigator.clipboard.writeText(bibtexContent);
    } catch (err) {
      // Fallback for older browsers
      const textArea = document.createElement('textarea');
      textArea.value = bibtexContent;
      textArea.style.position = 'fixed'; // Make the textarea out of viewport
      document.body.appendChild(textArea);
      textArea.select();
      document.execCommand('copy');
      document.body.removeChild(textArea);
    }
    
    // Visual feedback on the button
    const originalText = button.innerHTML;
    button.innerHTML = '<i class="fas fa-check"></i> Copied!';
    button.classList.add('active');
    
    setTimeout(() => {
      button.innerHTML = originalText;
      button.classList.remove('active');
    }, 2000);
  }

  /**
   * Toggle visibility of all hidden publications
   */
  toggleAllPublications() {
    const hiddenPubs = document.querySelectorAll('.hidden-pub');
    const pubToggleBtn = document.getElementById('pub-toggle-btn');
    
    if (hiddenPubs[0]?.classList.contains('show')) {
      // Hide publications
      hiddenPubs.forEach(pub => pub.classList.remove('show'));
      if (pubToggleBtn) pubToggleBtn.textContent = 'View all publications';
    } else {
      // Show publications
      hiddenPubs.forEach(pub => pub.classList.add('show'));
      if (pubToggleBtn) pubToggleBtn.textContent = 'Show less';
    }
  }
}

// Initialize the publications manager when the DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  console.log('DOM fully loaded, initializing publications manager...');
  const pubManager = new PublicationsManager();
  pubManager.init();
}); 