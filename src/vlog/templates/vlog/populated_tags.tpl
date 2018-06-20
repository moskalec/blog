{% extends 'core/base.tpl' %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:tags') }}">{{ _('Tags') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:populated_tags') }}">{{ _('Popular tags') }}</a></li>
{% endblock %}

{% block content %}
    {% for tag in popular_tags %}
        <div class="blog-post">
            <h4><a href="/">{{ tag.title }}</a></h4>
        </div>
    {% endfor %}
{% endblock %}