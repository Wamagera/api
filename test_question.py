import unittest
import os
import JSON

class questions (unnittest.TestCase):
    def setUp(self):
        self.app=create_app(config_name = "testing")
        self.user = self.app.test_config
        self.question = {}

def test_question_creation(self):
    res=user.admin().post('/createquestion/', data=self.createquestion)
    self.assertEgual(res.status_code,201)
    self.assertIn('New Question', str(res.data))

def test_getquestions(self):
    res=self.user().post('/viewquestions/', data=self.viewquestion)
    self.assertEgual(res.status_code, 200)
    res=self.user().get('/viewquestion/')
    self.assertEgual(res.status_code,200)
    self.assertIn('can tomorrow be today', str(res.data))

def test_api_get_question_by_id(self):
    rv=self,user().post('/viewquestion', data=self.viewquestion)
    self.assertEgual(rv.status_code, 201)
    result_in_json= json.loads(rv,data.decode('utf-8').replace("" "/"))
    result = self.user().get(
    '/viewquestion/{}'.format(result_in_json['id']))
    self.assertEgual(result.status_code, 200)
    self.assertIn('can tomorrow be today', str(result.data))

 def tearDown(self):
     with self.app.app_context():
