from django.db import models

# Create your models here.
class user_info(models.Model):
    uname = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)

    def __str__(self):
        return self.uname

class services(models.Model):
    service_name=models.CharField(max_length=50)
    service_id=models.CharField(max_length=50)

    def __str__(self):
        return self.service_name

class sub_services(models.Model):
    subservice_name=models.CharField(max_length=100)
    subservice_id=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/',null=True, blank=True)
    service_id=models.ForeignKey(services,on_delete=models.CASCADE)

    def __str__(self):
        return self.subservice_name

class bookings(models.Model):
    booking_time = models.DateTimeField()
    from_date=models.DateField()
    to_date=models.DateField()
    user_id = models.ForeignKey(user_info, on_delete=models.CASCADE)
    service_id=models.ForeignKey(services,on_delete=models.CASCADE)
    subservice_id=models.ForeignKey(sub_services,on_delete=models.CASCADE)
    price = models.CharField(max_length=50)

    # def save(self, *args, **kwargs):
    #     if self.subservice_id:
    #         self.price = self.subservice_id.price
    #     super().save(*args, **kwargs)