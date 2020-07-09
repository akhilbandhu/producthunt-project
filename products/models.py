from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to = 'images/')
    url = models.TextField()
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, db_column='hunter', default=0)

    def pub_date_pretty(self):      #makes date pretty, look up strftime references
        return self.pub_date.strftime( '%b %e %Y' )

    def __str__(self):              #shows title of blog in database instead of blog object
        return self.title

    def summary(self):              #doesn't show whole blog, first 100 characters
        return self.body[:100]
