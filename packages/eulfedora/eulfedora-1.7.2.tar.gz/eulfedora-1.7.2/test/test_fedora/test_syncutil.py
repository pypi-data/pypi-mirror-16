import hashlib
import logging
from lxml import etree
from mock import Mock, patch
import os
import requests
import unittest
from six.moves.urllib.request import url2pathname

from eulfedora.models import DigitalObject
from eulfedora.server import Repository
from eulfedora.syncutil import ArchiveExport, endswith_partial, \
    binarycontent_sections
from eulfedora.util import md5sum
from test.test_fedora.base import FIXTURE_ROOT


logger = logging.getLogger(__name__)

FIXTURES = {
    'sync1_export': os.path.join(FIXTURE_ROOT, 'synctest1-export.xml'),
    'sync2_export': os.path.join(FIXTURE_ROOT, 'synctest2-export.xml')
}

class ArchiveExportTest(unittest.TestCase):


    def setUp(self):
        # todo: use mocks?
        self.repo = Mock(spec=Repository)
        self.obj = Mock() #spec=DigitalObject)
        self.obj.pid = 'synctest:1'
        self.archex = ArchiveExport(self.obj, self.repo)

        # set up a request session that can load file uris, so
        # fixtures can be used as export data
        self.session = requests.session()
        self.session.mount('file://', LocalFileAdapter())

    def test_get_datastream_info(self):
        dsinfo = self.archex.get_datastream_info('''<foxml:datastreamVersion ID="DC.2" LABEL="Dublin Core" CREATED="2012-10-11T14:13:03.658Z" MIMETYPE="text/xml" FORMAT_URI="http://www.openarchives.org/OAI/2.0/oai_dc/" SIZE="771">
<foxml:contentDigest TYPE="MD5" DIGEST="f53aec07f2607f536bac7ee03dbbfe7c"/>''')
        self.assertEqual('DC.2', dsinfo['id'])
        self.assertEqual('text/xml', dsinfo['mimetype'])
        self.assertEqual('771', dsinfo['size'])
        self.assertEqual('MD5', dsinfo['type'])
        self.assertEqual('f53aec07f2607f536bac7ee03dbbfe7c', dsinfo['digest'])
        self.assertEqual('2012-10-11T14:13:03.658Z', dsinfo['created'])

        # datastream info split across chunks
        self.archex.end_of_last_chunk = '''<foxml:datastreamVersion ID="DC.2" LABEL="Dublin Core" CREATED="2012-10-11T14:13:03.658Z" MIMETYPE="te'''
        dsinfo = self.archex.get_datastream_info('''xt/xml" FORMAT_URI="http://www.openarchives.org/OAI/2.0/oai_dc/" SIZE="771">
<foxml:contentDigest TYPE="MD5" DIGEST="f53aec07f2607f536bac7ee03dbbfe7c"/>''')
        self.assertEqual('DC.2', dsinfo['id'])
        self.assertEqual('text/xml', dsinfo['mimetype'])
        self.assertEqual('f53aec07f2607f536bac7ee03dbbfe7c', dsinfo['digest'])

        # sample etd record with longer datastream info
        etd_ds = '''</foxml:datastreamVersion><foxml:datastreamVersion ID="RELS-EXT.9" LABEL="Relationships to other objects" CREATED="2009-09-18T19:36:04.235Z" MIMETYPE="application/rdf+xml" FORMAT_URI="info:fedora/fedora-system:FedoraRELSExt-1.0" SIZE="716">
<foxml:contentDigest TYPE="MD5" DIGEST="168fb675e5fcded1a3b8cc7251877744"/>'''

        self.archex.end_of_last_chunk = ''
        dsinfo = self.archex.get_datastream_info(etd_ds)
        self.assertEqual('RELS-EXT.9', dsinfo['id'])
        self.assertEqual('application/rdf+xml', dsinfo['mimetype'])
        self.assertEqual('716', dsinfo['size'])
        self.assertEqual('MD5', dsinfo['type'])
        self.assertEqual('168fb675e5fcded1a3b8cc7251877744', dsinfo['digest'])

        # getting audit record id instead of datastream id
        audit_trail_dsinfo = '''<audit:record ID="AUDREC48">
<audit:process type="Fedora API-M"/>
<audit:action>modifyDatastreamByValue</audit:action>
<audit:componentID>RELS-EXT</audit:componentID>
<audit:responsibility>fedoraAdmin</audit:responsibility>
<audit:date>2016-07-09T10:31:50.971Z</audit:date>
<audit:justification>datastream fixity check</audit:justification>
</audit:record>
</audit:auditTrail>
</foxml:xmlContent>
</foxml:datastreamVersion>
</foxml:datastream>
<foxml:datastream ID="content" STATE="A" CONTROL_GROUP="M" VERSIONABLE="false">
<foxml:datastreamVersion ID="content.0" LABEL="1199disk3" CREATED="2014-04-30T17:30:06.949Z" MIMETYPE="application/x-aff" SIZE="1277">
<foxml:contentDigest TYPE="MD5" DIGEST="2271e4a2678f69ce3f4a97ab07c06cbe"/>
<foxml:binaryContent>'''
        dsinfo = self.archex.get_datastream_info(audit_trail_dsinfo)
        self.assertEqual('content.0', dsinfo['id'])
        self.assertEqual('application/x-aff', dsinfo['mimetype'])
        self.assertEqual('1277', dsinfo['size'])
        self.assertEqual('MD5', dsinfo['type'])
        self.assertEqual('2271e4a2678f69ce3f4a97ab07c06cbe', dsinfo['digest'])

        # chunk contains multiple ds ids
        multi_dsinfo = '''</foxml:binaryContent>
</foxml:datastreamVersion>
<foxml:datastreamVersion ID="MODS.1" LABEL="MODS Metadata" CREATED="2015-06-24T17:26:39.154Z" MIMETYPE="text/xml" FORMAT_URI="http://www.loc.gov/mods/v3" SIZE="345">
<foxml:contentDigest TYPE="MD5" DIGEST="3d866951c5d2f4e665fd518a8d9433f2"/>
<foxml:binaryContent>

</foxml:datastreamVersion>
</foxml:datastream>
<foxml:datastream ID="VIDEO" STATE="A" CONTROL_GROUP="M" VERSIONABLE="true">
<foxml:datastreamVersion ID="VIDEO.0" LABEL="tape3" CREATED="2015-06-23T16:43:39.107Z" MIMETYPE="video/quicktime" SIZE="433279317">
<foxml:contentDigest TYPE="MD5" DIGEST="4fb5a23ee4c5d17cbd8b6d1f73fc6b8e"/>
'''
        dsinfo = self.archex.get_datastream_info(multi_dsinfo)
        self.assertEqual('VIDEO.0', dsinfo['id'])
        self.assertEqual('video/quicktime', dsinfo['mimetype'])
        self.assertEqual('433279317', dsinfo['size'])
        self.assertEqual('MD5', dsinfo['type'])
        self.assertEqual('4fb5a23ee4c5d17cbd8b6d1f73fc6b8e', dsinfo['digest'])

    def test_object_data(self):
        # mock api to read export data from a local fixture filie
        response = self.session.get('file://%s' % FIXTURES['sync1_export'])
        mockapi = Mock()
        def mock_upload(data, *args, **kwargs):
            list(data)  # consume the generator so datastream processing happens
            return 'uploaded://1'

        mockapi.upload = mock_upload
        mockapi.export.return_value = response
        mockapi.base_url = 'http://fedora.example.co/fedora'
        self.obj.api = self.repo.api = mockapi
        data = self.archex.object_data()
        foxml = data.getvalue()

        self.assert_(etree.XML(foxml) is not None,
            'object data should be valid xml')
        self.assert_(b'foxml:binaryContent' not in foxml,
            'object data for ingest should not include binaryContent tags')
        self.assert_(b'<foxml:contentLocation REF="uploaded://1" TYPE="URL"/>' in foxml,
            'object data for ingest should include upload id as content location')

        # other tests?

        # set read block size artificially low to test chunked handling
        self.archex = ArchiveExport(self.obj, self.repo)
        self.archex.read_block_size = 1024
        data = self.archex.object_data()
        foxml = data.getvalue()

        self.assert_(etree.XML(foxml) is not None,
            'object data should be valid xml')
        self.assert_(b'foxml:binaryContent' not in foxml,
            'object data for ingest should not include binaryContent tags')
        self.assert_(b'<foxml:contentLocation REF="uploaded://1" TYPE="URL"/>' in foxml,
            'object data for ingest should include upload id as content location')

        # test with second fixture - multiple small encoded datastreams
        self.archex = ArchiveExport(self.obj, self.repo)
        self.archex.read_block_size = 1024
        response = self.session.get('file://%s' % FIXTURES['sync2_export'])
        mockapi.export.return_value = response
        data = self.archex.object_data()
        foxml = data.getvalue()

        self.assert_(etree.XML(foxml) is not None,
            'object data should be valid xml')
        self.assert_(b'foxml:binaryContent' not in foxml,
            'object data for ingest should not include binaryContent tags')
        self.assert_(b'<foxml:contentLocation REF="uploaded://1" TYPE="URL"/>' in foxml,
            'object data for ingest should include upload id as content location')

    def test_object_data_split_bincontent(self):
        # explictly test handling of binary content tag split over
        # chunk boundaries

        response = self.session.get('file://%s' % FIXTURES['sync1_export'])
        mockapi = Mock()
        def mock_upload(data, *args, **kwargs):
            list(data)  # consume the generator so datastream processing happens
            return 'uploaded://1'

        mockapi.upload = mock_upload
        mockapi.export.return_value = response
        self.obj.api = self.repo.api = mockapi

        # test binary content tag split across chunks
        self.archex = ArchiveExport(self.obj, self.repo)
        # use a block size that will split the fixture in the middle of
        # the first binary content tag
        self.archex.read_block_size = 2688
        data = self.archex.object_data()
        foxml = data.getvalue()

        self.assert_(etree.XML(foxml) is not None,
            'object data should be valid xml')
        self.assert_(b'foxml:binaryContent' not in foxml,
            'object data for ingest should not include binaryContent tags')

        self.archex = ArchiveExport(self.obj, self.repo)
        # this blocksize ends with just the < in foxml:binaryContent
        self.archex.read_block_size = 2680
        data = self.archex.object_data()
        foxml = data.getvalue()
        self.assert_(etree.XML(foxml) is not None,
            'object data should be valid xml')
        self.assert_(b'foxml:binaryContent' not in foxml,
            'object data for ingest should not include binaryContent tags')

        self.archex = ArchiveExport(self.obj, self.repo)
        # this blocksize ends with an unrelated close tag </
        self.archex.read_block_size = 1526
        data = self.archex.object_data()
        foxml = data.getvalue()
        self.assert_(etree.XML(foxml) is not None,
            'object data should be valid xml')
        self.assert_(b'foxml:binaryContent' not in foxml,
            'object data for ingest should not include binaryContent tags')


    def test_encoded_datastream(self):
        # data content within a single chunk of data
        mockapi = Mock()
        mockapi.export.return_value = self.session.get('file://%s' % FIXTURES['sync1_export'])
        mockapi.upload.return_value = 'uploaded://1'
        self.obj.api = self.repo.api = mockapi

        section = self.archex.get_next_section()
        # get binary datastream info from first section
        dsinfo = self.archex.get_datastream_info(section)
        # fixture only has one binary content block
        # get binarycontent tag out of the way
        self.archex.get_next_section()
        # next section will be file contents
        self.archex.within_file = True
        dscontent = b''.join(self.archex.encoded_datastream())
        # check decoded size and MD5 match data from fixture
        self.assertEqual(int(dsinfo['size']), len(dscontent))
        self.assertEqual(dsinfo['digest'], md5sum(dscontent))

        # data content across multiple chunks
        mockapi.export.return_value = self.session.get('file://%s' % FIXTURES['sync1_export'])
        self.obj.api = self.repo.api = mockapi
        # set read block size artificially low to ensure
        # datastream content is spread across multiple chunks
        self.archex.read_block_size = 1024

        finished = False
        # iterate through the data, similar to object_data method,
        # but only handle binary content
        while not finished:
            try:
                section = self.archex.get_next_section()
            except StopIteration:
                finished = True

            # find the section with starting binary content
            if section == '<foxml:binaryContent>':
                # then decode the subsequent content
                self.archex.within_file = True
                dscontent = ''.join(self.archex.encoded_datastream())

                self.assertEqual(int(dsinfo['size']), len(dscontent))
                self.assertEqual(dsinfo['digest'], md5sum(dscontent))

                # stop processing
                finished = True

