<h4>{{ _('Популярные тэги') }}</h4>
{% for most_populated_tag in most_populated_tags %}
    <div class="sidebar-module sidebar-module-inset">
        <h5><a href="/">{{ most_populated_tag.title }}</a></h5>
    </div>
{% endfor %}