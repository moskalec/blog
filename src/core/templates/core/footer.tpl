<footer class="footer navbar navbar-dark bg-primary">
    <div class="container">
        <span class="text-muted">
            <a class="navbar-brand" href="{{ url('vlog:index') }}">{{ _('Blog') }}</a>
        </span>
            <a class="navbar-brand" href="{{ url('vlog:index') }}">{{ _('Home') }}</a>
            <a class="navbar-brand" href="{{ url('vlog:articles') }}">{{ _('Articles') }}</a>
            <a class="navbar-brand" href="{{ url('vlog:categories') }}">{{ _('Categories') }}</a>
            <a class="navbar-brand" href="{{ url('vlog:tags') }}">{{ _('Tags') }}</a>
    </div>
</footer>