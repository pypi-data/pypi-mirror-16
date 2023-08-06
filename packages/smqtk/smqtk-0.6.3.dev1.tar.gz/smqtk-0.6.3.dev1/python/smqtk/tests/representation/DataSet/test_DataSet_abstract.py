import nose.tools as ntools
import random
import unittest

from smqtk.representation import DataSet


__author__ = "paul.tunison@kitware.com"


class DummyDataSet (DataSet):

    @classmethod
    def is_usable(cls):
        return True

    def __init__(self):
        super(DummyDataSet, self).__init__()
        self.stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    def count(self):
        return len(self.stuff)

    def __iter__(self):
        for e in self.stuff:
            yield e

    def has_uuid(self, uuid):
        pass

    def get_data(self, uuid):
        return self.stuff[uuid]

    def add_data(self, *elems):
        pass

    def uuids(self):
        return range(len(self.stuff))

    def get_config(self):
        return {}


class TestDataSetAbstract (unittest.TestCase):

    def test_len(self):
        ds = DummyDataSet()
        ntools.assert_equal(len(ds), ds.count())

    def test_getItem(self):
        ds = DummyDataSet()
        uid_list = ds.uuids()
        random.shuffle(uid_list)
        for i in uid_list:
            ntools.assert_equal(ds.get_data(i), ds[i])
