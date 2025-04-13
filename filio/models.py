from django.db import models

# Create your models here.
# from django.db import models

# from django.db import models

from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to="Resumes/")

    def __str__(self):
        return self.name if self.name else "Unnamed Resume"