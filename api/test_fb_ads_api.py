from unittest.mock import Mock, MagicMock, patch
from facebook_business.api import FacebookAdsApi # pylint: disable=import-error
from facebook_business.adobjects.adaccount import AdAccount # pylint: disable=import-error


def call_fb_api():
    FacebookAdsApi.init("1234", "secret", "123456789abcdefghijklmnopqrstuvwxyz")
    print(FacebookAdsApi)

# key thing to note here is that we are patching where the FacebookAdsApi is used.
# In this case, it's actually being used *in* the test
@patch('api.test_fb_ads_api.FacebookAdsApi')
def test_call_fb_api_response(mock_fb):
    call_fb_api()
    print(mock_fb)
    assert isinstance(mock_fb, MagicMock)
    assert isinstance(FacebookAdsApi, MagicMock)


# usually, we'd expect that usually the test and the FacebookAdsApi would be in separate files
# in that case we would do:

# @patch('api.path_to_file_where_fb_ads_api_used.FacebookAdsApi')
# def test_call_fb_api_response(mock_fb):
#     call_fb_api()
#     print(mock_fb)
#     assert isinstance(mock_fb, MagicMock)
#     assert isinstance(FacebookAdsApi, MagicMock)