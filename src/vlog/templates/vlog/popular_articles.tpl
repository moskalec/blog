{% extends 'core/base.tpl' %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:articles') }}">{{ _('Articles') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:popular_articles') }}">{{ _('Popular articles') }}</a></li>
{% endblock %}

{% block content %}
    {% for article in popular_articles %}
        <div class="blog-post">
            <h4><a href="/">{{ article.title }}</a></h4>
        </div>
    {% endfor %}
{% endblock %}