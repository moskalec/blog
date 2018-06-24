{% extends 'core/base.tpl' %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{{ url('vlog:index') }}">{{ _('Home') }}</a></li>
  <li class="breadcrumb-item"><a href="{{ url('vlog:categories') }}">{{ _('Categories') }}</a></li>
{% endblock %}

{% block content %}
    {% for category in categories %}
        <div class="blog-post">
            <h4><a href="{{ url('vlog:category', category.slug) }}">{{ category.title }}</a></h4>
            <div class="date">
                {{ category.created }}
            </div>
        </div>
    {% endfor %}

    <nav aria-label="Page navigation example">
      <ul class="pagination">
        {% if categories.has_previous %}
            <li class="page-item">
                <a class="page-link" href="?page={{ categories.previous_page_number }}" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                    <span class="sr-only">Previous</span>
                </a>
            </li>
        {% else %}
          <li class="disabled"><span>&laquo;</span></li>
        {% endif %}
        {% for i in paginator.page_range %}
          {% if categories.number == i %}
            <li class="page-item active">
                <span class="page-link">
                    {{ i }}
                    <span class="sr-only">(current)</span>
                </span>
            </li>
          {% else %}
            <li class="page-item"><a class="page-link" href="?page={{ i }}">{{ i }}</a></li>
          {% endif %}
        {% endfor %}
        {% if categories.has_next %}
            <li>
                <a class="page-link" href="?page={{ categories.paginator.num_pages }}" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                    <span class="sr-only">Next</span>
                </a>
            </li>
        {% else %}
          <li class="disabled"><span>&raquo;</span></li>
        {% endif %}
      </ul>
    </nav>

{% endblock %}