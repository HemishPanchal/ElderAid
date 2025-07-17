from django.db import models

# Create your models here.
class user_info(models.Model):
    uname = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)

    def __str__(self):
        return self.uname

class services(models.Model):
    service_name=models.CharField(max_length=50,verbose_name="Service Name")
    service_id=models.CharField(max_length=50)

    def __str__(self):
        return self.service_name

class sub_services(models.Model):
    subservice_name=models.CharField(max_length=100,verbose_name="Subservice Name")
    subservice_id=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/',null=True, blank=True)
    service_id=models.ForeignKey(services,on_delete=models.CASCADE)

    def __str__(self):
        return self.subservice_name

class bookings(models.Model):
    booking_time = models.DateTimeField(verbose_name="Booking Time")
    from_date=models.DateField(verbose_name="From Date")
    to_date=models.DateField(verbose_name="To Date")
    user_id = models.ForeignKey(user_info, on_delete=models.CASCADE,verbose_name="User Name")
    service_id=models.ForeignKey(services,on_delete=models.CASCADE,verbose_name="Service")
    subservice_id=models.ForeignKey(sub_services,on_delete=models.CASCADE,verbose_name="Subservice")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Price")

    