<h4>{{ _('Комментируемые статьи') }}</h4>
{% for most_commented_article in most_commented_articles %}
    <div class="sidebar-module sidebar-module-inset">
        <h5><a href="/">{{ most_commented_article.title }}</a></h5>
    </div>
{% endfor %}