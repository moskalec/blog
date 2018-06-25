<h4><a href="{{ url('vlog:popular_categories') }}">{{ _('Popular categories') }}</a></h4>
{% for category in most_popular_categories %}
    <div class="sidebar-module sidebar-module-inset">
        <h5><a href="{{ url('vlog:category', category.slug) }}">{{ category.title }}</a></h5>
    </div>
{% endfor %}