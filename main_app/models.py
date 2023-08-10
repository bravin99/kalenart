import uuid

from django.db import models
from django.shortcuts import reverse
from main_app.image_compresor import compress_image


class MainAppBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SiteData(MainAppBaseModel):
    site_name = models.CharField(max_length=155, default="Kalen Art")
    site_domain = models.URLField(default="https://kalen.art")
    site_keywords = models.TextField(help_text="comma separated keywords")
    header_title = models.CharField(max_length=100, default="Header title here", verbose_name="Headline")
    header_message = models.TextField(default="put intro here", verbose_name="Introduction")
    header_image = models.ImageField(upload_to="here_images/", null=True)
    instagram_link = models.URLField()
    facebook_link = models.URLField(default="https://facebook.com/the.kalen")
    email = models.EmailField()
    terms_and_conditions = models.TextField()

    class Meta:
        verbose_name = "Site Data"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.header_title}"

    def save(self, *args, **kwargs):
        self.header_image = compress_image(self.header_image, 95)
        return super(SiteData, self).save(*args, **kwargs)


def feed_upload_path(instance, filename):
    return f"feed_images/{instance.image_slug}/{filename}"


class Feed(MainAppBaseModel):
    image_slug = models.SlugField(editable=False)
    picture = models.ImageField(upload_to=feed_upload_path)
    description = models.TextField()
    display = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.image_slug}"

    def save(self, *args, **kwargs):
        self.picture = compress_image(self.picture, 60)
        if self.image_slug is None:
            self.image_slug = uuid.uuid4()
        return super(Feed, self).save()

    class Meta:
        verbose_name = "Feeds"
        verbose_name_plural = verbose_name
