from django_seed import Seed
from .models import Department, Group
seeder=Seed.seeder()
seeder.add_entity(Department, 5)
seeder.add_entity(Group, 10)
inserted_pks = seeder.execute()