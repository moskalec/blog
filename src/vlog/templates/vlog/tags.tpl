{% extends 'core/base.tpl' %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
  <li class="breadcrumb-item active"><a href="{{ url('vlog:tags') }}">{{ _('Tags') }}</a></li>
{% endblock %}

{% block content %}
    {% for tag in tags %}
        <div class="blog-post">
            <h4><a href="{{ tag.slug }}">{{ tag.title }}</a></h4>
        </div>
    {% endfor %}
{% endblock %}