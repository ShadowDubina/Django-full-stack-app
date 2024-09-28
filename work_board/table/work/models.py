from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.conf import settings


professions = (
    ('automobile business', 'automobile business'),
    ('administrative staff', 'administrative staff'),
    ('senior and middle management', 'senior and middle management'),
    ('raw material extraction', 'raw material extraction'),
    ('advertising and marketing', 'advertising and marketing'),
    ('medicine and pharmaceuticals', 'medicine and pharmaceuticals'),
    ('sales and customer service', 'sales and customer service'),
    ('sport club and fitness', 'sport club and fitness'),
    ('science and education', 'science and education'),
    ('personnel management', 'personnel management'),
)

Experience = (
    ('no experience', 'no experience'),
    ('1 to 3 years', '1 to 3 years'),
    ('3 to 6 years', '3 to 6 years'),
    ('6 to 12 years', '6 to 12 years'),
    ('from 15 years', 'from 15 years')
)

choice = (
    ('yes', 'yes'),
    ('no', 'no')
)

class Announcement(models.Model):
    category = models.CharField(choices=professions, blank=False, max_length=100)
    title = models.CharField(max_length=40, blank=False)
    slug = models.SlugField(max_length=250, unique_for_date='publish', )
    price = models.IntegerField(default=None, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announcement_work')
    publish = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500, blank=False)
    company = models.CharField(max_length=30, blank=False)
    experience = models.CharField(choices=Experience, blank=False, max_length=100)
    address = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=30, blank=False)

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('account:announcement_detail', args=[self.publish.year,
                                                            self.publish.month,
                                                            self.publish.day,
                                                            self.slug])

    tags = TaggableManager()

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=30, blank=False)
    category = models.CharField(choices=professions, blank=False, max_length=100)
    description = models.TextField(max_length=500, blank=False)
    experience = models.CharField(choices=Experience, blank=False, max_length=100)


    def __str__(self):
        return f'Profile of {self.user.username}'
