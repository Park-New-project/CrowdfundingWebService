# Generated by Django 2.2.3 on 2019-08-15 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrfUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.CharField(max_length=16, unique=True, verbose_name='아이디')),
                ('username', models.CharField(max_length=30, verbose_name='유저 이름')),
                ('email', models.EmailField(max_length=50, verbose_name='이메일')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CrfProject',
            fields=[
                ('pType', models.CharField(choices=[('G', '게임'), ('A', '예술'), ('F', '패션'), ('C', '캠페인')], default='G', max_length=2, verbose_name='종류')),
                ('pid', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='고유번호')),
                ('pTitle', models.CharField(max_length=30, verbose_name='제목')),
                ('pImage', models.ImageField(blank=True, null=True, upload_to='<django.db.models.fields.CharField>/', verbose_name='이미지')),
                ('pIntro', models.CharField(max_length=50, null=True, verbose_name='소개글')),
                ('pContext', models.TextField(null=True, verbose_name='본문')),
                ('fin_time', models.DateField(auto_now_add=True, verbose_name='마감일')),
                ('cre_time', models.DateField(auto_now_add=True, verbose_name='등록일')),
                ('owned_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='소유주')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrib_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='기여자')),
                ('pid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crowdfunding.CrfProject', verbose_name='고유번호')),
            ],
        ),
    ]
