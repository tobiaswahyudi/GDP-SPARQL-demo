from SPARQLWrapper import SPARQLWrapper,JSON

sparql = SPARQLWrapper('http://www.your-url.com/path-to-sparql-endpoint')
sparql.setReturnFormat(JSON)

sparql.setQuery("""select ?h ?t where {?h <http://dbpedia.org/ontology/starring> ?t} LIMIT 10""")

res = sparql.query().convert()

h = [hrt['h']['value'] for hrt in res['results']['bindings']]
t = [hrt['t']['value'] for hrt in res['results']['bindings']]

ln = max([len(x) for x in h])

for idx,hd in enumerate(h):
    print(hd," "*(ln-len(hd))," --{starring}--> ",t[idx],sep="")

