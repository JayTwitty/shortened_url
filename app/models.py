from django.db import models

# Create your models here.


class Bookmark(models.Model):
    input_url = models.URLField()
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    output_url = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}, {}".format(self.input_url, self.output_url)

    class Meta:
        ordering = ["-timestamp"]



class Click(models.Model):
    bookmark = models.DateTimeField()
    count = models.ForeignKey(Bookmark)

