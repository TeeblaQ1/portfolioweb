from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    subject = models.CharField(max_length=256)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.name + "-" + self.email
