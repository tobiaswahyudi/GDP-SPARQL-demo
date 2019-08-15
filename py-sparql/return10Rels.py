from SPARQLWrapper import SPARQLWrapper,JSON

sparql = SPARQLWrapper('http://www.your-url.com/path-to-sparql-endpoint')
sparql.setReturnFormat(JSON)

sparql.setQuery("""select ?h ?r ?t where {?h ?r ?t} LIMIT 10""")

res = sparql.query().convert()

for hrt in res['results']['bindings']:
    print("<",hrt['h']['value'],">\t--{",hrt['r']['value'],"}--> <",hrt['t']['value'],">",sep="")

