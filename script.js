document.documentElement.classList.add('js');

document.addEventListener('DOMContentLoaded', function() {
  // Automatically update the copyright year
  const yearSpan = document.getElementById('copyright-year');
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
  }

  const newsToggle = document.querySelector('.news-toggle');
  const extraNewsItems = document.querySelectorAll('.news-extra');

  if (newsToggle && extraNewsItems.length > 0) {
    newsToggle.addEventListener('click', function() {
      const isExpanded = this.getAttribute('aria-expanded') === 'true';

      extraNewsItems.forEach(item => {
        item.classList.toggle('is-visible', !isExpanded);
      });

      this.setAttribute('aria-expanded', String(!isExpanded));
      this.textContent = isExpanded ? 'View older news' : 'Show fewer news';
    });
  }
});
