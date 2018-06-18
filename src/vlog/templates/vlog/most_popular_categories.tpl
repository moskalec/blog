<h4>{{ _('Популярные категории') }}</h4>
{% for most_popular_category in most_popular_categories %}
    <div class="sidebar-module sidebar-module-inset">
        <h5><a href="/">{{ most_popular_category.title }}</a></h5>
    </div>
{% endfor %}