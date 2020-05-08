from django.db import models

# Create your models here.


class Article(models.Model):
    article_meta = models.CharField('Заголовок', max_length=50, null=True, blank=True)
    article_title = models.CharField('Название статьи', max_length=100)
    article_text = models.TextField('Текст статьи')
    pub_date = models.TextField('Дата публикации')  # TextField для русского отображения даты.
    article_image = models.ImageField(null=False, blank=True, upload_to='article_image')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):  # надо не совсем
        pass

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
