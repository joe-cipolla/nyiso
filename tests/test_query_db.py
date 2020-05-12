import unittest
import nyiso_sql.query_db as q
import pandas as pd
import pandas.testing as pd_testing
from tests import data_snapshots


class TestQueryDb(unittest.TestCase):
    """Tests SQL query functions"""

    def assertDataFrameEqual(self, a, b, msg):
        try:
            pd_testing.assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e

    def setUp(self):

        self.addTypeEqualityFunc(pd.DataFrame, self.assertDataFrameEqual)

        # load static DataFrame objects and attributes files
        self.static_default_df = data_snapshots.default_df

        # load test DataFrame objects
        self.test_default_df = q.get_da_lmp(['2020-05-01', '2020-05-07'], 'CAPITL')

    def test_GetDaLmp(self):
        test_data_types = ['default']
        for test_data_type in test_data_types:
            test_df = vars(self)['test_' + test_data_type + '_df']
            test_df.date = [i.strftime('%Y-%m-%d') for i in test_df.date]
            static_df = vars(self)['static_' + test_data_type + '_df']

            with self.subTest():  # check columns match
                self.assertEqual(test_df.columns.tolist(), static_df.columns.tolist())
            with self.subTest():
                self.assertEqual(test_df.shape, static_df.shape)
            with self.subTest():  # test pandas DataFrame equality
                self.assertEqual(test_df, static_df)

        # test error raise
        with self.subTest():
            with self.assertRaises(ValueError):
                q.get_da_lmp(['2020-05-01', '2020-05-07'], 'corgi')
            with self.assertRaises(ValueError):
                q.get_da_lmp(['2020-05-01', 'corgi'], 'CAPITL')


if __name__ == '__main__':
    unittest.main()
