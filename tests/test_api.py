import unittest
from io import BytesIO

from minio import Minio
from minio.error import ResponseError

from datasets.api import app
from datasets.datasets import bucket, client


class TestApi(unittest.TestCase):

    def setUp(self):
        # ensures that the bucket exists and is empty
        self.empty_bucket()
        self.make_bucket()

    def tearDown(self):
        # removes bucket after the tests complete
        self.empty_bucket()
        self.remove_bucket()

    def empty_bucket(self):
        # removes bucket after tests are completed
        try:
            for obj in client.list_objects(bucket, prefix="", recursive=True):
                client.remove_object(bucket, obj.object_name)
        except:
            pass

    def make_bucket(self):
        try:
            client.make_bucket(bucket)
        except:
            pass

    def remove_bucket(self):
        try:
            client.remove_bucket(bucket)
        except:
            pass

    def test_ping(self):
        with app.test_client() as c:
            rv = c.get("/")
            result = rv.get_data(as_text=True)
            expected = "pong"
            self.assertEqual(result, expected)

    def test_get_datasets(self):
        with app.test_client() as c:
            rv = c.get("/v1/datasets")
            result = rv.get_json()
            expected = []
            self.assertListEqual(result, expected)

    def test_post_datasets(self):
        with app.test_client() as c:
            rv = c.post("/v1/datasets", data={
                "file": (BytesIO(b"5.1,3.5,1.4,0.2,Iris-setosa\n" +
                                 b"4.9,3.0,1.4,0.2,Iris-setosa\n" +
                                 b"4.7,3.2,1.3,0.2,Iris-setosa\n" +
                                 b"4.6,3.1,1.5,0.2,Iris-setosa"), "iris.data"),
            })
            result = rv.get_json()
            expected = {
                "name": "iris.data",
                "metadata": {
                    "col0": "numeric",
                    "col1": "numeric",
                    "col2": "numeric",
                    "col3": "numeric",
                    "col4": "category",
                },
            }
            if "url" in result:
                del result["url"]
            self.assertDictEqual(expected, result)

    def test_get_dataset(self):
        with app.test_client() as c:
            rv = c.get("/v1/datasets/iris.data")
            result = rv.get_json()
            expected = {"message": "The specified dataset does not exist"}
            self.assertDictEqual(expected, result)
