from django.db import models
from tag import Tag
from image import Image

class ImageTag(models.Model):
	image = models.ForeignKey(Image)
	tag = models.ForeignKey(Tag)