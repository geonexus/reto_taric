from django.db import models

class author_data(models.Model):
    name = models.CharField(max_length=50)
    id = models.CharField(max_length=50, primary_key=True)

class Book(models.Model):
    summary = models.CharField(max_length=500)
    book_id = models.CharField(max_length=500)
    lcc_number = models.CharField(max_length=500)
    publisher_name = models.CharField(max_length=500)
    isbn10 = models.CharField(max_length=10)
    publisher_text = models.CharField(max_length=500)
    language = models.CharField(max_length=500)
    title_latin = models.CharField(max_length=500)
    publisher_id = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)
    isbn13 = models.CharField(max_length=13, primary_key=True)
    dewey_decimal = models.CharField(max_length=10)
    dewey_normal = models.CharField(max_length=1)
    title_long = models.CharField(max_length=500)
    urls_text = models.CharField(max_length=500)
    awards_text = models.CharField(max_length=500)
    marc_enc_level = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    title_long = models.CharField(max_length=500)
    author_data =  models.ForeignKey(author_data, on_delete=models.CASCADE)


