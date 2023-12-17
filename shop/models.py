from django.db import models

# Create your models here.
#카테고리
#사진
#상품명
#가격
#설명

class Shop(models.Model) :
    category = models.CharField(max_length=10, default='')
    image = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    content = models.TextField()






