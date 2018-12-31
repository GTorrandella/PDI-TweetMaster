import connexion
import six

from swagger_server.models.campaign import Campaign  # noqa: E501
from swagger_server.models.delete import Delete  # noqa: E501
from swagger_server.models.patch import Patch  # noqa: E501
from swagger_server.models.reporter import Reporter  # noqa: E501
from swagger_server.models.tweet import Tweet  # noqa: E501
from swagger_server import util


def add_campaign(Campaign=None):  # noqa: E501
    """Añade una Campaña.

    Añade una Campaña al sistema. # noqa: E501

    :param Campaign: Campaign to add.
    :type Campaign: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Campaign = Campaign.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def del_campaign(email_e_iC=None):  # noqa: E501
    """Eliminar una campaña.

    Elimina una campaña del sistema al proporcionarle su ID o el email del dueño. Será eliminada únicamente si la campaña todavía no empezó. # noqa: E501

    :param email_e_iC: email e iC.
    :type email_e_iC: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        email_e_iC = Delete.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_campaign(_idC):  # noqa: E501
    """Obtener una Campaña.

    Indicando el id correcto se obtendrá información de la Campaña. # noqa: E501

    :param _idC: 
    :type _idC: int

    :rtype: ERRORUNKNOWN
    """
    return 'do some magic!'


def get_reporter_json(_idC):  # noqa: E501
    """Obtener un resumen del reporte en JSON.

    Se puede obtener el resumen del reporte en JSON dada la Campaña _idC. # noqa: E501

    :param _idC: 
    :type _idC: int

    :rtype: List[Reporter]
    """
    return 'do some magic!'


def get_reporter_raw(_idC):  # noqa: E501
    """Obtener un reporte crudo.

    Se puede obtener el reporte en crudo dada la Campaña _idC. # noqa: E501

    :param _idC: 
    :type _idC: int

    :rtype: List[Tweet]
    """
    return 'do some magic!'


def mod_campaign_byid_c(_idC, columnas=None):  # noqa: E501
    """Modificar una Campaña.

    Modifica una Campaña en el sistema sólo si esta todavía no empezó. Se debe ingresar el _idC, una columna a modificar en coumnaAModif (email, startDate, finDate, hashtags, mentions) y el valor a modificar (en campoCOlumna). # noqa: E501

    :param _idC: 
    :type _idC: int
    :param columnas: columnaAmodif y campoColumna.
    :type columnas: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        columnas = Patch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
