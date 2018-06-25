{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block breadcrumb %}
  {{ macro.breadcrumps(crumbs, 'Tags') }}
{% endblock %}

{% block content %}
    {% for tag in tags %}
        <div class="blog-post">
            <h4><a href="{{ url('vlog:tag', tag.slug) }}">{{ tag.title }}</a></h4>
        </div>
    {% endfor %}
{% endblock %}