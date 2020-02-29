from django.db import models

# Create your models here.

qualityLevel = (
    ('L', 'low')
    ('M', 'medium')
    ('H', 'high')
)

class User(models.Model):
    user_roles = (
        ('CUST', 'customer'),
        ('ADMN', 'admin')

    )
    
    name = models.CharField(max_length=200, unique=True)
    waterMeterNo = models.CharField(max_length=15, unique=True, null=True, blank=True)
    userId = models.IntegerField(unique=True)
    role = models.CharField(choices=user_roles, default='CUST')
    path = models.ManyToManyField(Node, related_name=path, on_delete=models.CASCADE)
    qualtiyLevel = models.CharField(choices=qualityLevel, default='M')
    createdAt = models.DateTimeField(auto_now=True)
    modifiedAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return name


class Node(models.Model):
    pH = models.FloatField(max=14)
    turbidity = models.FloatField()
    conductivity = models.FloatField()
    temperature = models.FloatField()
    nodeId = models.IntegerField(unique=True)
    status  = models.BooleanField(default=True)
    qualtiyLevel = models.CharField(choices=qualityLevel, default='M')
    createdAt = models.DateTimeField(auto_now=True)
    modifiedAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return status

    