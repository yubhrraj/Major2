from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Kid(models.Model):
    
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    thana_code = models.CharField(max_length=6)
    parent_name = models.CharField(max_length=200)
    parent_contact = models.PositiveIntegerField(primary_key = True, validators=[MaxValueValidator(9999999999)])
    image = models.ImageField(upload_to = 'Image/Saved', default = 'Image/None/No-img.jpg')

    def __str__(self):
        return str(self.parent_contact)

class RecvData(models.Model):

    address = models.CharField(max_length = 500,null = True, blank = True)
    contact_det = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    loc_long = models.DecimalField(max_digits=12, decimal_places=9)
    loc_lat = models.DecimalField(max_digits=12, decimal_places=9)
    img = models.ImageField(upload_to = 'Image/clientUpload', default = 'Image/None/No-img.jpg')

    def __str__(self):
        return str(self.contact_det)
