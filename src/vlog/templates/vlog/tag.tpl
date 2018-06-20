{% extends "core/base.tpl" %}

{% block title %}{{ tag.title }}{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:tags') }}">{{ _('Tags') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:tags') }}{{ tag.slug }}">{{ tag.title }}</a></li>
{% endblock %}

{% block content %}
    <h1 class="blog-post-title">{{ tag.title }}</h1>
    {% for article in articles %}
        <div class="blog-post">
            <h4><a href="/">{{ article.title }}</a></h4>
            <div class="date">
                {{ article.created }}
            </div>
        </div>
    {% endfor %}
{% endblock %}