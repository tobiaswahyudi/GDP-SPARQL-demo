curl -X POST --data-binary 'query=\
select ?s ?p ?o\
 where {\
    ?s ?p ?o\
}\
limit 10}\
http://www.your-url.com/path-to-sparql-endpoint 
