

## TypeSpec
The source of truth, A small language where you describe your data models and APIs once (a .tsp file) and everything else is generated from it by emitters, so the shapes can never drift apart.


## OpenAPI
The standard format for describing REST APIs (endpoints, request/response shapes). One of the generated outputs out of the TypeSpec/.tsp files. Used for the REST side, docs, and clients.


## OpenSearch
The search database (an ElasticSearch fork). The index-writer lambda (in our specific scenario) write documents into it so the UI gets fast text search, filters and counts.

### Document 
A document in OpenSearch is basically equal to a row in postgreSql table.

## GraphQL
The query language the Single Page Application speaks to the "Search API (in our specific scenario, the search API is the name we give to the AppSync)". The browser asks for exactly the fields it wants.

## GraphQL resolver
The GraphQL resolvers then translate the GraphQL query into OpenSearch queries.
There is only one endpoint (GraphQL client). So in our case there is ` searchApiFetch -> single GraphQL client -> one apiUrl` in `src/api/client.ts`.
Mental model: One endpoint, but each GraphQL field has its own resolver wired to its own data source. When the `POST` arrives, AppSync looks at which fields the operation asks for and routes accordingly.

- `searchCounterparty / CounterpartyProfileById / searchGroup ->` resolvers that query `OpenSearch`. These are projection of COS data - copies kept fresh by change-event - not COS itself.
- `createTask / getTask / advanceActivity ->` lambda resolvers tha call the TLM backend (DynamoDB-backend).

## GraphQL SDL
Schema Definition Language

## AppSync
The AWS's managed GraphQL service. You give the AppSync a schema plus resolvers, and it hosts the endpoint, auth, and routing.

### REST vs. GraphQL
These are two styles of using HTTP:

**REST**: The url names a source and the HTTP verb says what to do to it. `GET /counterparties/{id}` OR `PUT /counterparties/{id}/properties/website`. Each request is self-contained. Many URLs, meaningful verbs and fixed response shapes.
**GraphQL**: Inverts all of that: One URL, always `POST` and the "What do I want moves into the request body" - including which fields to return, chosen by the client per query.
**Neither is better**. They sit at different distances from the user. COS exposes `REST` because it is a `service-to-service` system API. The `SPA` gets `GraphQL` because a UI wants to fetch exactly the fields a screen needs
in one round trip, without knowing which of many services owns what.


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
Managed Streaming for Apache Kafka: AWS running Kafka for us, so nobody at STX patches Kafka servers. "The MSK cluster" = STX's central Kafka installation.


### SQS - Simple Queue Service


### DLQ - Dead-Letter Queue
Where a message goes after processing fails too manu times, instead of being retried forever or silently lost. It's the "look at me later, human" bin.


### Lambda
A function AWS runs for you on demand. No server, you pay per invocation and it scales automatically.


### VPC - Virtual Private Cloud
Each AWS account's own private network.


### Multi-VPC connection
Is an MSK-specific feature (built on AWS PrivatLink) that opens one private, purpose-built door from another account's network straight to the Kafka cluster.
(between legacy account - where MSK lives - and the core-services account - where the consumer lambda lives) 


### CDK - Cloud Development Kit
AWS CDK is a framework that lets you define AWS infrastructure(resources such as an s3 bucket) using familiar programming languages such as TypeScript, Python,... instead of writing infrastructure configuratino directly.
In our `src/stacks/**` directory we write with TypeScript "a DynamoDB table with these keys, a lambda with this memory and these permissions, an API in front of it."
running `cdk synth` compiles that TypeScript into CloundFormation template.

## CloudFormation template
The CKD synthesizes your code into CloudFormation template which AWS uses to create and manage infrastructure(resources).

## Stack
A deployable group of AWS resources managed together.


### SDK = Software Development Kit
A collection of tools, libraries and APIs that helps you build applications for a particular platform or service.
For example the AWS SDK lets your application talk with AWS services programmatically. (your application talk to a s3 bucket via an API)

## SDK vs. CDK
SDK -> used by your application code to interact with AWS.
CDK -> used to define and deploy infrastructure on AWS.

```
// SDK: application wants to upload a file
await s3Client.send(new PutObjectCommand(...));

// CDK: infrastructure wants to create a bucket
new s3.Bucket(this, 'MyBucket');
```


### Webhook vs. Polling
Webhook is the inversion of Polling. 
In **Polling** (let's consider we are trying to sync data with Hubspot), we call Hubspot every N minutes asking "what's new?" - mostly wasted calls, always stale by N minutes.
In **Webhook** we hand Hubspot a URL and say "Call me wheb something changes." Mechanically a webhook is nothing more than an HTTPs endpoint we expose + a subscription registered with the other system.
So in the current architecture we do: 
- Subscription (config file uploaded to the HubSpot app)
- Reciever (webhook handler - lambda - authentication only)
- Queue
- Worker (webhook worker - lambda)
- Write to COS

