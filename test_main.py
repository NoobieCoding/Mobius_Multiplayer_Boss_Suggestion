import data
import sys
import json
import unittest
import suggestion_system


class Test(unittest.TestCase):

    def testGetData1(self):
        suggestedJobs = (suggestion_system
                         .get_suggested_jobs_name('fire', 'attacker'))
        assert len(suggestedJobs) == 4
        assert suggestedJobs[1] == "天道士"

    def testGetData2(self):
        suggestedJobs = (suggestion_system
                         .get_suggested_jobs_name('light', 'breaker'))
        assert len(suggestedJobs) == 5
        assert suggestedJobs[3] == "マテリアハンター"

    def testGetDataError(self):
        with self.assertRaises(Exception):
            suggestedJobs = (suggestion_system
                             .get_suggested_jobs_name('god', 'support'))


if __name__ == '__main__':
    unittest.main()
