import os

from django.db import models
from django.urls import reverse_lazy


class task(models.Model):
    title = models.CharField(max_length=20, verbose_name='Задание')
    text = models.TextField(blank=True, verbose_name='Описание задания')
    in_date = models.DateTimeField(verbose_name='Дата начала')
    out_date = models.DateTimeField(blank=True, verbose_name='Дата окончания')

    def __str__(self):
        return f'Задача {self.pk}'

    def get_absolute_url(self):
        return reverse_lazy('task', kwargs={"task_id": self.pk})

    def get_edit_url(self):
        return reverse_lazy('task_edit', kwargs={"task_id": self.pk})

    def get_delete_url(self):
        return reverse_lazy('task_delete', kwargs={"task_id": self.pk})


class file(models.Model):
    task_id = models.ForeignKey('task', on_delete=models.CASCADE)
    path = models.FileField(upload_to='uploads/%Y/%m/%d')

    def get_filename(self):
        return os.path.basename(self.path.name)

    def get_delete_url(self):
        return reverse_lazy('file_delete', kwargs={"file_id": self.pk})
