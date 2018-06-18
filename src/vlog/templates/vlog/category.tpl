{% extends "core/base.tpl" %}

{% block title %}{{ category.title }}{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:categories') }}">{{ _('Categories') }}</a></li>
  <li class="breadcrumb-item active"><a href="{{ url('vlog:categories') }}{{ category.slug }}">{{ category.title }}</a></li>
{% endblock %}

{% block content %}
    <h1 class="blog-post-title">{{ category.title }}</h1>
    {% for article in articles %}
        <div class="blog-post">
            <h4><a href="/{{ category.slug }}/{{ article.slug }}/">{{ article.title }}</a></h4>
        </div>
    {% endfor %}
{% endblock %}