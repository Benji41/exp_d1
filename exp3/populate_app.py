import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','exp3.settings')
import django
django.setup()

##FAKE POP SCRIPT
import random
from app.models import Cat,Owner,AccessRecord
from faker import Faker
fakegen = Faker()
gatos = ['gardfield','felix','gato con botas','gatiato','don gato']

def addCat():
    cat = Cat.objects.get_or_create(catName=random.choice(gatos))[0]
    cat.save()
    return cat

def populate(N=5):
    for entry in range(N):
        #create cat
        cat = addCat()
        #create owner
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name= fakegen.company()

        owner = Owner.objects.get_or_create(
            #foreign key reads an object
            ownName=fake_name,ownCat=cat,ownPhoto=fake_url)[0]
        #create access record
        acc_rec= AccessRecord.objects.get_or_create(arName=owner,arDate= fake_date)[0]
        
       

if __name__ == "__main__":
    print('populating script!')
    populate(10)
    print('done')