from django.db import models
from django.urls import reverse



class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, max_length=250, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактора')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('views_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-title']


class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Наименование категорий')
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
    ordering = ['title' ]

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})


    def __str__(self):
        return self.title

    

