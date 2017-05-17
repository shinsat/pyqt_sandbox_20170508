#
#  https://pypi.python.org/pypi/pysolr/3.5.0#downloads
#  http://stackoverflow.com/questions/24415659/how-to-make-atomic-updates-to-solr-using-pysolr

import sys
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/', timeout=10)
# add
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

# search
results = solr.search('book')
#print("Saw {0} result(s).".format(len(results)))
for result in results:
    print("The title is '{0}'.".format(result['id']))

# delete
solr.delete(id='doc_2')

# partial update
doc = {'id':'978-1423103349', 'genre_s':'Science Fantasy'}
solr.add([doc], fieldUpdates={'genre_s':'set'})
