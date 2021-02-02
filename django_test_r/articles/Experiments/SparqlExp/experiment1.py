'''
This is the SWRL query used in the existing application. I am using it as the baseline.

'''


from rdflib import Graph, URIRef

g = Graph()
g.parse("/Users/redwanwalid/Desktop/redwan/django_test_r/EHROntology_v2.owl")
# print(g)

# makeSub = "http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#" + str(doctorName)
makeSub = "http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#" + str(Richard)
# makeSub = "http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#Richard"
# print(makeSub)
sub = URIRef(makeSub)
# print(sub)

res = []
for triple in g.triples((sub, None, None)):
    print(triple)
    print(triple[1])
    p = triple[1].split('#')[1]
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