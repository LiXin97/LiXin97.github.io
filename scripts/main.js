// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  // Navigation
  const nav = document.querySelector('.nav');
  const mobileMenuButton = document.querySelector('.mobile-menu-button');
  
  if (window.innerWidth <= 768) nav.style.display = 'none';
  
  mobileMenuButton?.addEventListener('click', () => {
    if (window.innerWidth <= 768) {
      nav.style.display = nav.style.display === 'flex' ? 'none' : 'flex';
    }
  });

  window.addEventListener('resize', () => {
    nav.style.display = window.innerWidth > 768 ? 'flex' : 'none';
  });

  document.addEventListener('click', (e) => {
    if (window.innerWidth <= 768 && !nav.contains(e.target) && !mobileMenuButton.contains(e.target)) {
      nav.style.display = 'none';
    }
  });

  // Smooth scrolling
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      e.preventDefault();
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        if (window.innerWidth <= 768) nav.style.display = 'none';
      }
    });
  });

  // Active navigation highlighting
  const sections = document.querySelectorAll('section[id]');
  const navItems = document.querySelectorAll('.nav-link');

  const highlightNavItem = () => {
    const scrollPosition = window.scrollY;
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 100;
      const sectionBottom = sectionTop + section.offsetHeight;
      const sectionId = section.getAttribute('id');
      
      if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
        navItems.forEach(item => {
          item.classList.remove('active');
          if (item.getAttribute('href') === `#${sectionId}`) {
            item.classList.add('active');
          }
        });
      }
    });
  };

  window.addEventListener('scroll', highlightNavItem);
  highlightNavItem();

  // Footer year
  const currentYearElement = document.getElementById('current-year');
  if (currentYearElement) {
    currentYearElement.textContent = new Date().getFullYear();
  }

  // BibTeX functionality
  document.querySelectorAll('.bibtex-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const card = this.closest('.publication-card');
      const bibtexContent = card?.querySelector('.bibtex-content');
      if (bibtexContent) {
        const isVisible = bibtexContent.style.display === 'block';
        bibtexContent.style.display = isVisible ? 'none' : 'block';
        const buttonText = this.querySelector('span');
        if (buttonText) buttonText.textContent = isVisible ? 'BibTeX' : 'Hide BibTeX';
      }
    });
  });

  // Copy BibTeX
  document.querySelectorAll('.copy-bibtex-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.stopPropagation();
      const bibtexText = this.parentElement.textContent.trim();
      navigator.clipboard.writeText(bibtexText)
        .then(() => {
          this.classList.add('copied');
          const originalIcon = this.innerHTML;
          this.innerHTML = '<i class="fas fa-check"></i>';
          setTimeout(() => {
            this.classList.remove('copied');
            this.innerHTML = originalIcon;
          }, 2000);
        })
        .catch(console.error);
    });
  });

  // Scroll animations
  const observer = new IntersectionObserver(
    entries => entries.forEach(entry => entry.isIntersecting && entry.target.classList.add('visible')),
    { threshold: 0.1 }
  );
  document.querySelectorAll('.fade-in').forEach(element => observer.observe(element));

  // Theme toggle
  const themeToggle = document.querySelector('.theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
    });

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
    }
  }
}); 