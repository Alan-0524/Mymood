from django.db import models


class TblHappiness(models.Model):
    id = models.BigAutoField(primary_key=True)
    team_id = models.IntegerField()
    date = models.DateTimeField()
    idvl_hpns = models.IntegerField(blank=True, null=True)
    team_hpns = models.IntegerField(blank=True, null=True)


class TblReminder(models.Model):
    user_id = models.IntegerField()
    cur_cnt = models.IntegerField(blank=True, null=True)


class TblTeam(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    wt_start = models.IntegerField(blank=True, null=True)
    wt_end = models.IntegerField(blank=True, null=True)
    team_size = models.IntegerField(blank=True, null=True)


class TblUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.IntegerField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