class UtilsTest(unittest.TestCase):

    def test_endswith_partial(self):
        test_string = '<foxml:binaryContent>'

        test_len = 19
        txt = 'some content %s' % test_string[:test_len]
        len_overlap = endswith_partial(txt, test_string)
        self.assertEqual(test_len, len_overlap)

        test_len = 5
        txt = 'some content %s' % test_string[:test_len]
        len_overlap = endswith_partial(txt, test_string)
        self.assertEqual(test_len, len_overlap)

        test_len = 1
        txt = 'some content %s' % test_string[:test_len]
        len_overlap = endswith_partial(txt, test_string)
        self.assertEqual(test_len, len_overlap)

        # no overlap
        self.assertFalse(endswith_partial('some content', test_string))

    def test_binarycontent_sections(self):
        with open(FIXTURES['sync1_export'], 'rb') as sync1data:
            sections = list(binarycontent_sections(sync1data.read()))
            self.assertEqual(5, len(sections))
            self.assertEqual(b'<foxml:binaryContent>', sections[1])
            self.assertEqual(b'</foxml:binaryContent>', sections[3])

        with open(FIXTURES['sync2_export'], 'rb') as sync1data:
            sections = list(binarycontent_sections(sync1data.read()))
            # second fixture should break into 17 sections
            self.assertEqual(17, len(sections))
            self.assertEqual(b'<foxml:binaryContent>', sections[1])
            self.assertEqual(b'</foxml:binaryContent>', sections[3])
            self.assertEqual(b'<foxml:binaryContent>', sections[5])
            self.assertEqual(b'</foxml:binaryContent>', sections[7])
            self.assertEqual(b'<foxml:binaryContent>', sections[9])
            self.assertEqual(b'</foxml:binaryContent>', sections[11])
            self.assertEqual(b'<foxml:binaryContent>', sections[13])
            self.assertEqual(b'</foxml:binaryContent>', sections[15])

