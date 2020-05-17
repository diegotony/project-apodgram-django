from django.db import models


class Author(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Image(models.Model):
    copyright = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='images')
    # owner = models.ForeignKey('auth.User', related_name='images', on_delete=models.CASCADE)
    date = models.DateTimeField()
    data_save = models.DateTimeField(auto_now=True)
    explanation = models.TextField()
    hdurl = models.TextField()
    url = models.TextField()
    media_type = models.TextField()
    service_version = models.CharField(max_length=10)
    title = models.TextField()
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


