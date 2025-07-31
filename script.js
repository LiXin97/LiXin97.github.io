document.addEventListener('DOMContentLoaded', function() {
  // Automatically update the copyright year
  const yearSpan = document.getElementById('copyright-year');
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
  }
});