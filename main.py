import requests
import steamspypi


def get_steam_api_url():
    return 'https://store.steampowered.com/appreviews/'


def get_top_100_app_ids():
    # Reference: https://github.com/woctezuma/steam-descriptions/blob/master/benchmark_utils.py

    data_request = dict()
    data_request['request'] = 'top100in2weeks'

    data = steamspypi.download(data_request)

    top_100_app_ids = list(int(app_id) for app_id in data.keys())

    return top_100_app_ids


def download_review_summary(verbose=False):
    # Reference: https://github.com/woctezuma/download-steam-reviews/blob/master/steamreviews/download_reviews.py

    input_app_ids = get_top_100_app_ids()

    request_params = {
        'json': '1',
        'language': 'all',
    }

    review_summary = dict()

    if verbose:
        print('AppID;Steam;Non-Steam')

    for app_id in input_app_ids:
        review_summary[app_id] = dict()

        for purchase_type in ['steam', 'non_steam_purchase']:
            request_params['purchase_type'] = purchase_type

            resp_data = requests.get(get_steam_api_url() + str(app_id), params=request_params)

            if resp_data.status_code == 200:
                result = resp_data.json()
                query_summary = result['query_summary']
                num_reviews = query_summary['total_reviews']
                review_summary[app_id][purchase_type] = int(num_reviews)
            else:
                # If you reach this point, there is an issue. You might want to try again later, from this point onward.
                review_summary[app_id][purchase_type] = -1

        if verbose:
            print('{};{};{}'.format(app_id,
                                    review_summary[app_id]['steam'],
                                    review_summary[app_id]['non_steam_purchase']))

    return review_summary


if __name__ == '__main__':
    review_summary = download_review_summary(verbose=True)
