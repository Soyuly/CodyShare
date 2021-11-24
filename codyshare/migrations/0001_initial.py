
import datetime
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
                ('img', models.ImageField(upload_to='img/')),
                ('gender', models.CharField(max_length=20)),
                ('cloth_type', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=10)),
                ('start', models.DateField(auto_now=True)),
                ('end', models.DateField(auto_now=True)),
                ('fee', models.IntegerField()),
                ('state', models.BooleanField(default=0)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_start', models.CharField(max_length=200)),
                ('rent_end', models.CharField(max_length=200)),
                ('state', models.IntegerField(default=1)),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codyshare.post')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codyshare.post')),
                ('recieve_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recieve', to='account.account')),
                ('send_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='send', to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codyshare.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
    ]
