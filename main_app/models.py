from django.db import models


class MainAppBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SiteData(MainAppBaseModel):
    header_title = models.CharField(max_length=100, default="Header title here")
    header_message = models.TextField(default="put intro here")
    instagram_link = models.URLField()

    class Meta:
        verbose_name = "Site Data"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.header_title}"
