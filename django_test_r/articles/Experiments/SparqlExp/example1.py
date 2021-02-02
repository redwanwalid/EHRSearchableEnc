# SELECT query
# from SPARQLWrapper import SPARQLWrapper, JSON
#
# sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# sparql.setQuery("""
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#     SELECT ?label
#     WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
# """)
# sparql.setReturnFormat(JSON)
# results = sparql.query().convert()
#
# for result in results["results"]["bindings"]:
#     print(result["label"]["value"])


# ASK query
# from SPARQLWrapper import SPARQLWrapper, XML
#
# sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# sparql.setQuery("""
#     ASK WHERE {
#         <http://dbpedia.org/resource/Asturias> rdfs:label "Asturias"@es
#     }
# """)
#
# sparql.setReturnFormat(XML)
# results = sparql.query().convert()
# print(results.toxml())


# CONSTRUCT query
# from SPARQLWrapper import SPARQLWrapper, XML
# from rdflib import Graph
#
# sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# sparql.setQuery("""
#     PREFIX dbo: <http://dbpedia.org/ontology/>
#     PREFIX schema: <http://schema.org/>
#     CONSTRUCT {
#       ?lang a schema:Language ;
#       schema:alternateName ?iso6391Code .
#     }
#     WHERE {
#       ?lang a dbo:Language ;
#       dbo:iso6391Code ?iso6391Code .
#       FILTER (STRLEN(?iso6391Code)=2) # to filter out non-valid values
#     }
# """)
#
# sparql.setReturnFormat(XML)
# results = sparql.query().convert()
# print(results.serialize(format='xml'))


# DESCRIBE query
from SPARQLWrapper import SPARQLWrapper, N3
from rdflib import Graph

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    DESCRIBE <http://dbpedia.org/resource/Asturias>
""")

sparql.setReturnFormat(N3)
results = sparql.query().convert()
g = Graph()
g.parse(data=results, format="n3")
print(g.serialize(format='n3'))