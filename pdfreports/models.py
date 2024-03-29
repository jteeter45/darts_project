from django.db import models

class Pdfreport(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)
