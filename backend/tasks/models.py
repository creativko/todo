from django.db import models


class Task(models.Model):
    """Задания"""
    CHOICES = (
        ('open', 'Открыта'),
        ('close', 'Закрыта')
    )
    content = models.TextField(verbose_name='Описание')
    status = models.CharField(verbose_name='Статус', choices=CHOICES, default='open', max_length=20)
    published = models.BooleanField(default=True, verbose_name='Публиковать')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Задание'
        verbose_name_plural = 'Задании'

    def __str__(self):
        return self.content[:40]
