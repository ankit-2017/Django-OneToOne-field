from django.db import models



from django.contrib.auth.models import User

class Emp(models.Model):
    user = models.OneToOneField(User)
    department = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return self.user.username
# Create your models here.
