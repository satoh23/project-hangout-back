# Generated by Django 3.1 on 2021-07-09 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields
import uuid
import validation.image_validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDetail',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=255, primary_key=True, serialize=False)),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='blog_thumbnail/', validators=[validation.image_validators.image_validator], verbose_name='サムネイル')),
                ('encoded_thumbnail', models.TextField(blank=True, null=True, verbose_name='エンコードしたサムネイル')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='前文')),
                ('body', models.TextField(verbose_name='本文')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='価格')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='筆者')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20, verbose_name='ジャンル')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=False, verbose_name='いいね')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.blogdetail', verbose_name='ブログ')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='購入者')),
            ],
        ),
        migrations.AddField(
            model_name='blogdetail',
            name='genre_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.genre', verbose_name='ジャンル'),
        ),
    ]
