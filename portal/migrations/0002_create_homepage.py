from django.db import migrations


def init_portal(apps, schema_editor):
    # Get models
    ContentType = apps.get_model("contenttypes.ContentType")
    Page = apps.get_model("wagtailcore.Page")
    Site = apps.get_model("wagtailcore.Site")
    HomePage = apps.get_model("portal.HomePage")

    # Delete the default homepage
    # If migration is run multiple times, it may have already been deleted
    Page.objects.filter(id=2).delete()

    # Create a new homepage
    homepage_content_type, __ = ContentType.objects.get_or_create(
        model="homepage", app_label="portal"
    )
    homepage = HomePage.objects.create(
        title="CoderDojo Verona",
        draft_title="CoderDojo Verona",
        slug="home",
        url_path="/home/",
        content_type=homepage_content_type,
        path="00010001",
        depth=2,
        numchild=0
    )

    # Create a site with the new homepage set as the root
    Site.objects.create(hostname="localhost", site_name="CoderDojo Verona", root_page=homepage, is_default_site=True)


def teardown_portal(apps, schema_editor):
    # Get models
    ContentType = apps.get_model("contenttypes.ContentType")
    HomePage = apps.get_model("portal.HomePage")

    # Delete the default homepage
    # Page, subpages and Site objects CASCADE
    HomePage.objects.filter(slug="home", depth=2).delete()

    # Delete content type for homepage model
    ContentType.objects.filter(model="homepage", app_label="portal").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(init_portal, teardown_portal),
    ]
