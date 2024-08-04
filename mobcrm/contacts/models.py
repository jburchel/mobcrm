from django.db import models

class Contact(models.Model):
    CONTACT_TYPES = (
        ('individual', 'Individual'),
        ('church', 'Church'),
    )
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CONTACT_TYPES)    
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    last_contact = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
