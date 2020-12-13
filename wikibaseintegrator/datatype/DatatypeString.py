from wikibaseintegrator.wbi_core import BaseDataType, JsonParser


class String(BaseDataType):
    """
    Implements the Wikibase data type 'string'
    """
    DTYPE = 'string'

    def __init__(self, value, prop_nr, is_reference=False, is_qualifier=False, snak_type='value', references=None,
                 qualifiers=None, rank='normal', check_qualifier_equality=True):
        """
        Constructor, calls the superclass BaseDataType
        :param value: The string to be used as the value
        :type value: str
        :param prop_nr: The item ID for this claim
        :type prop_nr: str with a 'P' prefix followed by digits
        :param is_reference: Whether this snak is a reference
        :type is_reference: boolean
        :param is_qualifier: Whether this snak is a qualifier
        :type is_qualifier: boolean
        :param snak_type: The snak type, either 'value', 'somevalue' or 'novalue'
        :type snak_type: str
        :param references: List with reference objects
        :type references: A data type with subclass of BaseDataType
        :param qualifiers: List with qualifier objects
        :type qualifiers: A data type with subclass of BaseDataType
        :param rank: rank of a snak with value 'preferred', 'normal' or 'deprecated'
        :type rank: str
        """

        super(String, self).__init__(value=value, snak_type=snak_type, data_type=self.DTYPE,
                                     is_reference=is_reference, is_qualifier=is_qualifier, references=references,
                                     qualifiers=qualifiers, rank=rank, prop_nr=prop_nr,
                                     check_qualifier_equality=check_qualifier_equality)

        self.set_value(value=value)

    def set_value(self, value):
        assert isinstance(value, str) or value is None, "Expected str, found {} ({})".format(type(value), value)
        self.value = value

        self.json_representation['datavalue'] = {
            'value': self.value,
            'type': 'string'
        }

        super(String, self).set_value(value=value)

    @classmethod
    @JsonParser
    def from_json(cls, jsn):
        if jsn['snaktype'] == 'novalue' or jsn['snaktype'] == 'somevalue':
            return cls(value=None, prop_nr=jsn['property'], snak_type=jsn['snaktype'])
        return cls(value=jsn['datavalue']['value'], prop_nr=jsn['property'])