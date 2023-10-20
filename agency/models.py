from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("agency:redactor-detail", kwargs={"pk": self.pk})


class Article(models.Model):
    title = models.CharField(max_length=127, unique=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(to=Topic, on_delete=models.DO_NOTHING)
    publishers = models.ManyToManyField(to=Redactor, related_name="articles")

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("agency:article-detail", kwargs={"pk": self.pk})
