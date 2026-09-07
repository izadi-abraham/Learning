

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


### Kafka
A durable, ordered event log. Producers append messages to named topics; Consumers read at their own pace. Its job is to let Datahive announce "this counterparty changed" once, and let any number of systems react,
without Datahive knowing or caring who listens.


### Avro
A compact binary message format where the structure (field names, types) lives in a separate schema file (.avsc), not in each message. A message on the wire is just a schema-id + raw bytes - small, fast and validated.
Schemas are versioned in a schema registry, which is houw producers can evolve the record (add a field) without breaking consumers. (contrast JSON: self-describing and human-readable, but bulky and nothing enforces its shape.) 


### Redpanda
Strictly, a Kafka-compatible broker. Redpanda console - a web UI for browsing Kafka: topics, live messages, schemas. So MSK runs the log, Redpanda console is the window into it.


## Kafka vs. SQS
SQS is a simple queue (each message is consumed once, then gone, no history, no ordering gurantees across the queue).
Kafka is a log (message persist, many independent readers, replayable, ordered per partition).


### MSK
Managed Streaming for Kafka: AWS running Kafka for us, so nobody at STX patches Kafka servers. "The MSK cluster" = STX's central Kafka installation.


### SQS - Simple Queue Service


### DLQ - Dead-Letter Queue
Where a message goes after processing fails too manu times, instead of being retried forever or silently lost. It's the "look at me later, human" bin.


### Lambda
A function AWS runs for you on demand. No server, you pay per invocation and it scales automatically.


### VPC - Virtual Private Cloud
Each AWS account's own private network.


### Multi-VPC connectino
Is an MSK-specific feature (built on AWS PrivatLink) that opens one private, purpose-built door from another account's network straight to the Kafka cluster.
(between legacy account - where MSK lives - and the core-services account - where the consumer lambda lives) 
