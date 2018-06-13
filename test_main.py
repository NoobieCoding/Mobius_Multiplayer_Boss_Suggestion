import data
import sys
import json
import unittest


class Test(unittest.TestCase):
    jobsData = {}

    def setUp(self):
        global jobsData
        with open('jobs.json', 'r') as f:
            jobsData = json.load(f)

    def testGetData1(self):
        allSuggestedJobs = jobsData["suggestion"]["fire"]["attacker"]
        assert len(allSuggestedJobs) == 4
        assert allSuggestedJobs[0] == "天道士"

    def testGetData2(self):
        allSuggestedJobs = jobsData["suggestion"]["light"]["breaker"]
        assert len(allSuggestedJobs) == 5
        assert allSuggestedJobs[3] == "マテリアハンター"

    def testGetDataError(self):
        with self.assertRaises(Exception):
            allSuggestedJobs = jobsData["suggestion"]["ice"]["breaker"]
            

if __name__ == '__main__':
    unittest.main()
