{% extends 'core/base.tpl' %}

{% block content %}
    {% for tag in tags %}
        <div class="blog-post">
            <h4><a href="/">{{ tag.title }}</a></h4>
        </div>
    {% endfor %}
{% endblock %}