from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.TextField()
    company = models.TextField()
    cost_price = models.IntegerField(default='00000')

    def __str__(self):
        return self.name 
    

class inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    # def __str__(self):
    #     return self.product.name + " - " + str(self.quantity) 

class Sells(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sell_price = models.IntegerField()
    def __str__(self):
        return self.product.name  + " - " + str(self.quantity) + " - " + str(self.sell_price)

    def NewQuantity(self):
        return  inventory.quantity - self.quantity 