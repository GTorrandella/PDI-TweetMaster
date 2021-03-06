# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Reporter(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id_c: int=None, fecha_inicio: datetime=None, fecha_fin: datetime=None, email: str=None, mentions: List[str]=None, hashtags: List[str]=None, cant_tweets: int=None, more_tw_user: str=None, user_quantity: str=None):  # noqa: E501
        """Reporter - a model defined in Swagger

        :param id_c: The id_c of this Reporter.  # noqa: E501
        :type id_c: int
        :param fecha_inicio: The fecha_inicio of this Reporter.  # noqa: E501
        :type fecha_inicio: datetime
        :param fecha_fin: The fecha_fin of this Reporter.  # noqa: E501
        :type fecha_fin: datetime
        :param email: The email of this Reporter.  # noqa: E501
        :type email: str
        :param mentions: The mentions of this Reporter.  # noqa: E501
        :type mentions: List[str]
        :param hashtags: The hashtags of this Reporter.  # noqa: E501
        :type hashtags: List[str]
        :param cant_tweets: The cant_tweets of this Reporter.  # noqa: E501
        :type cant_tweets: int
        :param more_tw_user: The more_tw_user of this Reporter.  # noqa: E501
        :type more_tw_user: str
        :param user_quantity: The user_quantity of this Reporter.  # noqa: E501
        :type user_quantity: str
        """
        self.swagger_types = {
            'id_c': int,
            'fecha_inicio': datetime,
            'fecha_fin': datetime,
            'email': str,
            'mentions': List[str],
            'hashtags': List[str],
            'cant_tweets': int,
            'more_tw_user': str,
            'user_quantity': str
        }

        self.attribute_map = {
            'id_c': 'idC',
            'fecha_inicio': 'fechaInicio',
            'fecha_fin': 'fechaFin',
            'email': 'email',
            'mentions': 'mentions',
            'hashtags': 'hashtags',
            'cant_tweets': 'cant_tweets',
            'more_tw_user': 'moreTwUser',
            'user_quantity': 'userQuantity'
        }

        self._id_c = id_c
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._email = email
        self._mentions = mentions
        self._hashtags = hashtags
        self._cant_tweets = cant_tweets
        self._more_tw_user = more_tw_user
        self._user_quantity = user_quantity

    @classmethod
    def from_dict(cls, dikt) -> 'Reporter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Reporter of this Reporter.  # noqa: E501
        :rtype: Reporter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_c(self) -> int:
        """Gets the id_c of this Reporter.


        :return: The id_c of this Reporter.
        :rtype: int
        """
        return self._id_c

    @id_c.setter
    def id_c(self, id_c: int):
        """Sets the id_c of this Reporter.


        :param id_c: The id_c of this Reporter.
        :type id_c: int
        """
        if id_c is None:
            raise ValueError("Invalid value for `id_c`, must not be `None`")  # noqa: E501

        self._id_c = id_c

    @property
    def fecha_inicio(self) -> datetime:
        """Gets the fecha_inicio of this Reporter.


        :return: The fecha_inicio of this Reporter.
        :rtype: datetime
        """
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: datetime):
        """Sets the fecha_inicio of this Reporter.


        :param fecha_inicio: The fecha_inicio of this Reporter.
        :type fecha_inicio: datetime
        """
        if fecha_inicio is None:
            raise ValueError("Invalid value for `fecha_inicio`, must not be `None`")  # noqa: E501

        self._fecha_inicio = fecha_inicio

    @property
    def fecha_fin(self) -> datetime:
        """Gets the fecha_fin of this Reporter.


        :return: The fecha_fin of this Reporter.
        :rtype: datetime
        """
        return self._fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, fecha_fin: datetime):
        """Sets the fecha_fin of this Reporter.


        :param fecha_fin: The fecha_fin of this Reporter.
        :type fecha_fin: datetime
        """
        if fecha_fin is None:
            raise ValueError("Invalid value for `fecha_fin`, must not be `None`")  # noqa: E501

        self._fecha_fin = fecha_fin

    @property
    def email(self) -> str:
        """Gets the email of this Reporter.


        :return: The email of this Reporter.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this Reporter.


        :param email: The email of this Reporter.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def mentions(self) -> List[str]:
        """Gets the mentions of this Reporter.


        :return: The mentions of this Reporter.
        :rtype: List[str]
        """
        return self._mentions

    @mentions.setter
    def mentions(self, mentions: List[str]):
        """Sets the mentions of this Reporter.


        :param mentions: The mentions of this Reporter.
        :type mentions: List[str]
        """
        if mentions is None:
            raise ValueError("Invalid value for `mentions`, must not be `None`")  # noqa: E501

        self._mentions = mentions

    @property
    def hashtags(self) -> List[str]:
        """Gets the hashtags of this Reporter.


        :return: The hashtags of this Reporter.
        :rtype: List[str]
        """
        return self._hashtags

    @hashtags.setter
    def hashtags(self, hashtags: List[str]):
        """Sets the hashtags of this Reporter.


        :param hashtags: The hashtags of this Reporter.
        :type hashtags: List[str]
        """
        if hashtags is None:
            raise ValueError("Invalid value for `hashtags`, must not be `None`")  # noqa: E501

        self._hashtags = hashtags

    @property
    def cant_tweets(self) -> int:
        """Gets the cant_tweets of this Reporter.


        :return: The cant_tweets of this Reporter.
        :rtype: int
        """
        return self._cant_tweets

    @cant_tweets.setter
    def cant_tweets(self, cant_tweets: int):
        """Sets the cant_tweets of this Reporter.


        :param cant_tweets: The cant_tweets of this Reporter.
        :type cant_tweets: int
        """
        if cant_tweets is None:
            raise ValueError("Invalid value for `cant_tweets`, must not be `None`")  # noqa: E501

        self._cant_tweets = cant_tweets

    @property
    def more_tw_user(self) -> str:
        """Gets the more_tw_user of this Reporter.


        :return: The more_tw_user of this Reporter.
        :rtype: str
        """
        return self._more_tw_user

    @more_tw_user.setter
    def more_tw_user(self, more_tw_user: str):
        """Sets the more_tw_user of this Reporter.


        :param more_tw_user: The more_tw_user of this Reporter.
        :type more_tw_user: str
        """
        if more_tw_user is None:
            raise ValueError("Invalid value for `more_tw_user`, must not be `None`")  # noqa: E501

        self._more_tw_user = more_tw_user

    @property
    def user_quantity(self) -> str:
        """Gets the user_quantity of this Reporter.


        :return: The user_quantity of this Reporter.
        :rtype: str
        """
        return self._user_quantity

    @user_quantity.setter
    def user_quantity(self, user_quantity: str):
        """Sets the user_quantity of this Reporter.


        :param user_quantity: The user_quantity of this Reporter.
        :type user_quantity: str
        """
        if user_quantity is None:
            raise ValueError("Invalid value for `user_quantity`, must not be `None`")  # noqa: E501

        self._user_quantity = user_quantity
