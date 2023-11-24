
import unittest
from fastapi.testclient import TestClient
from src.app import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, World!"})

    def test_read_item(self):
        response = self.client.get("/items/42")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 42, "query_param": None})

    def test_read_item_with_query_param(self):
        response = self.client.get("/items/42?query_param=test")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 42, "query_param": "test"})

if __name__ == '__main__':
    unittest.main()


# import pytest

# from fastapi.testclient import TestClient
# from src import app

# client = TestClient(app.app)

# class TestCase:

#     def test_read_root(self):
#         response = client.get("/")
#         assert response.status_code == 200
#         assert response.json() == {"message": "Hello, World!"}

#     def test_read_item(self):
#         response = client.get("/items/42")
#         assert response.status_code == 200
#         assert response.json() == {"item_id": 42, "query_param": None}

#     def test_read_item_with_query_param(self):
#         response = client.get("/items/42?query_param=test")
#         assert response.status_code == 200
#         assert response.json() == {"item_id": 42, "query_param": "test"}
