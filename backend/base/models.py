from django.db import models
from backend.settings import AUTH_USER_MODEL


class Toner (models.Model):
    type = models.CharField(max_length=30)
    date_entree = models.DateField()
    quantite_entree = models.CharField(max_length=30)
    date_sortie = models.DateField()
    quantite_sortie = models.CharField(max_length=30)
    stock_initial= models.CharField(max_length=30)
    stock_reel= models.CharField(max_length=30)
    stock_provisionnel= models.CharField(max_length=30)
    prix = models.DecimalField(decimal_places=2, max_digits=10)
    user= models.CharField(max_length=30)
    observation= models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Reservation (models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    toner = models.ForeignKey(Toner,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} {self.toner.type}"




