{"filter":false,"title":"test_views.py","tooltip":"/cart/test_views.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":8,"column":59},"action":"insert","lines":["from django.test import TestCase","","","class TestCartView(TestCase):","","    def test_view_cart_page(self):","        response = self.client.get('/cart/view_cart/')","        self.assertEquals(response.status_code, 200)","        self.assertTemplateUsed(response, 'cart/cart.html')"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":59},"end":{"row":8,"column":59},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1584122277437,"hash":"057646bd4a5618d6ea1cd838cb9b20d7d9029d7e"}