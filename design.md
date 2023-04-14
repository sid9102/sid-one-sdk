## Core Interface
While thinking of a design paradigm for the SDK, I was torn between a resource based interface and a client based one.
For example, querying for all movies could be done with either of the following:
```python
client.get_all(Movie)
```
or
```python
Movie.get_all()
```

I decided to go with the former because it allows for less repeated code. You'll note that the model files for both 
`Movie` and `Quote` are very small, only covering the fields of each model. The `get_all` and `get_instance` methods
take in the class that you're querying for as an argument, making it trivial to add additional models.

Also, this allows the user to have explicit control over instantiating the client with an API key. An alternative design
would be to have a singleton client that is instantiated with the API key, enabling more resource oriented queries.

Were this a production SDK I would have allowed for both styles of querying for maximum flexibility.
## Caveats
- I can only do so much with a broken API! For example, if an entity is not found, 
the server returns a 500 rather than a 404. 
- With more time I would have added
much more error handling and validation, as well as more detailed errors for the user of the SDK.