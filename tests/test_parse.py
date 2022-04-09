import unittest

import common
import parse

class test_FGItemDescriptor_hook(unittest.TestCase):
    def test_happy(self):
        # Given
        good_item = {
            'ClassName': 'Desc_NuclearWaste_C',
            'mDisplayName': 'Uranium Waste',
            'mDescription': 'The by-product of consuming Uranium Fuel '
                            'Rods in the Nuclear Power Plant.\r\nNon-fissible '
                            'Uranium can be extracted. Handle with caution.'
                            '\r\n\r\nCaution: HIGHLY Radioactive.'
            }

        # When
        result = parse.FGItemDescriptor_hook(good_item)

        # Then
        print(result)
        self.assertIsNotNone(result)