from django.db import models

# Create your models here.
#& make any changes in the databse or add new stuff always run the python manage.py migrate to make sure the changes reflect in the migrations and other areas
class PageVisit(models.Model):
    #? db -> table, will create three columns
    #! id (hidden)-> primary key -> autofield -> 1, 2, 3, 4, 5
    path = models.TextField(blank=True ,null=True) #?col
    timestop = models.DateTimeField(auto_now_add=True) #?col
    