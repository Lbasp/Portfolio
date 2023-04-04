from django.db import models

# Create your models here.


class Project(models.Model):
    #Descriptions
    title = models.CharField(max_length=200)
    summary = models.TextField()

    #Links
    page_url = models.URLField(max_length=200)
    gif_url = models.URLField(max_length=200)

    ##Atributes
    SQL = models.BooleanField(default=False)
    Machine_Learning = models.BooleanField(default=False)
    Team_Work = models.BooleanField(default=False)
    State_of_art = models.BooleanField(default=False) 
    Analysis = models.BooleanField(default=False)
    Data_Mining = models.BooleanField(default=False)


    area_choices = [
        ('DS', 'Data Science'),
        ('PD', 'Product Development'),
        ('RS', 'Physics'),
    ]
    #
    area = models.CharField(
        max_length=2,
        choices=area_choices,
    )
    def __str__(self) -> str:
        return self.title

