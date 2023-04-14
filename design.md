## Design Overview

The SDK is designed with maintainability, extensibility, and readable code in mind. The main components of the SDK are the `OneApiClient` class, the model classes (e.g., `Movie` and `Quote`), and the `Filter` class.

## Core Interface

Two design paradigms were considered for the SDK: a resource-based interface and a client-based interface.

In the resource-based interface, querying for all movies would be done like this:

```python
Movie.get_all()
```

In the client-based interface, the same query would look like this:

```python
client.get_all(Movie)
```

The client-based interface was chosen for the following reasons:

- Less repeated code: The model files for `Movie` and `Quote` are small, only covering the fields of each model. The `get_all` and `get_instance` methods take in the class that you're querying for as an argument, making it trivial to add additional models.
- Explicit control over client instantiation: Users can instantiate the client with an API key, allowing for better control over authentication, or even multiple clients at the same time.

An alternative design would be to have a singleton client that is instantiated with the API key, enabling more resource-oriented queries. If this were a production SDK, both styles of querying would be supported for maximum flexibility.

## Error Handling and Validation

Due to limitations in the API and time constraints, the SDK has some caveats:

- Inadequate error handling: The API returns a 500 status code instead of a 404 when an entity is not found. More detailed error handling and validation would be added in a production SDK.
- Limited user-facing errors: More informative error messages would be provided to users in a production SDK.

## Extensibility and Future Work

The current SDK design allows for easy extension to support additional API endpoints and features. Some possible future improvements include:

- Adding more models for other API endpoints.
- Implementing a resource-based interface for more flexible querying.
- Adding caching mechanisms to improve performance.

Overall, the SDK is designed with a focus on clean code, ease of use, and extensibility to support a wide range of use cases and requirements.