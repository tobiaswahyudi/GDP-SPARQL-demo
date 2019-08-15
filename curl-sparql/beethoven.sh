curl -X POST --data-binary 'query=\
PREFIX nav: <http://purl.org/ontology/classicalmusicnav#> \
PREFIX comp: <http://dbtune.org/classical/resource/composer/> \
PREFIX mo: <http://purl.org/ontology/mo/> \
PREFIX foaf: <http://xmlns.com/foaf/0.1/> \
select ?compName (SAMPLE (?title) as ?title) \
where {\
  ?comp nav:influencedBy comp:beethoven_ludwig_van.\
  ?comp foaf:name ?compName.\
  ?event mo:composer ?comp.\
  ?event mo:produced_work ?work.\
  ?work <http://purl.org/dc/elements/1.1/title> ?title.\
}\
 GROUP BY ?compName\
 limit 10'\
http://www.your-url.com/path-to-sparql-endpoint 
