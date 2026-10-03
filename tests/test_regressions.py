import unittest
import numpy as np
import pandas as pd
from forecast_data import prepare_series

class ForecastRegressionTests(unittest.TestCase):
    def setUp(self):
        self.frame = pd.DataFrame({'Date':['2018-01-14','2018-01-07','2018-01-07','2018-01-07'],
          'AveragePrice':[1.2,1.1,4.,9.], 'region':['TotalUS','TotalUS','West','TotalUS'],
          'type':['conventional','conventional','conventional','organic']})
    def test_national_series_excludes_regional_and_organic_rows(self):
        result=prepare_series(self.frame)
        self.assertEqual(result.y.tolist(),[1.1,1.2])
        self.assertTrue(result.ds.is_monotonic_increasing)
    def test_duplicate_dates_rejected(self):
        with self.assertRaises(ValueError): prepare_series(pd.concat([self.frame,self.frame.iloc[:1]]))
    def test_missing_series_rejected(self):
        with self.assertRaises(ValueError): prepare_series(self.frame,region='missing')
    def test_nonfinite_prices_rejected(self):
        self.frame.loc[0,'AveragePrice']=np.inf
        with self.assertRaises(ValueError): prepare_series(self.frame)
    def test_missing_schema_rejected(self):
        with self.assertRaises(ValueError): prepare_series(self.frame.drop(columns='type'))
