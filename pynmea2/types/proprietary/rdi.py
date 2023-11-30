from ... import ProprietarySentence, nmea_utils
from datetime import datetime


class RDI(ProprietarySentence):
    sentence_types = {}

    def __new__(_cls, manufacturer, data):
        name = manufacturer + data[0]
        cls = _cls.sentence_types.get(name, _cls)
        return super(RDI, cls).__new__(cls)

    def __init__(self, manufacturer, data):
        self.sentence_type = manufacturer + data[0]
        super(RDI, self).__init__(manufacturer, data[1:])

    def identifier(self):
        return 'P%s,' % self.sentence_type


class RDIG(RDI):
    # Example
    # $PRDIG, H, 197.34, P, -10.2, R, -11.5, D, 122.7,7*7E

    fields = (
        ('Heading ID', 'head_id'),
        ('Heading', 'heading', float),
        ('Pitch ID', 'pitch_id'),
        ('Pitch', 'pitch', float),
        ('Roll ID', 'roll_id'),
        ('Roll', 'roll', float),
        ('Depth ID', 'depth_id'),
        ('Depth', 'depth', float)
    )


class RDIH(RDI):
    # Example
    # $PRDIH, R, 143.2, S, 1.485, C, 192.93*17

    fields = (
        ('Range to bottom ID', 'altitude_id'),
        ('Range to bottom', 'altitude', float),
        ('Speed over ground ID', 'sv_id'),  # surface speed
        ('Speed over ground', 'sv', float),
        ('Course over ground ID', 'sh_id'),  # surface heading
        ('Course over ground', 'sh', float)
    )


class RDII(RDI):
    # Example
    # $PRDII, S, 1.503, C, 203.5*55

    fields = (
        ('Speed relative to current ID', 'rv_id'),  # relative velocity
        ('Speed relative to current', 'rv', float),
        ('Course relative to current ID', 'rh_id'),  # relative heading
        ('Course relative to current', 'rh', float)
    )
