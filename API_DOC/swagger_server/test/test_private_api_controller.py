# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.campaign_fetcher import CampaignFetcher  # noqa: E501
from swagger_server.models.tweet import Tweet  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPrivateAPIController(BaseTestCase):
    """PrivateAPIController integration test stubs"""

    def test_get_tweets(self):
        """Test case for get_tweets

        Obtención de los Tweets en formato JSON para ser usados por Manager.
        """
        Campaign = CampaignFetcher()
        response = self.client.open(
            '/FedericoCalonge/TweetMaster/1.0.0/Fetcher',
            method='GET',
            data=json.dumps(Campaign),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
