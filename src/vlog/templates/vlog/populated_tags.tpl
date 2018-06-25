{% extends 'core/base.tpl' %}
{% import 'core/macros.tpl' as macro %}

{% block breadcrumb %}
  {{ macro.breadcrumps(crumbs, _('Populated tags')) }}
{% endblock %}

{% block content %}
    {% for tag in populated_tags %}
        <div class="blog-post">
            <h4><a href="{{ url('vlog:tag', tag.slug) }}">{{ tag.title }}</a></h4>
        </div>
    {% endfor %}
{% endblock %}