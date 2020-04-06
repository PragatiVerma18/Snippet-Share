from django.db import models

class Upload(models.Model):
    file = models.FileField(upload_to="uploads")

    def __unicode__(self):
        return self.file.name
