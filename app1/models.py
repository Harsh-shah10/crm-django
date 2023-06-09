from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'Tag'

    def __str__(self):
        return self.name
    
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=20, null=True, blank=True)
    instructor_name = models.CharField(max_length=255)
    course_tags = models.ManyToManyField(Tag)
    original_course_link = models.URLField(max_length=200)
    download_link = models.URLField(max_length=200)
    course_image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'Course'

    def __str__(self):
        return f"{self.course_name}"