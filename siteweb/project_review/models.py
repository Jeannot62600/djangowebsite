from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MinValueValidator, MaxValueValidator

@python_2_unicode_compatible
class Type(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
    def  __str__(self):
        return self.name

@python_2_unicode_compatible
class Project(models.Model):
    name_text_field = models.CharField(max_length=150,null=False, blank=False, default="NoName")
    maj_date = models.DateTimeField(null = False)
    picture = models.ImageField(upload_to='../media/images/', default='/home/meliodas/Documents/DUT/conf/kairos/prog/ico_kairos.png')
    types = models.ManyToManyField(Type)
    slug = models.SlugField()
    fini = models.BooleanField(null = False, blank= False, default=True)
    fiche = models.TextField(null = False, blank= False, default="No Fiche Yet")
    difficulty = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default = 0)
    class Meta:
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'
    def  __str__(self):
        return self.name_text_field
