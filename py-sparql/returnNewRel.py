from SPARQLWrapper import SPARQLWrapper,JSON

sparql = SPARQLWrapper('http://www.your-url.com/path-to-sparql-endpoint')
sparql.setReturnFormat(JSON)

sparql.setQuery("""
PREFIX test: <https://tiest.com/>
select ?s ?p ?o {
?s ?p ?o.
VALUES ?s {<https://test.com/s>}.
VALUES ?p {<https://test.com/p>}.
VALUES ?o {<https://test.com/o>}.
}""")

res = sparql.query().convert()

print(res)
