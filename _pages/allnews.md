---
title: "News"
layout: textlay
excerpt: "Cheng-Nan at UofU."
sitemap: false
permalink: /allnews.html
---

# News
{% for article in site.data.news %}
<div markdown="0" class="news-item">
    <strong>{{ article.date }}</strong>
    <p>{{ article.headline }}</p>
</div>
{% endfor %}