document.addEventListener("DOMContentLoaded", function() {
  const keywordCheckboxes =
      document.querySelectorAll('input[type="checkbox"][name="paper_keyword"]');
  const yearCheckboxes =
      document.querySelectorAll('input[type="checkbox"][name="paper_year"]');

  keywordCheckboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
      if (checkbox.value === "All") {
        const isChecked = checkbox.checked;
        keywordCheckboxes.forEach(cb => {
          cb.checked = isChecked; // Set all keyword checkboxes to the same
                                  // state as "Show All"
        });
      } else {
        // If any checkbox other than "All" is changed, ensure "Show All" is not
        // checked
        document
            .querySelector(
                'input[type="checkbox"][name="paper_keyword"][value="All"]')
            .checked = false;
      }
      filterPapers();
    });
  });

  yearCheckboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
      if (checkbox.value === "All") {
        const isChecked = checkbox.checked;
        yearCheckboxes.forEach(cb => {
          cb.checked = isChecked; // Set all year checkboxes to the same state
                                  // as "Show All"
        });
      } else {
        // If any checkbox other than "All" is changed, ensure "Show All" is not
        // checked
        document
            .querySelector(
                'input[type="checkbox"][name="paper_year"][value="All"]')
            .checked = false;
      }
      filterPapers();
    });
  });

  function filterPapers() {
    const checkedKeywords = Array.from(keywordCheckboxes)
                                .filter(checkbox => checkbox.checked)
                                .map(checkbox => checkbox.value);
    const checkedYears = Array.from(yearCheckboxes)
                             .filter(checkbox => checkbox.checked)
                             .map(checkbox => checkbox.value);

    const papers = document.querySelectorAll('.paper');

    papers.forEach(paper => {
      const paperKeywords = paper.getAttribute('data-paper-keywords').split(',');
      const paperYear = paper.getAttribute('data-paper-year');
      // Since all keywords/years are now selected with "Show All", no need to
      // check for "All"
      const hasKeyword =
          paperKeywords.some(keyword => checkedKeywords.includes(keyword));
      const hasYear = checkedYears.includes(paperYear);
      paper.style.display = hasKeyword && hasYear ? '' : 'none';
    });
  }

  filterPapers(); // Run initially to apply filter based on default checked
                  // states
});

// Function to open the modal
function openModal(modalId) {
  document.getElementById(modalId).style.display = "block";
}


// Function to copy BibTeX
function copyBibtex(bibtexId) {
    var bibtexText = document.getElementById(bibtexId).innerText;
    navigator.clipboard.writeText(bibtexText)
        .then(function() { alert('Copied to clipboard'); },
              function(err) { console.error('Could not copy text: ', err); });
}

// Function to close the modal
function closeModal(modalId) {
  document.getElementById(modalId).style.display = "none";
}