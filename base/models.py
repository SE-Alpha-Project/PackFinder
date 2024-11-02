from django.db import models
from django.contrib.auth.models import User

class CompatibilityQuestion(models.Model):
    question = models.CharField(max_length=200)
    choices = models.JSONField()

    def __str__(self):
        return self.question

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(CompatibilityQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=50)

    class Meta:
        unique_together = ['user', 'question'] 