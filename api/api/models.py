from django.db import models


class ImportedFile(models.Model):
    file = models.FileField(upload_to='imported_files/')
    structure = models.JSONField()

    def __str__(self):
        return self.file.name

    class Meta:
        app_label = 'api'
