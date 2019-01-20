import uuid

from django.db import models

# Create your models here.
from rest_framework import serializers, generics


class Tag(models.Model):
    tag = models.CharField(primary_key=True, max_length=32)

    def __str__(self):
        return self.tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag')


class News(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
        ('OTH', 'Other')
    )

    title = models.CharField(max_length=128)
    date = models.DateTimeField()
    image = models.ImageField()
    text = models.CharField(max_length=2048)
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH')
    url = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True, editable=False, auto_created=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('date',)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'date', 'image', 'text', 'field', 'tags')
        depth = 1


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
