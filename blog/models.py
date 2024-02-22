from django.db import models


# Create your models here.

def user_directory_path(instance, filename: str):
    return f"uploads/{instance.id}/{filename}"


class Post(models.Model):
    # BASE_DIR/media/uploads/
    title = models.CharField(default="", max_length=30)
    text = models.TextField()
    edit_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=user_directory_path, default="")

    def __str__(self):
        local_date = self.creation_date.astimezone()
        formatted_date = local_date.strftime("%Y-%m-%d (%H:%M)")
        return f"{formatted_date} ({self.id})"
