from django.db import models

CATEGORY_CHOICES = [
    ('electronics', 'Electronics'),
    ('furniture', 'Furniture'),
    ('stationery', 'Stationery'),
    ('other', 'Other'),
]

LOCATION_CHOICES = [
    ('office', 'Office'),
    ('warehouse', 'Warehouse'),
    ('lab', 'Lab'),
    ('other', 'Other'),
]

CONDITION_CHOICES = [
    ('new', 'New'),
    ('good', 'Good'),
    ('fair', 'Fair'),
    ('poor', 'Poor'),
]

ASSIGNED_TO_CHOICES = [
    ('john', 'John'),
    ('jane', 'Jane'),
    ('team_a', 'Team A'),
    ('team_b', 'Team B'),
    ('other', 'Other'),
]

class Inventory(models.Model):
    name = models.CharField(max_length=255, default="null")
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='other')
    ser_number = models.CharField(verbose_name='Serial numbers', default="null", max_length=255)
    tag_number = models.CharField(verbose_name='Tag numbers', default="null", max_length=255)
    quantity = models.IntegerField(verbose_name='Quantity', default=1)
    description = models.TextField(verbose_name="Description", max_length=800, default="null")
    location = models.CharField(verbose_name='Item present location', max_length=255, choices=LOCATION_CHOICES, default='other')
    d_o_p = models.DateField(verbose_name='Date Of Purchase (YYYY-MM-DD)', null=True, blank=True)
    purchase = models.DecimalField(verbose_name='Purchased price', null=True, blank=True, max_digits=10, decimal_places=2)
    vendor = models.CharField(verbose_name='Seller', default="null", max_length=255)
    receipt = models.ImageField(verbose_name='Receipt', upload_to='receipts/', null=True, blank=True)
    condition = models.CharField(verbose_name='Asset condition', max_length=50, choices=CONDITION_CHOICES, default='good')
    assigned_to = models.CharField(verbose_name='Assigned to who?', max_length=255, choices=ASSIGNED_TO_CHOICES, default='other')
    intended_usage = models.CharField(verbose_name='Purpose of assigned item', default="null", max_length=255)
    additional_notes = models.TextField(verbose_name='Additional notes', default="null", max_length=800)

    def __str__(self):
        return f"{self.name} - Assigned to: {self.assigned_to}"