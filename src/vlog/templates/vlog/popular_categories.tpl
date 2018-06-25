{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block breadcrumb %}
  {{ macro.breadcrumps(crumbs, _('Popular categories')) }}
{% endblock %}

{% block content %}
    {% for category in popular_categories %}
        <div class="blog-post">
            <h4><a href="{{ url('vlog:category', category.slug) }}">{{ category.title }}</a></h4>
        </div>
    {% endfor %}
{% endblock %}