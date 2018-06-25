{% extends "core/base.tpl" %}
{% import 'core/macros.tpl' as macro %}

{% block title %}{{ category.title }}{% endblock %}

{% block breadcrumb %}
  {{ macro.breadcrumps(crumbs, category.title) }}
{% endblock %}

{% block content %}
    {% for article in articles %}
        <div class="blog-post">
            <h4><a href="{{ url('vlog:article', article.category.slug, article.slug) }}">{{ article.title }}</a></h4>
            <div class="date">
                {{ article.created }}
            </div>
        </div>
    {% endfor %}
{% endblock %}