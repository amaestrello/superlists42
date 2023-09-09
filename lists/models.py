from django.db import models

class Item(models.Model):
    text = models.CharField(max_length=200)  # Campo para o texto do item
    priority = models.CharField(max_length=20)  # Campo para a prioridade do item

    def __str__(self):
        return f"{self.text} ({self.priority})"
