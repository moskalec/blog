{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block breadcrumb %}
  {{ macro.breadcrumps(crumbs, _('Popular articles')) }}
{% endblock %}

{% block content %}
    {% for article in popular_articles %}
        <div class="blog-post">
            <h4><a href="{{ url('vlog:article', article.category.slug, article.slug) }}">{{ article.title }}</a></h4>
        </div>
    {% endfor %}
{% endblock %}