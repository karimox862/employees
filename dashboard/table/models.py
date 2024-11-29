from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    start_date = models.DateField(null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"
