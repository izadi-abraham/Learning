# A Network Request
Browser -> DNS -> TCP Connection -> TLS Handshake (HTTPS) -> HTTP Request -> Load Balancer -> API ->
Database -> HTTP Response -> Browser renders the page


## URL
When a URL is typed in a browser, at this point the browser only knows that url.
https://google.com - https tells the browser to use that protocol.
Browsers can not send packets to domain names, they need to know the ip address.


## DNS (Domain Name System)
If Google wants to change its servers, they update one DNS record.
google.com -> 142.250.74.14
google.com -> 34.160.111.145


### An Abstraction layer
DNS isn't just for humans, it is also an abstraction layer between a stable name and a changeable network address.


### DNS Resolver Picture
Browser/nslookup -> 127.0.0.53 (local DNS Cache) -> Recursive Resolver -> Root DNS -> .com DNS -> Google Authorative DNS -> 172.217.17.206


In a more precise words, after DNS resolving, the browser knows something like this:
- Domain: myapp.com
- IP address: 104.26.10.78
- Port number: 443

:443  -> HTTPS (Nginx)
:80   -> HTTP
:22   -> SSH
:5432 -> PostgreSQL
:6379 -> Redis

### DNS Resolving journey in more detail
When I enter a domain name (like www.google.com) in my browser the journey starts:

Browser => Operating System => Local DNS Stub Resolver (systemd-resolved) 127.0.0.53 =>
Home router (DNS forwarder) 192.168.1.1 => cache hit (return IP) / cahce miss => 
Upstream DNS Resolver (ISP DNS / Google 8.8.8.8 / Cloudflare 1.1.1.1)

Now suppose the **Home Router** forwards the DNS packet/request to **Google's recursive resolver**,
(8.8.8.8) and it doesn't have the answer cached, The first step is ask **Root name server**,
And since this is a .com domain, root name server asks **.com TLD servers** and finally the
.com TLD server asks **Google's authorative server** and the IP is resolved.

**TLD Name server** stands for **Top-Level Domain server**. Some of them are generic like .com, .net, .org and
some of the are coutery code TLDs.

- When a recursive resolver like Google DNS, Cloudflare, the ISP's resovler, etc. ship with a built-in file called the **Root Hints** file.
- It contains only the addresses of the root name servers, which is a very small amount of data.


```text
## DNS Resolution Flow

Browser
    │
    ├── Cache hit → Return IP
    │
    └── Cache miss
          │
          ▼
Operating System
          │
          ▼
Local DNS Stub Resolver
(systemd-resolved)
127.0.0.53
          │
          ├── Cache hit → Return IP
          │
          └── Cache miss
                │
                ▼
Home Router
(DNS Forwarder)
                │
                ├── Cache hit → Return IP
                │
                └── Cache miss
                      │
                      ▼
Recursive Resolver
(ISP / Google / Cloudflare)
                      │
                      ├── Cache hit → Return IP
                      │
                      └── Cache miss
                            │
                            ▼
Root Name Server
                            │
                            ▼
TLD Name Server (.com)
                            │
                            ▼
Authoritative Name Server
(google.com)
                            │
                            ▼
Returns IP Address
```


## TCP Connection (Transmission Control Protocol)
Suppose DNS replied and browser now has the IP address.
Browser still can not make an http request, because http is an application protocol.
Before 2 computers can exchange HTTP messages, they first need a reliable communication channel.
Browser before sending the HTTP message should konw:
 - Is the server actually there?
 - Is someone listening on the correct port?
 - Can data arrive reliably?
 - Can both sides agree to talk?

### TCP Handshake process includes:
 - SYN (synchronization)
 - SYN-ACK (acknowledgement of synchronisation)
 - ACK (final acknowledgement)

```text
Client                         Server

   SYN ────────────────────────►
       "Can we connect?"

       ◄──────────────── SYN-ACK
         "Yes. I received
          your request,
          and I want to connect too."

   ACK ────────────────────────►
       "I received your response."
```

** The handshake establishes the connection and synchronizes the sequence-number state between the two endpoints. **

**DNS** tells us **where** the server is.
**TCP** establishes a reliable communication channel **with** that server.

When I start a Nest.js app as:
```
await app.listen(3000)
```
I am telling the OS: "Please accept TCP connections on port 3000 and give them to me."

## TLS (Transport Layer Security)
TLS provides us security properties that TCP does not:
- Encryption / confidentiality: Someone observing the network can't easily read the HTTP data.
- Authentication: The browser can verify it is communicating with the intended server.
- Interity: The data can not be modified in transit without detection.

```text
TCP:
"I can reliably communicate with this IP:port."

TLS:
"The communication is encrypted,
the server's identity can be authenticated,
and modifications can be detected."

HTTP:
"Here is the actual application message."
```

** One important detail: Encoding doesn't provide security (like Base64) but encryption does it. TLS encrypts the data. **

Historically, ** TLS replaced SSL (Secure Sockets Layer). ** You'll still hear people say "SSL certificate," but modern HTTPS uses TLS, not SSL.

### TLS Handshake
Q: If the browser and server need to communicate using encryption, how do they agree on the encryption keys without sending the secrets key openly over the network?
The famous cryptographic algorithms "Diffie-Hellman" key exchange. The idea is very interesting:

```text
Browser                         Server

       public information
       ◄────────────────────►

       private information
       (never transmitted)

             ↓
       both independently
       calculate the same
       shared secret

       Shared Secret
       ─────────────
       same on both sides
```

#### Asymmetric and Symmetric cryptography are used in TLS
The Asymmetric cryptography is useful for authentication and certain key-exchange mechanisms.
Once the TLS handshake has established the shared key, symmetric encryption is used for the actual data because it's much more efficient.

```text
TLS handshake
      │
      ├── Authenticate server
      │
      ├── Establish shared key material
      │
      ▼
Symmetric encryption
      │
      ▼
Encrypted HTTP traffic
```

#### TLS Certificates and Certificate Authorities(CAs)
These help the browser to know if the server is really google.com or not as an example.

```text
TCP
 │
 │ Reliable connection
 ▼
TLS
 │
 ├── Certificate
 │      └── "This server is google.com"
 │
 ├── Authentication
 │
 ├── Key exchange
 │
 └── Encrypted communication
 ▼
HTTP
```

