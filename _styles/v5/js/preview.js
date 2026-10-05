/* Preview-only style switcher. Not part of the shipped site. */
(function () {
  var themes = [['paper', 'Paper'], ['night', 'Night'], ['swiss', 'Swiss']];
  var cur = document.documentElement.dataset.theme || 'paper';
  var bar = document.createElement('div');
  bar.className = 'preview';
  bar.setAttribute('role', 'group');
  bar.setAttribute('aria-label', 'Preview a visual style');
  bar.innerHTML = '<span class="preview__k">Style</span>' + themes.map(function (t) {
    return '<button type="button" data-t="' + t[0] + '" aria-pressed="' + (t[0] === cur) + '">' + t[1] + '</button>';
  }).join('');
  bar.addEventListener('click', function (ev) {
    var b = ev.target.closest('button');
    if (!b) return;
    document.documentElement.dataset.theme = b.dataset.t;
    try { localStorage.setItem('v5-theme', b.dataset.t); } catch (_) {}
    bar.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
  });
  document.body.appendChild(bar);
})();
