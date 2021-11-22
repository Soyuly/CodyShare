

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='')),
                ('category1', models.CharField(max_length=20)),
                ('category2', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('cloth_type', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=10)),
                ('start', models.DateField(auto_now=True)),
                ('end', models.DateField(auto_now=True)),
                ('fee', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
    ]
