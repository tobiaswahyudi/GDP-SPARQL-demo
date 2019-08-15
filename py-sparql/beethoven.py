from SPARQLWrapper import SPARQLWrapper,JSON

sparql = SPARQLWrapper('http://www.your-url.com/path-to-sparql-endpoint')
sparql.setReturnFormat(JSON)

sparql.setQuery("""
PREFIX nav: <http://purl.org/ontology/classicalmusicnav#>
PREFIX comp: <http://dbtune.org/classical/resource/composer/>
PREFIX mo: <http://purl.org/ontology/mo/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

select ?compName (SAMPLE (?xx) as ?title) where {
  ?comp nav:influencedBy comp:beethoven_ludwig_van.
  ?comp foaf:name ?compName.
  ?event mo:composer ?comp.
  ?event mo:produced_work ?work.
  ?work <http://purl.org/dc/elements/1.1/title> ?xx. 
} GROUP BY ?compName limit 10""")

res = sparql.query().convert()

comps = [spo['compName']['value'] for spo in res['results']['bindings']]
titles = [spo['title']['value'] for spo in res['results']['bindings']]

mxln = max([len(x) for x in comps])

for idx,comp in enumerate(comps):
    print(comp,' '*(mxln-len(comp))," --{composed}--> ",titles[idx])
