from django.db import models


# Create your models here.

def user_directory_path(instance, filename: str):
    return f"uploads/{instance.id}/{filename}"


class Post(models.Model):
    # BASE_DIR/media/uploads/
    photo = models.ImageField(upload_to=user_directory_path, default="")
    text = models.TextField()
    edit_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)
