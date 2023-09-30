from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Ady')
    content = models.TextField(blank=True, verbose_name='Mazmuny')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Wagty')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Tazelenen')
    photo = models.ImageField(upload_to='photos/%Y/%d/%m', verbose_name='Surat', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Goylanmy?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 verbose_name='Kategoriyalar')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Habarnama'
        verbose_name_plural = 'Habarnamalar'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Kategoriyalary atlandyrma')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        ordering = ['-title']
