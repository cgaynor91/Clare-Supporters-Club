{"filter":false,"title":"test_views.py","tooltip":"/accounts/test_views.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":13,"column":61},"action":"insert","lines":["from django.test import TestCase","","","class TestAccountsView(TestCase):","","    def test_register_page(self):","        response = self.client.get('/accounts/register/')","        self.assertEquals(response.status_code, 200)","        self.assertTemplateUsed(response, 'users/register.html')","","    def test_login_page(self):","        response = self.client.get('/accounts/login/')","        self.assertEquals(response.status_code, 200)","        self.assertTemplateUsed(response, 'users/login.html')"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":61},"end":{"row":13,"column":61},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1584122165590,"hash":"8217168c07c8d6dd65a6ddd7851f4afdb1ffae87"}