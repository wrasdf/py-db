import unittest2 as unittest

class TestDB(unittest.TestCase):

    def test_example(self):
        self.assertTrue(True)

    # def setUp(self):
    #    if not self.database_connection:
    #        self.skipTest("No database URL set")
    #    self.engine = sqlalchemy.create_engine(self.database_connection)
    #    self.connection = self.engine.connect()
    #    self.connection.execute("CREATE DATABASE testdb")
    #
    # def tearDown(self):
    #     self.connection.execute("DROP DATABASE testdb")

if __name__ == '__main__':
    unittest.main()
