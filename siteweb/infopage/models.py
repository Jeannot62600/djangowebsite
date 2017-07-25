from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# from embed_video.fields import EmbedVideoField
import random
import string

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

@python_2_unicode_compatible
class Info(models.Model):
    title = models.CharField(max_length=150,null=False, blank=False, default="NoName")
    maj_date = models.DateTimeField(null = False)
    slug = models.CharField(max_length=6, unique=True, default=rand_slug())
    picture = models.ImageField(upload_to='../media/images/', null = True, blank= True)
    fiche = models.TextField(null = False, blank= False, default="No Fiche Yet")
    private = models.BooleanField(null = False, blank= False, default=True)
    # video = EmbedVideoField(null = True, Blank= True)
    class Meta:
        verbose_name = 'Page d\'information'
        verbose_name_plural = 'Pages d\'information'
    def  __str__(self):
        return self.title
