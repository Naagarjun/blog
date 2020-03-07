from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.storage import default_storage as storage


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        mem_file = BytesIO()
        img = Image.open(self.image)
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size, Image.ANTIALIAS)
            img.save(mem_file, 'JPEG', quality=100)
            storage.save(self.image.name, mem_file)
            mem_file.close()
            img.close()
