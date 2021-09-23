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
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __repr__(self):
        return f"S: {self.name} {self.author.username}"
