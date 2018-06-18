{% extends 'core/base.tpl' %}

{% block content %}
    {% for category in categories %}
        <div class="blog-post">
            <h4><a href="/">{{ category.title }}</a></h4>
            <div class="date">
                {{ category.created }}
            </div>
        </div>
    {% endfor %}
{% endblock %}