# Generated by Django 3.1.4 on 2022-07-01 04:09

import ckeditor_uploader.fields
import datetime
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
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('descricao', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('enderesso', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='youtube')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('twiter', models.URLField(blank=True, null=True, verbose_name='Twiter')),
            ],
        ),
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.CharField(max_length=20, unique=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('meta_description', models.TextField(blank=True, max_length=160, null=True)),
                ('meta_keywords', models.TextField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_blog_it.author')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Equipa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('descricao', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('git', models.URLField(blank=True, null=True, verbose_name='Git')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='youtube')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('twiter', models.URLField(blank=True, null=True, verbose_name='Twiter')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.CreateModel(
            name='Image_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='static/uploads/%Y/%m/%d/')),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('is_image', models.BooleanField(default=True)),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='static/uploads/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('meta_description', models.TextField(blank=True, max_length=160, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Drafted', 'Drafted'), ('Published', 'Published'), ('Rejected', 'Rejected'), ('Trashed', 'Trashed')], default='Drafted', max_length=10)),
                ('keywords', models.TextField(blank=True, max_length=500)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='static/blog/uploads/%Y/%m/%d/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_blog_it.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_blog_it.author')),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=500)),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Drafted', 'Drafted'), ('Published', 'Published'), ('Rejected', 'Rejected'), ('Trashed', 'Trashed')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PostHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='django_blog_it.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_Slugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slugs', to='django_blog_it.post')),
            ],
        ),
        migrations.CreateModel(
            name='Google',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_id', models.CharField(default='', max_length=200)),
                ('google_url', models.CharField(default='', max_length=1000)),
                ('verified_email', models.CharField(default='', max_length=200)),
                ('family_name', models.CharField(default='', max_length=200)),
                ('name', models.CharField(default='', max_length=200)),
                ('picture', models.CharField(default='', max_length=200)),
                ('gender', models.CharField(default='', max_length=10)),
                ('dob', models.CharField(default='', max_length=50)),
                ('given_name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(db_index=True, default='', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='google', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_id', models.CharField(max_length=100)),
                ('facebook_url', models.CharField(default='', max_length=200)),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('verified', models.CharField(default='', max_length=200)),
                ('name', models.CharField(default='', max_length=200)),
                ('language', models.CharField(default='', max_length=200)),
                ('hometown', models.CharField(default='', max_length=200)),
                ('email', models.CharField(db_index=True, default='', max_length=200)),
                ('gender', models.CharField(default='', max_length=200)),
                ('dob', models.DateField(blank=True, null=True)),
                ('location', models.CharField(default='', max_length=200)),
                ('timezone', models.CharField(default='', max_length=200)),
                ('accesstoken', models.CharField(default='', max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facebook', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
