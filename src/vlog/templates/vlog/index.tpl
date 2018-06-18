{% extends 'core/base.tpl' %}

{% block breadcrumb %}
  <li class="breadcrumb-item active"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
{% endblock %}

{% block content %}
    {% for article in articles %}
        <div class="blog-post">
            <h4><a href="{{ article.slug }}">{{ article.title }}</a></h4>
            <p>{{ article.description|linebreaksbr }}</p>
            <div class="date">
                {{ article.created }}
            </div>
        </div>
    {% endfor %}
{% endblock %}
