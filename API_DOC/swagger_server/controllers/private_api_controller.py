import connexion
import six

from swagger_server.models.campaign_fetcher import CampaignFetcher  # noqa: E501
from swagger_server.models.tweet import Tweet  # noqa: E501
from swagger_server import util


def get_tweets(Campaign=None):  # noqa: E501
    """Obtención de los Tweets en formato JSON para ser usados por Manager.

    Parte INTERNA de la API. REcibe una Campaña como JSON en el request y devuelve al Manager en el response una lista de Tweets en formato JSON. # noqa: E501

    :param Campaign: Campaign to add.
    :type Campaign: dict | bytes

    :rtype: Tweet
    """
    if connexion.request.is_json:
        Campaign = CampaignFetcher.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
