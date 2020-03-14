from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
# from django_comments.moderation import CommentModerator
# from django_comments_xtd.moderation import moderator, SpamModerator


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default='', max_length=255)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs={'pk': self.pk,
                'slug':self.slug 
                }
        return reverse('post-detail', kwargs= kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode = True)
        super().save(*args, **kwargs)

# class PostCommentModerator(CommentModerator):
#     email_notification = True
#     auto_moderate_field = 'publish'
#     moderate_after = 365

# moderator.register(Post, PostCommentModerator)
