{% for article in articles %}
    <div class="blog-post">
        <h4><a href="/{{ category.slug }}/{{ article.slug }}/">{{ article.title }}</a></h4>
        <p>{{ article.description|linebreaksbr }}</p>
        <div class="date">
            {{ article.created }}
        </div>
    </div>
{% endfor %}