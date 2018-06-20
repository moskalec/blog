{% extends 'core/base.tpl' %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:categories') }}">{{ _('Categories') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:popular_categories') }}">{{ _('Popular categories') }}</a></li>
{% endblock %}

{% block content %}
    {% for category in popular_categories %}
        <div class="blog-post">
            <h4><a href="/">{{ category.title }}</a></h4>
        </div>
    {% endfor %}
{% endblock %}