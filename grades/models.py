from django.db import models



class Resort(models.Model):
    resortname_text = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    def __str__(self):              # __unicode__ on Python 2
        return self.resortname_text

class Grade(models.Model):
    resort = models.ForeignKey(Resort)
    grade_decimal = models.DecimalField(max_digits=2, decimal_places=1)
    forecast_date = models.DateTimeField('date forecast') 
    def __str__(self):              # __unicode__ on Python 2
        return str(self.grade_decimal)