import unittest

import main


class TestMainMethods(unittest.TestCase):
    def test_get_top_100_app_ids(self) -> None:
        top_100_app_ids = main.get_top_100_app_ids()
        assert len(top_100_app_ids) == 100

    def test_download_review_summary(self) -> None:
        review_summary = main.download_review_summary(
            input_app_ids=[4000],
            verbose=True,
        )
        assert len(review_summary) == 1


if __name__ == '__main__':
    unittest.main()
