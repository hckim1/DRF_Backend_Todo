# Generated by Django 3.2.21 on 2023-10-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('낮음', '낮음'), ('중간', '중간'), ('높음', '높음')], default='중간', max_length=20)),
            ],
        ),
    ]
