from django.db import migrations

def create_data(apps, schema_editor):
    Welearner = apps.get_model('welearner', 'Welearner')
    Welearner(first_name="Welearner 001", last_name="Welearner 001", email="customer001@email.com", phone="00000000", address="Welearner 000 Address", description= "Welearner 001 description").save()

class Migration(migrations.Migration):
    dependencies = [
    ('welearner', '0001_initial'),
	                ]
    operations = [
	migrations.RunPython(create_data),
	            ]        