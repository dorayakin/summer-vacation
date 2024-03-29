# Generated by Django 4.0.3 on 2022-05-06 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diaryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_text', models.TextField(blank=True, max_length=2000, null=True)),
                ('pub_date', models.DateTimeField(verbose_name='作成日時')),
                ('public_mode', models.CharField(choices=[('T', '一次保存'), ('U', '公開申請'), ('A', '公開済'), ('D', '削除')], default='T', max_length=1)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'posted_diaries',
            },
        ),
    ]
