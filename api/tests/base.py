import unittest
from src.main import create_app
from src.scripts import MongoDataImporter
from src.interfaces.importer import IDataImporter
from src.connection.database import DataAccessLayer


class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._import_api()
        cls.dal: DataAccessLayer = DataAccessLayer()
        cls.importer: IDataImporter = MongoDataImporter()
        cls.importer.clear_all_models()

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def _import_api(cls):
        cls.app = create_app(config_name='test')
        cls.client = cls.app.test_client()
        cls.headers = {
            'Content-Type': 'application/json'
        }
