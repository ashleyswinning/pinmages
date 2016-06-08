from django.db import models

class Image(models.Model):
	svg_data = models.TextField()
	name = models.CharField(max_length = 30)
	description = models.TextField()

	# TO DO-
	# MAKE USER MODEL !
