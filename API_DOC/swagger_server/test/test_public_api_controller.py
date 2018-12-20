# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.campaign import Campaign  # noqa: E501
from swagger_server.models.reporter import Reporter  # noqa: E501
from swagger_server.models.tweet import Tweet  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPublicAPIController(BaseTestCase):
    """PublicAPIController integration test stubs"""

    def test_add_campaign(self):
        """Test case for add_campaign

        Añade una Campaña.
        """
        Campaign = Campaign()
        response = self.client.open(
            '/FedericoCalonge/TweetMaster/1.0.0/Campaign',
            method='POST',
            data=json.dumps(Campaign),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_del_campaign(self):
        """Test case for del_campaign

        Eliminar una campaña.
        """
        headers = [('_email', '_email_example'),
                   ('_idC', 56)]
        response = self.client.open(
            '/FedericoCalonge/TweetMaster/1.0.0/Campaign',
            method='DELETE',
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_campaign(self):
        """Test case for get_campaign

        Obtener una Campaña.
        """
        response = self.client.open(
            '/FedericoCalonge/TweetMaster/1.0.0/Campaign/{_idC}'.format(_idC=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_reporter_json(self):
        """Test case for get_reporter_json

        Obtener un resumen del reporte en JSON.
        """
        response = self.client.open(
            '/FedericoCalonge/TweetMaster/1.0.0/Reporter/ReporterJSON/{_idC}'.format(_idC=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_reporter_raw(self):
        """Test case for get_reporter_raw

        Obtener un reporte crudo.
        """
        response = self.client.open(
            '/FedericoCalonge/TweetMaster/1.0.0/Reporter/ReporterRaw/{_idC}'.format(_idC=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mod_campaign_byid_c(self):
        """Test case for mod_campaign_byid_c

        Modificar una Campaña.
        """
        headers = [('columnaAModif', 'columnaAModif_example'),
                   ('campoColumna', 'campoColumna_example')]
        response = self.client.open(
            '/FedericoCalonge/TweetMaster/1.0.0/Campaign/{_idC}'.format(_idC=56),
            method='PATCH',
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
