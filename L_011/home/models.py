from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Thread(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads')
    title = models.CharField(max_length=255)
    content = models.TextField()
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    last_activity = models.DateTimeField(default=timezone.now)
    reports = models.IntegerField(default=0)
    bookmarks = models.ManyToManyField(User, related_name='bookmarked_threads', blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.views})"

    def up_vote(self):
        self.up_votes += 1
        self.score = self.up_votes - self.down_votes
        self.save()

    def down_vote(self):
        self.down_votes += 1
        self.score = self.up_votes - self.down_votes
        self.save()

    def update_last_activity(self):
        self.last_activity = timezone.now()
        self.views += 1
        self.save()

    def report(self):
        self.reports += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Thread, self).save(*args, **kwargs)