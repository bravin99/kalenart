from django.db import models
from main_app.image_compresor import compress_image


class MainAppBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SiteData(MainAppBaseModel):
    header_title = models.CharField(max_length=100, default="Header title here", verbose_name="Headline")
    header_message = models.TextField(default="put intro here", verbose_name="Introduction")
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
    display = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.image_slug}"

    def save(self, *args, **kwargs):
        self.picture = compress_image(self.picture)
        return super(Feed, self).save()

    class Meta:
        verbose_name = "Feeds"
        verbose_name_plural = verbose_name
