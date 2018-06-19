<h4><a href="{{ url('vlog:tags') }}">{{ _('Популярные тэги') }}</a></h4>
{% for most_populated_tag in most_populated_tags %}
    <div class="sidebar-module sidebar-module-inset">
        <h5>{{ most_populated_tag.title }}</h5>
    </div>
{% endfor %}