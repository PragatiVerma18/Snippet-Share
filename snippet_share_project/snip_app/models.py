from django.db import models
from django.core.validators import RegexValidator
from django import forms

class Snip(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    title=models.CharField(max_length=40, default="Untitled")
    text=models.TextField()
    link_code=models.CharField(max_length=8,unique=True, validators=[alphanumeric])
    langs=[('text','None'),('c','C'),('cpp','C++'),('csharp','C#'),('java','Java'),('js','JavaScript'),('php','PHP'),('py','Python'),('sql','SQL')]
    lang=models.CharField(max_length=10, choices=langs, default='text')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link_code+" : "+self.text[:20]