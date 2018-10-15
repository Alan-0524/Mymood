# content of test_sample.py
from Mymood.biz import process_happiness, process_teams, process_members, process_events
from models_app.models import *
from django.test import TestCase
import uuid
from django.test import Client


class MyClassTestCase(TestCase):

    def setUp(self):
        TblTeam.objects.filter(team_id='00000').update(
            team_size='8')  # update all records which are undone into timeout

    def test_add_team(self):
        team = TblTeam()
        team.id = str(uuid.uuid1()).replace("-", "")
        team.team_id = "12345"
        team.name = "top team"
        team.wt_start = "10"
        team.wt_end = "17"
        team.team_size = 8
        team.save()

        self.assertIsNotNone(team)

    def test_delete_team(self):
        team = TblTeam()
        team.id = str(uuid.uuid1()).replace("-", "")
        team.save()

        team_id = team.id
        team.delete()

        team_list = TblTeam.objects.filter(id=team_id)
        self.assertEquals(len(team_list), 0)

    def test_modify_team(self):
        team = TblTeam()
        team.id = str(uuid.uuid1()).replace("-", "")
        team.team_size = 4
        team.save()

        team = TblTeam.objects.get(id=team.id)
        team.team_size = 8
        team.save()

        team = TblTeam.objects.get(id=team.id)

        self.assertIsNotNone(team)
        self.assertEqual(team.team_size, 8)

    def test_query_happiness(self):
        list_team = TblTeam.objects.all()

        for i in range(0, len(list_team)):
            team = list_team.get(i)

            list_happiness = TblHappiness.objects.filter(team_id=team.team_id)
            self.assertIsNotNone(list_happiness)
