from django.db import models


class TblHappiness(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    user_id = models.CharField(max_length=16, null=True)
    team_id = models.CharField(max_length=5, null=True)
    date = models.DateTimeField(null=True)
    idvl_hpns = models.IntegerField(blank=True, null=True)
    team_hpns = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.user_id)
        return str(self.team_id)
        return str(self.date)
        return str(self.idvl_hpns)
        return str(self.team_hpns)


class TblReminder(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    user_id = models.CharField(max_length=16, null=True)
    cur_cnt = models.IntegerField(blank=True, null=True)


class TblTeam(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    team_id = models.CharField(max_length=5, null=True)
    name = models.CharField(max_length=255, null=True)
    wt_start = models.IntegerField(blank=True, null=True)
    wt_end = models.IntegerField(blank=True, null=True)
    team_size = models.IntegerField(blank=True, null=True)


class TblUser(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    user_id = models.CharField(max_length=16, null=True)
    email = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    role = models.IntegerField(blank=True, null=True)
    team_id = models.CharField(max_length=5, null=True)
