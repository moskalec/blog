<h4><a href="{{ url('vlog:popular_articles') }}">{{ _('Комментируемые статьи') }}</a></h4>
{% for article in most_commented_articles %}
    <div class="sidebar-module sidebar-module-inset">
        <h5><a href="/">{{ article.title }}</a></h5>
    </div>
{% endfor %}