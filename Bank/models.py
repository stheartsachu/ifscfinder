from django.db import models

# Create your models here.
class banks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, default="", max_length=200)
    def __str__(self):
        st = "%s - %s" % (self.id, self.name)
        return st
class Branch(models.Model):
    ifsc = models.CharField(unique=True, max_length=20, default="", null=True)
    bank = models.ForeignKey(banks, on_delete=models.CASCADE, default="", null=True)
    branch =models.CharField(max_length=100, default="", null=True)
    address = models.CharField(max_length=200, default="", null=True)
    city = models.CharField(max_length=100, default="", null=True)
    district = models.CharField(max_length=50, default="", null=True)
    state = models.CharField(max_length=50, default="", null=True)
    def __str__(self):
        st = "%s - %s" % (self.branch, self.ifsc)
        return st

