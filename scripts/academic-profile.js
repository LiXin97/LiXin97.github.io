document.addEventListener('DOMContentLoaded', function() {
  // Set current year in the footer
  const currentYearSpan = document.getElementById('current-year');
  if (currentYearSpan) {
    currentYearSpan.textContent = new Date().getFullYear();
  }
  
  // Simple animation on scroll
  const animateElements = document.querySelectorAll('.card:not(.hidden-pub), .award-item, .education-item, .interest-item, .activity-category');
  
  function checkScroll() {
    animateElements.forEach((element, index) => {
      const elementTop = element.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
      
      if (elementTop < windowHeight * 0.9) {
        setTimeout(() => {
          element.classList.add('visible');
        }, index * 50);
      }
    });
  }
  
  // Initial check
  checkScroll();
  
  // Check on scroll
  window.addEventListener('scroll', checkScroll);
  
  // Header scroll effect
  const header = document.querySelector('header');
  
  function handleHeaderScroll() {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }
  
  // Initial check
  handleHeaderScroll();
  
  // Check on scroll
  window.addEventListener('scroll', handleHeaderScroll);
  
  // Mobile menu toggle
  const mobileMenuButton = document.querySelector('.mobile-menu-button');
  const nav = document.querySelector('nav');
  
  if (mobileMenuButton && nav) {
    mobileMenuButton.addEventListener('click', () => {
      nav.classList.toggle('open');
      
      // Change icon
      const icon = mobileMenuButton.querySelector('i');
      if (icon) {
        if (nav.classList.contains('open')) {
          icon.classList.remove('fa-bars');
          icon.classList.add('fa-times');
        } else {
          icon.classList.remove('fa-times');
          icon.classList.add('fa-bars');
        }
      }
    });
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', (event) => {
      if (!nav.contains(event.target) && !mobileMenuButton.contains(event.target)) {
        nav.classList.remove('open');
        const icon = mobileMenuButton.querySelector('i');
        if (icon) {
          icon.classList.remove('fa-times');
          icon.classList.add('fa-bars');
        }
      }
    });
  }
  
  // News toggle functionality
  const newsToggleBtn = document.getElementById('news-toggle-btn');
  const hiddenNewsItems = document.querySelectorAll('.hidden-news');
  
  if (newsToggleBtn && hiddenNewsItems.length > 0) {
    newsToggleBtn.addEventListener('click', function() {
      // Toggle visibility of hidden news items
      hiddenNewsItems.forEach(item => {
        item.classList.toggle('show');
      });
      
      // Update button text
      if (this.textContent === 'View all news') {
        this.textContent = 'View less';
      } else {
        this.textContent = 'View all news';
      }
      
      // Smooth scroll back to news section if items are hidden
      if (this.textContent === 'View all news') {
        const newsSection = document.getElementById('news');
        if (newsSection) {
          newsSection.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  }
  
  // Publications toggle functionality
  const pubToggleBtn = document.getElementById('pub-toggle-btn');
  const hiddenPubItems = document.querySelectorAll('.hidden-pub');
  
  if (pubToggleBtn && hiddenPubItems.length > 0) {
    pubToggleBtn.addEventListener('click', function() {
      // Toggle visibility of hidden publication items
      hiddenPubItems.forEach(item => {
        item.classList.toggle('show');
        
        // Handle animation of newly visible items
        if (item.classList.contains('show')) {
          setTimeout(() => {
            item.classList.add('visible');
          }, 100);
        } else {
          item.classList.remove('visible');
        }
      });
      
      // Update button text
      if (this.textContent === 'View all publications') {
        this.textContent = 'View less';
      } else {
        this.textContent = 'View all publications';
      }
      
      // Smooth scroll back to publications section if items are hidden
      if (this.textContent === 'View all publications') {
        const pubsSection = document.getElementById('publications');
        if (pubsSection) {
          pubsSection.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  }
  
  // Smooth scrolling for navigation links
  const navLinks = document.querySelectorAll('a[href^="#"]');
  navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      const targetElement = document.querySelector(targetId);
      
      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: 'smooth'
        });
        
        // Update URL without page reload
        history.pushState(null, null, targetId);
      }
    });
  });
  
  // Handle active state for nav links based on scroll position
  function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const scrollPosition = window.scrollY + 100; // Add offset for header
    
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute('id');
      
      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        // Remove active class from all nav links
        document.querySelectorAll('.nav-link').forEach(link => {
          link.classList.remove('active');
        });
        
        // Add active class to corresponding nav link
        const activeLink = document.querySelector(`.nav-link[href="#${sectionId}"]`);
        if (activeLink) {
          activeLink.classList.add('active');
        }
      }
    });
  }
  
  // Update active nav link on scroll
  window.addEventListener('scroll', updateActiveNavLink);
  updateActiveNavLink(); // Initialize on page load
}); 