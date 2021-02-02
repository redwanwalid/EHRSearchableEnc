'''
This is SPARQL query code used in the application. This is the test code which was used in the implementation.
'''


import rdflib

g = rdflib.Graph()

import time

start_time = time.perf_counter()

g.parse("/Users/redwanwalid/Desktop/redwan/django_test_r/EHROntology_v2.owl")

# a =     '''SELECT ?predicate WHERE
#     {<http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#'''+str(Richard)'''>
#     ?predicate ?object .}'''

# a = "SELECT ?predicate WHERE {<http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#" + str(1) + "> ?predicate ?object .}"
# print(a)
#
# qres = g.query(a)

qres = g.query('''SELECT ?predicate WHERE {<http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#Richard> ?predicate ?object .}''')

res = []
for row in qres:
    print(row[0])
    # print(type(row))
    p = row[0].split('#')[1]
    print(p)
    if (p.startswith('can')):
        permission = str(p[3])
        if (permission == 'M'):
            field = str(p[9:])
        else:
            field = str(p[7:])

        if (field and permission):
            if field != 'VitalStats':
                res.append((field, permission))
print(res)
print(time.perf_counter() - start_time, "seconds")

# qres = g.query(
#     '''SELECT ?subject ?predicate ?object
#
#         WHERE {
#         ?subject ?predicate ?object
#         }''')
#
# for row in qres:
#     print(row)