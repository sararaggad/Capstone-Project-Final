from django.db import models

# Create your modefrom django.db import models

class Car(models.Model):
    TRANSMISSION = (('auto','Automatic'), ('manual','Manual'))
    STATUS = (('available','Available'), ('maintenance','Maintenance'))

    title = models.CharField(max_length=120)
    brand = models.CharField(max_length=80)
    model_year = models.PositiveIntegerField()
    daily_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=12, choices=STATUS, default='available')
    plate_no = models.CharField(max_length=20, unique=True)
    seats = models.PositiveSmallIntegerField(default=4)
    transmission = models.CharField(max_length=6, choices=TRANSMISSION, default='auto')
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.brand} {self.title} {self.model_year}"
