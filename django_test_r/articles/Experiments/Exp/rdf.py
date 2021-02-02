'''
from rdflib import Graph, URIRef

g = Graph()
g.parse("/Users/redwanwalid/Desktop/redwan/test.owl")
print(g)

#makeSub = "http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#" + str('Elizabeth')
makeSub = "http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#"
print(makeSub)
sub 	= URIRef(makeSub)
print(sub)

res = []
for triple in g.triples((sub,None,None)):
	p 	= triple[1].split('#')[1]
	if (p.startswith('can')):
		permission = str(p[3])
		if (permission == 'M'):
			field = str(p[9:])
		else:
			field = str(p[7:])

		if (field and permission):
			if field != 'VitalStats':
				res.append((field, permission))

'''
# http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#Patient
# from rdflib import Namespace
# from rdflib import Graph, URIRef, Literal, RDF

# g = Graph()
# g.parse("/Users/redwanwalid/Desktop/redwan/test.owl")
#g.open("/Users/redwanwalid/Desktop/redwan/test.owl")
# makeSub = "http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#Lynda"
#makeSub = "http://www.w3.org/2002/07/owl#NamedIndividual#Lynda"
# sub = URIRef(makeSub)
#
# for triple in g.triples((sub,None,None)):
#for triple in g:
    #print(sub)
    #p = triple[2]
    #print((triple[0], triple[1], triple[2]))
    #print(p)
    #p = triple[2].split('#')[1]
    #print(p)

# for s, p, o in g:
#     print((s, p, o))

# for s, p, o in g.triples((Ron, None, None)):
#     print((s, p, o))
#


# from rdflib import URIRef, BNode, Literal
#
# bob = URIRef("http://example.org/people/Bob")
# linda = BNode()  # a GUID is generated
#
# name = Literal('Bob')  # passing a string
# age = Literal(24)  # passing a python int
# height = Literal(76.5)  # passing a python float
#
#
# from rdflib import Namespace
#
# n = Namespace("http://example.org/people/")
#
# n.bob  # = rdflib.term.URIRef(u'http://example.org/people/bob')
# n.eve  # = rdflib.term.URIRef(u'http://example.org/people/eve')
#
# from rdflib.namespace import FOAF, RDF
#
# RDF.type
# # = rdflib.term.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")
#
# FOAF.knows
# # = rdflib.term.URIRef("http://xmlns.com/foaf/0.1/knows")
#
# #PROF.isProfileOf
# # = rdflib.term.URIRef("http://www.w3.org/ns/dx/prof/isProfileOf")
#
# #SOSA.Sensor
# # = rdflib.term.URIRef("http://www.w3.org/ns/sosa/Sensor")
#
# from rdflib import Graph
# g = Graph()
# g.bind("foaf", FOAF)
#
# g.add((bob, RDF.type, FOAF.Person))
# g.add((bob, FOAF.name, name))
# g.add((bob, FOAF.knows, linda))
# g.add((linda, RDF.type, FOAF.Person))
# g.add((linda, FOAF.name, Literal("Linda")))
#
# print(g.serialize(format="turtle").decode("utf-8"))

# from owlready2 import *
#
# onto = get_ontology("/Users/redwanwalid/Desktop/redwan/test.owl").load()
#
# with onto:
#     class Drug(Thing):
#         def take(self): print("I took a drug")
#     class ActivePrinciple(Thing):
#         pass
#     class has_for_active_principle(Drug >> ActivePrinciple):
#         python_name = "active_principles"
#     class Placebo(Drug):
#         equivalent_to = [Drug & Not(has_for_active_principle.some(ActivePrinciple))]
#         def take(self): print("I took a placebo")
#     class SingleActivePrincipleDrug(Drug):
#         equivalent_to = [Drug & has_for_active_principle.exactly(1, ActivePrinciple)]
#         def take(self): print("I took a drug with a single active principle")
#     class DrugAssociation(Drug):
#         equivalent_to = [Drug & has_for_active_principle.min(2, ActivePrinciple)]
#         def take(self): print("I took a drug with %s active principles" % len(self.active_principles))
#     class Man(Thing):
#         pass
#     class test()
#         pass

# acetaminophen   = ActivePrinciple("acetaminophen")
# amoxicillin     = ActivePrinciple("amoxicillin")
# clavulanic_acid = ActivePrinciple("clavulanic_acid")
#
# AllDifferent([acetaminophen, amoxicillin, clavulanic_acid])
#
# drug1 = Drug(active_principles = [acetaminophen])
# drug2 = Drug(active_principles = [amoxicillin, clavulanic_acid])
# drug3 = Drug(active_principles = [])
#
# close_world(Drug)



# from rdflib import Graph, URIRef
# from faker import Faker
# fake = Faker()

# g.parse("/Users/redwanwalid/Desktop/redwan/test.owl")
# g = Graph()

# for x in range(2):
#     Faker.seed(x)
#     Person = fake.name().split(' ')[0]
#     print(Person)
#     Person = Man(Person)
#     x = x + 1
#
# onto.save(file = "test.owl", format = "rdfxml")



# http://www.w3.org/2002/07/owl#NamedIndividual
# http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#PatientName
# http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#DoctorName
# http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#getsTreatedby
# http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#Patient
# http://www.w3.org/1999/02/22-rdf-syntax-ns#type

# Reference link for final code: https://owlready2.readthedocs.io/en/latest/reasoning.html http://owlready2.readthedocs.io
#---------Final Code-----------
from owlready2 import *

onto = get_ontology("/Users/redwanwalid/Desktop/redwan/django_test_r/EHROntology.owl").load()

with onto:
    #Creating Patient Class
    class Patient(Thing):
        pass

from faker import Faker
fake = Faker()

for x in range(5000):
    Faker.seed(x)
    #Extracting first name of 100 peopler
    Person = fake.name().split(' ')[0]
    print(Person)
    #Adding it into Patient instance
    Person = Patient(Person)
    x = x + 1

onto.save(file = "EHROntology_v2.owl", format = "rdfxml")

# filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/articles/examplePickle'
# f = open(filepath, 'r')
# filecontents = f.read()
# print(filecontents)
#
# from charm.core.engine.util import objectToBytes, bytesToObject
# from charm.toolbox.pairinggroup import PairingGroup
# import pickle
#
# pairing_group = PairingGroup('SS512')
#
# a = objectToBytes(filecontents, pairing_group)
# print(a)
# print(type(a))
#
# b = bytesToObject(a, pairing_group)
# print(b)
# print(type(b))
#
# msg = pairing_group.hash(a)
# #msg = pickle.dumps(a)
# print(msg)
# print(type(msg))
#
# act = pairing_group.serialize(msg)
# print(act)
#
# final = bytesToObject(act, pairing_group)
# print(final)

#pickle.dump(bytes, open(examplePickle, 'wb'))