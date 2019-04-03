import unittest

import main


class TestMainMethods(unittest.TestCase):

    def test_get_top_100_app_ids(self):
        top_100_app_ids = main.get_top_100_app_ids()
        self.assertEqual(len(top_100_app_ids), 100)

    def test_download_review_summary(self):
        review_summary = main.download_review_summary(input_app_ids=[4000], verbose=True)
        self.assertEqual(len(review_summary), 1)


if __name__ == '__main__':
    unittest.main()
