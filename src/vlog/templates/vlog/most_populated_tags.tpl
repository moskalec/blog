<h4><a href="{{ url('vlog:populated_tags') }}">{{ _('Популярные тэги') }}</a></h4>
{% for tag in most_populated_tags %}
    <div class="sidebar-module sidebar-module-inset">
        <h5><a href="{{ url('vlog:tags') }}{{ tag.slug }}">{{ tag.title }}</a></h5>
    </div>
{% endfor %}