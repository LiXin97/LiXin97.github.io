/* Scroll story: light the node the reader is on. Without JS the whole ring is lit and every step is readable. */
(function () {
  var box = document.querySelector('.scrolly');
  if (!box || !('IntersectionObserver' in window)) return;
  var steps = [].slice.call(box.querySelectorAll('.step'));
  box.dataset.step = 'evaluate';
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      box.dataset.step = en.target.dataset.step;
      steps.forEach(function (s) { s.classList.toggle('is-on', s === en.target); });
    });
  }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });
  steps.forEach(function (s) { io.observe(s); });
})();
