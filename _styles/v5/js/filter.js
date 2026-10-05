/* Publications: filter by thread. Without JS every paper is shown and the buttons stay hidden. */
(function () {
  var group = document.querySelector('.filter');
  if (!group) return;
  var pubs = [].slice.call(document.querySelectorAll('.pub'));
  var years = [].slice.call(document.querySelectorAll('.year'));
  group.addEventListener('click', function (ev) {
    var b = ev.target.closest('button');
    if (!b) return;
    var f = b.dataset.f;
    group.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
    pubs.forEach(function (p) { p.hidden = !(f === 'all' || p.dataset.thread === f); });
    years.forEach(function (y) { y.hidden = !y.querySelector('.pub:not([hidden])'); });
  });
})();
