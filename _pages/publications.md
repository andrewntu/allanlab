---
title: "CN Liu - Publications"
layout: gridlay
excerpt: "CN Liu -- Publications."
sitemap: false
permalink: /publications/
---
<div markdown="0" class="cover-image-container" style="text-align: center; margin: 1px 0;">
<img src="{{ site.url }}{{ site.baseurl }}/images/cover/DC.jpg" 
    alt="Cover Image" 
    style="width: 100%; max-height: 250px; object-fit: fill; border-radius: 1px;">
</div>

#### Publications
**You can find all the abtracts and publications on my [google scholar](https://scholar.google.com/citations?user=92mnkwIAAAAJ&hl=en&inst=6453797383205921872&authuser=1).**

<!-- {% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>
  <p><strong><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></strong></p>
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<p> &nbsp; </p> -->

#### Upcoming
- Seismic and Thermal Disturbances at Upper Geyser Hill, Yellowstone National Park (2023): Insights into Hydrothermal System Dynamics <br />
<em>**Liu, C. N.***, Lin, F. C., Manga, M., Farrell, J., Reed, M. H., Barth, A.,... & White, E. (**in prep.**) </em><br />

- An ML-Enhanced Earthquake Catalog for the 2024 Mw 7.4 Hualien Earthquake Sequence: Insights into Structural Transition from Collision to Subduction in Eastern Taiwan <br />
<em>Yang, H.-Y.^, H.-H. Huang*, E.-S. Wu^, H.-A. Chen^, C.-N. Liu, Y.-F. Hsu, W.-T. Liang, and C.-S. Ku  (**in revision (JRL)**) </em><br />

- Seismic Monitoring on Steamboat Geyser, Yellowstone National Park (TBD) <br />
<em>**Liu, C. N.***, Lin, F. C., Manga, M., Farrell, J. (**in prep.**) </em><br />


#### Full List of publications

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }} </a> {% if publi.news1 %} (News: <a href="{{ publi.news1.url }}">{{ publi.news1.name }}</a>, <a href="{{ publi.news2.url }}">{{ publi.news2.name }}</a>, <a href="{{ publi.news3.url }}">{{ publi.news3.name }}</a>, <a href="{{ publi.news4.url }}">{{ publi.news4.name }}</a>, <a href="{{ publi.news5.url }}">{{ publi.news5.name }}</a>){% endif %}

{% endfor %}

<!-- {% for publi in site.data.publist %}
  {{ publi.title }} <br />
  <em>{{ publi.authors }}</em><br />
  <a href="{{ publi.link.url }}">{{ publi.link.display }}</a>
  {% if publi.news %}
    (<em> News:
    {% for news_item in publi.news %}
      <a href="{{ news_item.url }}">{{ news_item.name }}</a>{% if forloop.last == false %}, {% endif %}
    {% endfor %}
    </em>)
  {% endif %}
  <br /><br />
{% endfor %} -->

#### Thesis
Using low-cost seismometers and machine learning on earthquake early warning.<br />
<em>**Liu, Cheng-Nan***, Ting Chung Huang, and Yih Min Wu</em><br /> [Master Thesis](https://doi.org/10.6342/NTU201901735) (2019)
