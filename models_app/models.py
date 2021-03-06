from django.db import models


class TblHappiness(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    user_id = models.CharField(max_length=16, null=True)
    team_id = models.CharField(max_length=5, null=True)
    date = models.DateTimeField(null=True)
    idvl_hpns = models.IntegerField(blank=True, null=True)
    team_hpns = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.team_id)


class TblReminder(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    user_id = models.CharField(max_length=16, null=True)
    cur_cnt = models.IntegerField(blank=True, null=True)


class TblTeam(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    team_id = models.CharField(max_length=5, null=True)
    name = models.CharField(max_length=255, null=True)
    wt_start = models.CharField(blank=True, max_length=2, null=True)
    wt_end = models.CharField(blank=True, max_length=2, null=True)
    team_size = models.IntegerField(blank=True, null=True)
    week_push = models.CharField(max_length=7, null=True)

    def __str__(self):
        return str(self.team_id)

    class Meta:
        ordering = ["name"]


class TblUser(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    user_id = models.CharField(max_length=16, null=True)
    user_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    role = models.IntegerField(blank=True, null=True)
    team_id = models.CharField(max_length=5, null=True)
    first_time = models.CharField(max_length=50, blank=True, null=True)
    first_time_status = models.IntegerField(blank=True, null=True)
    second_time = models.CharField(max_length=50, blank=True, null=True)
    second_time_status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.user_id)


class TblEvent(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    event_title = models.CharField(max_length=50, null=True)
    event_date = models.DateTimeField(null=True)
    event_content = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return str(self.event_title)
