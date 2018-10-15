# from django.test import TestCase
# from models_app.models import *
# import uuid


# Create your tests here.

# id = models.CharField(max_length=32, primary_key=True)
# team_id = models.CharField(max_length=5, null=True)
# name = models.CharField(max_length=255, null=True)
# wt_start = models.IntegerField(blank=True, null=True)
# wt_end = models.IntegerField(blank=True, null=True)
# team_size = models.IntegerField(blank=True, null=True)

# def setUp(self):
#     TblTeam.objects.filter(team_id='00000').update(team_size='8')  # update all records which are undone into timeout
#
#
# def test_add_team(self):
#     team = TblTeam()
#     team.id = str(uuid.uuid1()).replace("-", "")
#     team.team_id = "12345"
#     team.name = "top team"
#     team.wt_start = "10:00"
#     team.wt_end = "17:00"
#     team.team_size = 8
#     team.save()
#
#     self.assertIsNotNone(team)
#     self.assertEqual(len(team), 1)
#
#
# def test_delete_team(self):
#     team = TblTeam()
#     team.id = str(uuid.uuid1()).replace("-", "")
#     team.save()
#
#     team_id = team.id
#     team.delete()
#
#     team = TblTeam.objects.filter(id=team_id)
#     self.assertIsNone(team)
#     self.assertEquals(len(team), 0)
#
#
# def test_modify_team(self):
#     team = TblTeam()
#     team.id = str(uuid.uuid1()).replace("-", "")
#     team.team_size = 4
#     team.save()
#
#     team = TblTeam.objects.get(id=team.id)
#     team.team_size = 8
#     team.save()
#
#     team = TblTeam.objects.get(id=team.id)
#
#     self.assertIsNotNone(team)
#     self.assertEqual(team.team_size, 8)
#
#
# def test_query_happiness(self):
#     list_team = TblTeam.objects.all()
#
#     for i in range(len(0, list_team)):
#         team = list_team.get(i)
#
#         list_happiness = TblHappiness.objects.filter(team_id=team.team_id)
#         self.assertIsNotNone(list_happiness)
def test_eql(self):
    self.assertEqual(1, 1)
