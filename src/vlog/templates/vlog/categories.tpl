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

    <div class="pagination">
        <span class="step-links">
            {% if categories.has_previous %}
                <a href="?page=1">&laquo; first</a>
                <a href="?page={{ categories.previous_page_number }}">previous</a>
            {% endif %}

            <span class="current">
                Page {{ categories.number }} of {{ categories.paginator.per_pages }}.
            </span>

            {% if categories.has_next %}
                <a href="?page={{ categories.paginator_per_page }}">next</a>
                <a href="?page={{ categories.paginator.num_pages }}">last &raquo;</a>
            {% endif %}
        </span>
    </div>

{% endblock %}