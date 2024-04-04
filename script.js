document.addEventListener("DOMContentLoaded", function() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"][name="paper_tag"]');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', filterPapers);
    });

    function filterPapers() {
        const checkedValues = Array.from(checkboxes)
            .filter(checkbox => checkbox.checked)
            .map(checkbox => checkbox.value);

        const papers = document.querySelectorAll('.paper');

        papers.forEach(paper => {
            const paperTags = paper.getAttribute('data-tags').split(',');
            const isMatch = paperTags.some(tag => checkedValues.includes(tag));
            paper.style.display = isMatch ? '' : 'none';
        });
    }

    filterPapers(); // Run initially to apply filter based on default checked states
});
