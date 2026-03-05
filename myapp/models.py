from django.db import models

class Books(models.Model):
    book_name=models.CharField(max_length=255,verbose_name="Kitabyn ady")
    author=models.CharField(max_length=255,verbose_name="Awtory")
    page_volume=models.IntegerField(max_length=10,verbose_name="Sahypa sany")
    published_date=models.DateField(verbose_name="Neshir edilen senesi")

    def __str__(self):
        return self.book_name

    class Meta():
        verbose_name="kitap"
        verbose_name_plural="kitaplar"
