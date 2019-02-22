# Generated by Django 2.2b1 on 2019-02-22 12:13

from django.db import migrations

from wepost.apps.auth.models import WepostUser


def create_dev_test_users(apps,schema_editor):
  dev_usernames = [ f"dev{i}" for i in range(20)]
  test_usernames = [ f"test{i}" for i in range(20)]
  usernames = dev_usernames + test_usernames
  users = [ ]
  for username in usernames:
    user = WepostUser(username=username, is_active=True,is_staff=username.startswith("dev"))
    user.set_password("abc123456")
    users.append(user)

  WepostUser.objects.bulk_create(users)

class Migration(migrations.Migration):

    dependencies = [
        ('wepost_auth', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_dev_test_users)
    ]