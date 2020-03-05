from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.storage import default_storage as storage

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self):
        if not self.id and not self.project_description:
            return

        super(Projects, self).save()
        if self.project_thumbnail:
            size = 200, 200
            image = Image.open(self.project_thumbnail)
            image.thumbnail(size, Image.ANTIALIAS)
            fh = storage.open(self.project_thumbnail.name, "w")
            format = 'png'  # You need to set the correct image format here
            image.save(fh, format)
            fh.close()