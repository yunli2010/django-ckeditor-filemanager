from django.db import models

class ReferenceContent(models.Model):
    title = models.CharField(max_length=255)
    reference = models.SlugField(max_length=255)
    display = models.BooleanField(default=True, blank=True)
    content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Reference Content"

    def __unicode__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    display = models.BooleanField(default=True, blank=True)
    content = models.TextField(null=True, blank=True)

    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.CharField(max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Page"

    def __unicode__(self):
        return self.title


class SEOMetatag(models.Model):
    TYPE_CHOICES = (
        ('global', 'Global'),
        ('contact', 'Contact'),
    )
    display_type = models.CharField(max_length=30, choices=TYPE_CHOICES, unique=True)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.CharField(max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "SEO Metatag"

    def __unicode__(self):
        return self.meta_title
