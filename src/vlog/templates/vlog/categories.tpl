{% extends 'core/base.tpl' %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:categories') }}">{{ _('Categories') }}</a></li>
{% endblock %}

{% block content %}
    {% for category in categories %}
        <div class="blog-post">
            <h4><a href="{{ category.slug }}">{{ category.title }}</a></h4>
            <div class="date">
                {{ category.created }}
            </div>
        </div>
    {% endfor %}
{% endblock %}