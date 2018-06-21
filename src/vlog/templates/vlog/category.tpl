{% extends "core/base.tpl" %}

{% block title %}{{ category.title }}{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:categories') }}">{{ _('Categories') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:categories') }}{{ category.slug }}">{{ category.title }}</li>
{% endblock %}

{% block content %}
    {% for article in articles %}
        <div class="blog-post">
            <h4><a href="articles/{{ article.slug }}">{{ article.title }}</a></h4>
            <div class="date">
                {{ article.created }}
            </div>
        </div>
    {% endfor %}
{% endblock %}