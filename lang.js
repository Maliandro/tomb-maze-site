// Iki dilli sayfa: metinler data-tr / data-en niteliklerinde tutulur.
// Secim localStorage'da saklanir; tarayici dili Turkce degilse Ingilizce baslar.
(function () {
  var KEY = 'tombmaze-lang';
  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) { }
  var lang = saved || ((navigator.language || 'en').toLowerCase().indexOf('tr') === 0 ? 'tr' : 'en');

  function apply(l) {
    lang = l;
    document.documentElement.lang = l;
    var nodes = document.querySelectorAll('[data-tr]');
    for (var i = 0; i < nodes.length; i++) {
      var v = nodes[i].getAttribute(l === 'tr' ? 'data-tr' : 'data-en');
      if (v !== null) nodes[i].innerHTML = v;
    }
    var btn = document.getElementById('lang');
    if (btn) btn.textContent = l === 'tr' ? 'English' : 'Türkçe';
    try { localStorage.setItem(KEY, l); } catch (e) { }
  }

  var btn = document.getElementById('lang');
  if (btn) {
    btn.addEventListener('click', function () { apply(lang === 'tr' ? 'en' : 'tr'); });
  }
  apply(lang);
})();
