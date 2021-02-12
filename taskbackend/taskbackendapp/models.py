from django.db.models import *

import uuid

class Scan(Model):
    ALGORITHMS = [
        ('NS', 'NOT SET'),
        ('SVC', 'Simple Support Vector Machine')
    ]
    token = UUIDField('Scan Token',unique=True, editable=False)
    algorithm=CharField('Algorithm Used',max_length=10,choices=ALGORITHMS,default=ALGORITHMS[0][0])
    results=TextField('Algorithm Text Output',max_length=300,default="Not Set")

    def __str__(self):
        return "Scan "+str(self.token)