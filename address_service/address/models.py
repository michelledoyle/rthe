from django.db import models


class Address(models.Model):
    address_id = models.CharField(max_length=36, primary_key=True, db_column='AddressID')
    patient_id = models.CharField(max_length=36, db_column='PatientID')  # Foreign key logic is removed
    address_line1 = models.CharField(max_length=255, db_column='AddressLine1', blank=True, null=True)
    address_line2 = models.CharField(max_length=255, db_column='AddressLine2', blank=True, null=True)
    city = models.CharField(max_length=100, db_column='City', blank=True, null=True)
    state = models.CharField(max_length=50, db_column='State', blank=True, null=True)
    zip_code = models.CharField(max_length=20, db_column='ZipCode', blank=True, null=True)

    class Meta:
        db_table = 'PatientAddress'

    def __str__(self):
        return f'{self.address_line1}, {self.city}'