# requests file uri adapter, thanks to
# http://stackoverflow.com/questions/10123929/python-requests-fetch-a-file-from-a-local-url
class LocalFileAdapter(requests.adapters.BaseAdapter):
    """Protocol Adapter to allow Requests to GET file:// URLs

    @todo: Properly handle non-empty hostname portions.
    """

    @staticmethod
    def _chkpath(method, path):
        """Return an HTTP status for the given filesystem path."""
        if method.lower() in ('put', 'delete'):
            return 501, "Not Implemented"  # TODO
        elif method.lower() not in ('get', 'head'):
            return 405, "Method Not Allowed"
        elif os.path.isdir(path):
            return 400, "Path Not A File"
        elif not os.path.isfile(path):
            return 404, "File Not Found"
        elif not os.access(path, os.R_OK):
            return 403, "Access Denied"
        else:
            return 200, "OK"

    def send(self, req, **kwargs):  # pylint: disable=unused-argument
        """Return the file specified by the given request

        @type req: C{PreparedRequest}
        @todo: Should I bother filling `response.headers` and processing
               If-Modified-Since and friends using `os.stat`?
        """
        path = os.path.normcase(os.path.normpath(url2pathname(req.path_url)))
        response = requests.Response()

        response.status_code, response.reason = self._chkpath(req.method, path)
        if response.status_code == 200 and req.method.lower() != 'head':
            try:
                response.raw = open(path, 'rb')
            except (OSError, IOError) as err:
                response.status_code = 500
                response.reason = str(err)

        if isinstance(req.url, bytes):
            response.url = req.url.decode('utf-8')
        else:
            response.url = req.url

        response.request = req
        response.connection = self

        return response

    def close(self):
        pass

