# Generated by Django 4.2.15 on 2024-12-08 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('tank', 'Танки'), ('hilt', 'Хилы'), ('dd', 'ДД'), ('traders', 'Торговцы'), ('guild_master', 'Гилдмастеры'), ('questgiver', 'Квестгиверы'), ('blacksmith', 'Кузнецы'), ('tanner', 'Кожевники'), ('potion_maker', 'Зельевары'), ('spellmaster', 'Мастера заклинаний')], max_length=35)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('approved', 'Принят'), ('rejected', 'Отклонен'), ('new', 'Новый')], default='new', max_length=35)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
            },
        ),
    ]
