from django.db import models

class datos_uma(models.Model):
    id_uma = models.AutoField(primary_key=True)
    time = models.CharField(max_length=10)
    uma = models.IntegerField()
    lat = models.DecimalField(max_digits=13, decimal_places=10)
    lon = models.DecimalField(max_digits=13, decimal_places=10)
    mp01 = models.IntegerField()
    mp25 = models.IntegerField()
    mp10 = models.IntegerField()
    d03 = models.IntegerField()
    d05 = models.IntegerField()
    d01 = models.IntegerField()
    d25 = models.IntegerField()
    d50 = models.IntegerField()
    d10 = models.IntegerField()
    vel = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{id_uma: %s,time: %s, uma: %s,lat: %s,lon: %s,mp01: %s,mp25: %s,mp10: %s,d03: %s,d05: %s,d01: %s,d25: %s,d50: %s,d10: %s,vel: %s}" %(self.id_uma,self.time,self.uma,self.lat,self.lon,self.mp01,self.mp25,self.mp10,self.d03,self.d05,self.d01,self.d25,self.d50,self.d10,self.vel)