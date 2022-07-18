#
# from django.db import models
#
# # Create your models here.
# class District(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
# class ServiceAcctype(models.Model):
#     name = models.CharField(max_length=250)
#
#     def __str__(self):
#         return self.name
#
#
# class Branch(models.Model):
#     district=models.ForeignKey(District,on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
# class Banking(models.Model):
#     name = models.CharField(max_length=250)
#     email = models.CharField(max_length=250)
#     date_of_birth = models.DateField()
#     mobile = models.IntegerField()
#     address = models.TextField()
#     district = models.ForeignKey(District,on_delete=models.SET_NULL,blank=True,null=True)
#     branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,blank=True,null=True)
#     account_type = models.ForeignKey(ServiceAcctype,on_delete=models.CASCADE)
#     chequebook = models.BooleanField(default=False)
#     netbanking = models.BooleanField(default=False)
#     passbook = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.name