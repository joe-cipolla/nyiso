import unittest
import nyiso_sql.query_db as q
import pandas as pd
import pandas.testing as pd_testing
from tests import data_snapshots


class TestSQL(unittest.TestCase):
    """Tests SQL query functions"""

    def assertDataFrameEqual(self, a, b, msg):
        try:
            pd_testing.assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e

    def setup(self):

        self.addTypeEqualityFunc(pd.DataFrame, self.assertDataFrameEqual)

        # load static DataFrame objects and attributes files
        self.static_default_df = data_snapshots.default_df
        self.static_default_df_attr = data_snapshots.default_df_attr

        # load test DataFrame objects
        self.test_default_df = q.get_da_lmp(['2020-05-01', '2020-05-07'], 'CAPITL')

    def tearDown(self):
        pass

    def test_get_da_lmp(self):
        # test value match
        test_data_types = ['default']
        for test_data_type in test_data_types:
            test_df = vars(self)['test_' + test_data_type + '_df']
            static_df = vars(self)['static_' + test_data_type + '_df']
            static_df_attr = vars(self)['static_' + test_data_type + '_df_attr']
            with self.subTest():  # check columns match
                self.assertEqual(test_df.tolist(), static_df.tolist())
            with self.subTest():
                self.assertEqual(test_df.shape, static_df.shape)
            with self.subTest():
                self.assertEqual(test_df['date'], static_df_attr.date)
            with self.subTest():
                self.assertEqual(test_df['zone'], static_df_attr.zone)
            with self.subTest():
                self.assertEqual(test_df['he01'], static_df_attr.he01)

        # test pandas DataFrame equality
        with self.subTest():
            self.assertEqual(self.test_default_df, self.static_default_df)

        # test error raise
        with self.subTest():
            with self.assertRaises(ValueError):
                q.get_da_lmp(['2020-05-01', '2020-05-07'], 'corgi')
            with self.assertRaises(ValueError):
                q.get_da_lmp(['2020-05-01', 'corgi'], 'CAPITL')


if __name__ == '__main__':
    unittest.main()
