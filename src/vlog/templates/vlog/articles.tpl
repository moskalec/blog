{% extends 'core/base.tpl' %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
  <li class="breadcrumb-item active"><a href="{{ url('vlog:articles') }}">{{ _('Articles') }}</a></li>
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