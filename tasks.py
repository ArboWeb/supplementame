from invoke import task


@task
def start(c):
    """Start the Django development server."""
    c.run("python manage.py runserver", pty=False)


@task
def start_front(c):
    """Load initial data into the database."""
    c.run("npm install")
    c.run("npm start", pty=False)


@task
def build_front(c):
    """Load initial data into the database."""
    c.run("npm install")
    c.run("npm run build")


@task
def load_data(c):
    """Load initial data into the database."""
    c.run("python manage.py createcachetable")
    c.run("python manage.py migrate")
    c.run("python manage.py load_initial_data")
    c.run("python manage.py collectstatic --noinput")


@task
def dump_data(c):
    """Dump data to a JSON fixture."""
    dump_command = (
        "python ./manage.py dumpdata --natural-foreign --indent 2 "
        "-e auth.permission "
        "-e contenttypes "
        "-e wagtailcore.GroupCollectionPermission "
        "-e wagtailimages.rendition "
        "-e images.rendition "
        "-e sessions "
        "-e wagtailsearch.indexentry "
        "-e wagtailsearch.sqliteftsindexentry "
        "-e wagtailcore.referenceindex "
        "-e wagtailcore.pagesubscription > fixtures/demo.json"
    )
    c.run(dump_command)


@task
def reset_db(c):
    """Reset the database and reload initial data."""
    c.run("python manage.py reset_db --noinput")
    load_data(c)


@task(pre=[load_data, start])
def init(c):
    """Initialize the project by loading data and starting the server."""
    pass
