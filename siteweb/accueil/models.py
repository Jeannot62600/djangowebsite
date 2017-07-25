from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Part(models.Model):
    title = models.CharField(max_length=150,null=False, blank=False, default="NoName")
    slug = models.SlugField(null = False, blank = False)
    picture = models.ImageField(upload_to='../media/images/', null = True, blank= True)

    class Meta:
        verbose_name = 'Partie du site'
        verbose_name_plural = 'Parties du site'
    def  __str__(self):
        return self.title
