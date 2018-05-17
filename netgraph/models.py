
from django.db import models
from django.utils.translation import ugettext as _, ugettext_lazy


#0222_bikemap_crawaler
class Bikestatus(models.Model):
    #id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=30, default="")
    station_number = models.IntegerField(
        default= 0,
        null = False
    )
    available_bike = models.IntegerField(
        default= 0,
        null = False
    )
    all_dock = models.IntegerField(
        default= 0,
        null = False
    )
    using_dock = models.IntegerField(
        default= 0,
        null = False
    )
    available_dock = models.IntegerField(
        default=0,
        null=False
    )
    #is_new = models.BooleanField(default=False)

