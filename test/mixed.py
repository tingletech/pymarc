from unittest import TestCase, makeSuite

import os
import codecs

from pymarc import marc8_to_unicode, Field, Record, MARCReader, MARCWriter

class MixedTest(TestCase):
    
    def test_edit_mixed_code(self):
        reader = MARCReader(
            file('test/mixed-code.dat'), 
            to_unicode=True, 
            force_utf8=True, 
            utf8_handling='ignore'
        )
        writer = MARCWriter(open('test/foo', 'w'))
        for record in reader:
            field = Field(
                tag = '941',
                indicators = ['',''],
                subfields = [ 'a', 'x' ]
            )
            record.add_field(field)
            writer.write(record)
        writer.close()
        reader = MARCReader(open('test/foo'), to_unicode=True)
        for record in reader:
            self.assertEquals(type(record), Record)
        os.remove('test/foo')


def suite():
    test_suite = makeSuite(MixedTest, 'test')
    return test_suite 
