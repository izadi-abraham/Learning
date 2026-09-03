

## TypeSpec
The source of truth, A small language where you describe your data models and APIs once (a .tsp file) and everything else is generated from it by emitters, so the shapes can never drift apart.


## OpenAPI
The standard format for describing REST APIs (endpoints, request/response shapes). One of the generated outputs out of the TypeSpec/.tsp files. Used for the REST side, docs, and clients.


## OpenSearch
The search database (an ElasticSearch fork). The index-writer lambda (in our specific scenario) write documents into it so the UI gets fast text search, filters and counts.

### Document 
A document in OpenSearch is basically equal to a row in postgreSql table.

## GraphQL
The query language the Single Page Application speaks to the "Search API (in our specific scenario)". The browser asks for exactly the fields it wants.

### GraphQL resolver
The GraphQL resolvers then translate the GraphQL query into OpenSearch queries.

### GraphQL SDL
Schema Definition Language


### Code Artifacts
AWS's private npm registry. CI publishes the generated packages in CodeArtifact with version numbers, and each consumer pins the version it builds against.

```text
TypeSpec --> Emitters generate --> OpenAPI (REST) + OpenSearch mappings + GraphQL schema/resolver + TS types --> Published to CodeArtifacts
--> Services pin & deploy them
```

### Zod
Zod helps to do runtime validation. Zod schemas will check actual incomming data.
TypeScript checks at compile time (does the code fit together?), then it's type are erased from the running JavaScript. Zod checks at runtime (does this actual value, comming from outside, match?).
Wherever data enters from a place the compiler can't see - API responses, form input, workflow tokens, queue messages, Zod can validate.
Zod can derive a TypeScript type from a schema like `CounterpartyParamsSchema`, (z.infer), so the compile-time and runtime definitions can never drift apart.
