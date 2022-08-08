from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
# Create your models here.


class UserImage(models.Model):
    userid = ForeignKey(User, on_delete=DO_NOTHING)
    imgcaption = CharField(max_length=230, default="Profile Picture")
    userimage = ImageField(upload_to ="profile_pics/")

    def __str__(self) -> str:
        return self.imgcaption