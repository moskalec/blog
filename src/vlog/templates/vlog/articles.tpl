{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block breadcrumb %}
  {{ macro.breadcrumps(crumbs, 'Articles') }}
{% endblock %}

{% block content %}
    {% for article in articles %}
        <div class="blog-post">
            <h4><a href="{{ url('vlog:article', article.category.slug, article.slug) }}">{{ article.title }}</a></h4>
            <p>{{ article.description|linebreaksbr }}</p>
            <div class="date">
                {{ article.created }}
            </div>
        </div>
    {% endfor %}
{% endblock %}