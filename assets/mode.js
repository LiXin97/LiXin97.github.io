// Footer light/dark switch. "auto" removes the attribute and lets prefers-color-scheme decide.
// Same localStorage key and values as the old site, so a choice made there carries over.
(function () {
  var root = document.documentElement, buttons = document.querySelectorAll('.mode-switch [data-mode]');
  function get() { try { return localStorage.getItem('theme') || 'system'; } catch (e) { return 'system'; } }
  function apply(mode) {
    if (mode === 'light' || mode === 'dark') root.setAttribute('data-mode', mode); else root.removeAttribute('data-mode');
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-mode') === mode)); });
  }
  buttons.forEach(function (b) {
    b.addEventListener('click', function () {
      var mode = b.getAttribute('data-mode');
      try { if (mode === 'system') localStorage.removeItem('theme'); else localStorage.setItem('theme', mode); } catch (e) {}
      apply(mode);
    });
  });
  apply(get());
})();
