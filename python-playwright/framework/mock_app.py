"""A tiny self-contained web app used to practice network mocking.

We don't need a real website to learn interception: we hand the browser this
HTML with ``page.set_content(...)``, and the page's JavaScript calls a real API
(DummyJSON). That gives us a deterministic "frontend" whose backend we can stub,
fail, or modify with ``page.route(...)``.

The app:
- has a "Load products" button (id ``load``)
- on click, fetches ``https://dummyjson.com/products?limit=10``
- renders each product title as ``<li class="product">``
- reveals ``#error`` if the request fails or returns a non-OK status
"""

from __future__ import annotations

PRODUCTS_URL_GLOB = "**/products*"

PRODUCTS_APP_HTML = """<!doctype html>
<html>
<head><meta charset="utf-8"><title>Mock Products</title></head>
<body>
  <h1>Products</h1>
  <button id="load">Load products</button>
  <ul id="list"></ul>
  <p id="error" hidden>Failed to load products</p>
  <script>
    const list = document.getElementById('list');
    const error = document.getElementById('error');
    document.getElementById('load').addEventListener('click', async () => {
      error.hidden = true;
      list.innerHTML = '';
      try {
        const res = await fetch('https://dummyjson.com/products?limit=10');
        if (!res.ok) throw new Error('http ' + res.status);
        const data = await res.json();
        for (const p of data.products) {
          const li = document.createElement('li');
          li.className = 'product';
          li.textContent = p.title;
          list.appendChild(li);
        }
      } catch (e) {
        error.hidden = false;
      }
    });
  </script>
</body>
</html>
"""
