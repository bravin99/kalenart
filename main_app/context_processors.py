from main_app.models import SiteData


def site_data(request):
    try:
        my_site_data = SiteData.objects.latest("updated")
        return dict(my_site_data=my_site_data)
    except SiteData.DoesNotExist as exc:
        return {
            "my_site_data": None,
        }
