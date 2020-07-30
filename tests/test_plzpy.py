#
# Initially the tests were implemented for the go version
# and then the results compared with jsondiff to make sure
# the result was the same, but in the end is better to have them
# here as well
#

from plzpy.plzpy import massage
import json
import os


def test_massage(testdata_fixture, tmpdir):

    tests = [
        {
            "input": os.path.join(testdata_fixture, "data.csv"),
            "output": os.path.join(tmpdir, "x.json"),
            "want_err": False,
            "expected": {
                "counters": {"10001": {"total": 1}, "10003": {"total": 3}, "10006": {"total": 6}},
                "distributions": {
                    "10001": [{"year": "1960", "count": 1}],
                    "10003": [{"year": "1960", "count": 2}, {"year": "1961", "count": 1}],
                    "10006": [{"year": "1960", "count": 3}, {"year": "2010", "count": 3}],
                },
            }
        }
    ]

    for x in tests:
        try:
            massage(x["input"], x["output"], True)
            assert(not x["want_err"])
            with open(x["output"]) as fp:
                got = json.load(fp)
                print(got)
                assert(got == x["expected"])
        except:
            assert(x["want_err"])
