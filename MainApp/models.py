from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

LANG_CHOICE = {
    ("py", "Python"),
    ("cpp", "C++"),
    ("js", "JavaScript"),
    ("c#", "C#"),
    ("php", "PHP"),
}


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANG_CHOICE)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="comments")
    is_private = models.BooleanField(default=False)

    # def __repr__(self):
    #     return f"S: {self.name} {self.author}"

    # def __str__(self):
    #     return self.__repr__()


class Comment(models.Model):
    text = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE, related_name="comments")
    image = models.ImageField(upload_to='images', null=True, blank=True)
