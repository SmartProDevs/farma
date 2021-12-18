from django.db import models


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=300)
    dekan_name = models.CharField(max_length=300)

    def __str__(self):
        return self.faculty_name
