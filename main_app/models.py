from django.db import models


class MainAppBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SiteData(MainAppBaseModel):
    header_title = models.CharField(max_length=100, default="Header title here")
    header_message = models.TextField(default="put intro here")
    instagram_link = models.URLField()
    email = models.EmailField()

    class Meta:
        verbose_name = "Site Data"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.header_title}"


def feed_upload_path(instance, filename):
    return f"feed_images/{instance.image_slug}/{filename}"


class Feed(MainAppBaseModel):
    image_slug = models.SlugField()
    picture = models.ImageField(upload_to=feed_upload_path)
    description = models.TextField()

    def __str__(self):
        return f"{self.image_slug}"

    class Meta:
        verbose_name = "Feeds"
        verbose_name_plural = verbose_name
