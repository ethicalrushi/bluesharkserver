from django.db import models

# Create your models here.

qualityLevel = (
    ('1', 'low'),
    ('2', 'medium'),
    ('3', 'high')
)

class User(models.Model):
    user_roles = (
        ('CUST', 'customer'),
        ('ADMN', 'admin')

    )
    
    name = models.CharField(max_length=200, unique=True)
    waterMeterNo = models.CharField(max_length=15, unique=True, null=True, blank=True)
    userId = models.IntegerField(unique=True)
    role = models.CharField(choices=user_roles, default='CUST', max_length=4)
    tapNode = models.OneToOneField('Node', related_name='tapnode', on_delete=models.CASCADE)
    path = models.ManyToManyField('Node', related_name="path")
    qualtiyLevel = models.CharField(choices=qualityLevel, default='M', max_length=1)
    createdAt = models.DateTimeField(auto_now=True)
    modifiedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Node(models.Model):
    pH = models.FloatField()
    turbidity = models.FloatField()
    conductivity = models.FloatField()
    temperature = models.FloatField()
    nodeId = models.IntegerField(unique=True)
    status  = models.BooleanField(default=True)
    qualityLevel = models.CharField(choices=qualityLevel, default='2', max_length=1)
    createdAt = models.DateTimeField(auto_now=True)
    modifiedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.status)


    