from SPARQLWrapper import SPARQLWrapper,JSON

sparql = SPARQLWrapper('http://www.your-url.com/path-to-sparql-endpoint')
sparql.setReturnFormat(JSON)

sparql.setQuery("""
INSERT DATA {
<https://test.com/s> <https://test.com/p> <https://test.com/o> .
}""")

sparql.method = 'POST'
sparql.query()

print("<https://test.com/s> <https://test.com/p> <https://test.com/o> inserted")
