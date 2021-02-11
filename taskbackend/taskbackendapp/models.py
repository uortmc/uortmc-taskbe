from django.db.models import *
from django.contrib.auth.models import User
from django.utils.timezone import now
import uuid

class Scan(Model):
    ALGORITHMS = [
        ('NS', 'NOT SET'),
        ('SVC', 'Simple Support Vector Machine')
    ]
    token = UUIDField('Scan Token',unique=True, default=uuid.uuid4, editable=False)
    algorithm=CharField('Algorithm Used',max_length=10,choices=ALGORITHMS,default=ALGORITHMS[0][0])


    def __str__(self):
        return "Scan "+str(self.token)
