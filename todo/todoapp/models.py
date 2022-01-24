from django.contrib.auth.models import User
from django.db import models



class Todo(models.Model):
    s = (
        ("yangi", "yangi"),
        ('bajarildi', 'bajarildi')
    )
    sarlavha = models.CharField(max_length=200)
    batafsil = models.CharField(max_length=300)
    status = models.CharField(max_length=50, choices=s)
    vaqt = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.batafsil},{self.vaqt},{self.status}"

