// Progressive enhancement only. Every page is fully readable with JS disabled.
(function () {
  'use strict';

  // Insert a filter box above each table that has more than a handful of rows.
  var blocks = document.querySelectorAll('.block');
  Array.prototype.forEach.call(blocks, function (block) {
    var table = block.querySelector('table');
    if (!table) return;
    var rows = table.querySelectorAll('tbody tr');
    if (rows.length < 6) return;

    var tools = document.createElement('div');
    tools.className = 'tools';
    var input = document.createElement('input');
    input.type = 'search';
    input.placeholder = 'Filter rows in this table\u2026';
    input.setAttribute('aria-label', 'Filter rows in ' + (block.querySelector('h2') || {}).textContent);
    var count = document.createElement('span');
    count.className = 'count';
    count.textContent = rows.length + ' rows';
    tools.appendChild(input);
    tools.appendChild(count);
    block.insertBefore(tools, block.querySelector('.tablewrap'));

    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      var shown = 0;
      Array.prototype.forEach.call(rows, function (tr) {
        var hit = !q || tr.textContent.toLowerCase().indexOf(q) !== -1;
        tr.classList.toggle('hide', !hit);
        if (hit) shown++;
      });
      count.textContent = shown + ' / ' + rows.length + ' rows';
    });
  });

  // Flag any link that leaves the site without a resolvable href (build-time
  // integrity check surfaced in the browser too).
  var broken = document.querySelectorAll('a[href=""], a[href="#"], a.chip:not([href])');
  if (broken.length) {
    console.warn('[site] links with no target:', broken.length);
  }
})();
