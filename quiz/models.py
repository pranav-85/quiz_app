from django.db import models

# Create your models here.
class Questions(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=255, decimal_places=0)
    question = models.CharField(max_length=255)
    choice_1 = models.CharField(max_length=255)
    choice_2 = models.CharField(max_length=255)
    choice_3 = models.CharField(max_length=255)
    choice_4 = models.CharField(max_length=255)
    answer = models.DecimalField(max_digits=1, decimal_places=0)

    def __str__(self):
        return f"Question: {self.question} - Correct Choice: {str(self.answer)}"
