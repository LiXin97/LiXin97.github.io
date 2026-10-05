/* Preview-only controls: layout x palette. Not part of the shipped site. */
(function () {
  var palettes = [['paper', 'Paper'], ['night', 'Night'], ['swiss', 'Swiss']];
  var layouts = [['index.html', 'Table'], ['ring.html', 'Ring'], ['track.html', 'Track'], ['scroll.html', 'Scroll']];
  var cur = document.documentElement.dataset.theme || 'paper';
  var here = location.pathname.split('/').pop() || 'index.html';
  var bar = document.createElement('div');
  bar.className = 'preview';
  bar.setAttribute('role', 'region');
  bar.setAttribute('aria-label', 'Preview controls');
  bar.innerHTML =
    '<span class="preview__k">Layout</span>' + layouts.map(function (l) {
      return '<a href="' + l[0] + '"' + (l[0] === here ? ' aria-current="page"' : '') + '>' + l[1] + '</a>';
    }).join('') +
    '<span class="preview__sep" aria-hidden="true"></span><span class="preview__k">Palette</span>' + palettes.map(function (t) {
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
