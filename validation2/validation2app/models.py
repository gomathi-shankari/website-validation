from django.db import models

# Create your models here.

Static_link=(
  ('https://www.github.com', 'https://www.github.com'),
  ('https://www.geeksforgeeks.org', 'https://www.geeksforgeeks.org'),
  ('https://www.tutorialspoint.com', 'https://www.tutorialspoint.com'),
)
class link(models.Model):
    Static_ID = models.CharField(max_length=100, choices=Static_link)
    Dynamic_ID = models.CharField(max_length=500)

