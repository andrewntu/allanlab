---
title: "CN Liu - Publications"
layout: gridlay
excerpt: "CN Liu -- Publications."
sitemap: false
permalink: /publications/
---


## Publications
**You can find all the abtract and publications on the [google scholar](https://scholar.google.com/citations?user=92mnkwIAAAAJ&hl=en&inst=6453797383205921872&authuser=1).**

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

## upcoming


## Full List of publications

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }} </a> (<em> News: {{ publi.news1 }}, {{ publi.news2 }},  {{ publi.news3 }}, {{ publi.news4 }}, {{ publi.news5 }} </em>)

{% endfor %}

## Thesis
<em>**Liu, Cheng-Nan***, Ting Chung Huang, and Yih Min Wu</em><br />Using low-cost seismometers and machine learning on earthquake early warning.<br /> [Master Thesis](https://doi.org/10.6342/NTU201901735) (2019)
