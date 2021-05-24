from django.db import models

class Neo(models.Model):
    neo_reference_id = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=700, blank=False, default='', unique=True)
    created = models.DateTimeField(auto_now_add=True)
    nasa_jpl_url = models.URLField(unique=True)
    is_potentially_hazardous_asteroid = models.BooleanField(default=False)
   

    class Meta:
        ordering = ('name',)




