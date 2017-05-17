#
#  https://pypi.python.org/pypi/pysolr/3.5.0#downloads
#

import sys
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/', timeout=10)
solr.add([
{
        "id": "doc_1",
        "title": "A test document",
    },
    {
        "id": "doc_2",
        "title": "The Banana: Tasty or Dangerous?",
    },
])


results = solr.search('book')
#print("Saw {0} result(s).".format(len(results)))
for result in results:
    print("The title is '{0}'.".format(result['id']))

solr.delete(id='doc_2')
