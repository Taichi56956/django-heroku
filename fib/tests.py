from django.test import TestCase
from django.urls import reverse
from .views import fibonacci_view


class FibonacciTest(TestCase):
    def test_fibonacci(self):
        # APIにアクセスし、結果を取得
        response = self.client.get(reverse('fibonacci', args=[10]))

        # 結果が200 OKであることを確認
        self.assertEqual(response.status_code, 200)

        # 結果が55であることを確認
        self.assertJSONEqual(response.content, {"result": 55})

    def test_fibonacci_invalid_input(self):
        # APIにアクセスし、結果を取得
        response = self.client.get(reverse('fibonacci', args=[-1]))

        # 結果が400 Bad Requestであることを確認
        self.assertEqual(response.status_code, 400)

        # 結果がエラーメッセージであることを確認
        self.assertJSONEqual(response.content, {'status':400, 'message': 'bad request'})

