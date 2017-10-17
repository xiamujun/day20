from django.db import models

# Create your models here.

class Foo(models.Model):
    name = models.CharField(max_length=12)
    def __str__(self):
        return self.name


class Business(models.Model):
    #id
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32,null=True,default='Z001')
    # test = models.CharField(max_length=32,db_column='测试',null=True)
    # fk = models.ForeignKey('Foo') #默认和主键关联
    def __str__(self):
        return self.caption


class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(protocol='ipv4',db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey('Business',to_field='id')

    def __str__(self):
        return self.hostname