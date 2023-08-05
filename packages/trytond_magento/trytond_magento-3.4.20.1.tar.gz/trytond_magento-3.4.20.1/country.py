# -*- coding: utf-8 -*-
from trytond.pool import PoolMeta


__all__ = ['Country', 'Subdivision']
__metaclass__ = PoolMeta


class Country:
    "Country"
    __name__ = 'country.country'

    @classmethod
    def __setup__(cls):
        """
        Setup the class before adding to pool
        """
        super(Country, cls).__setup__()
        cls._error_messages.update({
            'country_not_found': 'Country with ISO code %s does not exist.',
        })

    @classmethod
    def search_using_magento_code(cls, code):
        """
        Searches for country with given magento code.

        :param code: ISO code of country
        :return: Browse record of country if found else raises error
        """
        countries = cls.search([('code', '=', code)])

        if not countries:
            return cls.raise_user_error(
                "country_not_found", error_args=(code, )
            )

        return countries[0]


class Subdivision:
    "Subdivision"
    __name__ = 'country.subdivision'

    @classmethod
    def search_using_magento_region(cls, region, country):
        """
        Searches for state with given magento region.
        Magento does not send state code but it just sends region name
        thats why subdivisions here are searched using a case insensitive
        search

        :param region: Name of state from magento
        :param country: Active record of country
        :return: Active record of state if found else raises error
        """
        subdivisions = cls.search([
            ('name', 'ilike', region),
            ('country', '=', country.id),
        ])

        # TODO: Exception need be created if subdivison does not exist.

        return subdivisions and subdivisions[0] or None
