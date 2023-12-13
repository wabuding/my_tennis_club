from django.db import models

class Court(models.Model):
  courtname = models.CharField(max_length=255)
  courttype = models.CharField(max_length=255)
  city = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.courtname} {self.courttype} {self.city}"