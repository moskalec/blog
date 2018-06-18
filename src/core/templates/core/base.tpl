<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap.min.css">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        {% block navbar %}
            {% include 'core/navbar.tpl' %}
        {% endblock %}
        <br>
        <div class="content container">
            <div class="row">
                <div class="col-sm-8 blog-main">
                    {% block content %}
                    {% endblock %}
                </div>
                <div class="col-sm-3 offset-sm-1 blog-sidebar">
                    {% include "vlog/most_popular_categories.tpl" %}
                    {% include "vlog/most_populated_tags.tpl" %}
                    {% include "vlog/most_commented_articles.tpl" %}
                </div>
            </div>
        </div>
    </body>
    <script src="{{ STATIC_URL }}js/bootstrap.min.js"></script>
</html>