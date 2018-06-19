{% extends "core/base.tpl" %}

{% block title %}{{ article.title }}{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}{{ category.slug }}">{{ category.title }}</a></li>
  <li class="breadcrumb-item active">{{ article.title }}</li>
{% endblock %}

{% block content %}
    <h1 class="blog-post-title">{{ article.title }}</h1>
    <div class="blog-post">
        <p>{{ article.content }}</p>
    </div>
{% endblock %}