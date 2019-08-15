curl -X POST --data-binary 'update=\
DELETE DATA \
{\
   <https://test.com/s> <https://test.com/p> <https://test.com/o>.\
}'\
http://www.your-url.com/path-to-sparql-endpoint 
