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

### DNS Rsolver Picture
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

## TCP Connection (Transmission Control Protocol)
Suppose DNS replied and browser now has the IP address.
Browser still can not make an http request, because http is an application protocol.
Before 2 computers can exchange HTTP messages, the first need a reliable communication channel.
Browser before sending the HTTP message should konw:
 - Is the server actually there?
 - Is someone listening on the correct port?
 - Can data arrive reliably?
 - Can both sides agree to talk?

### TCP Handshake process includes:
 - SYN (synchronization)
 - SYN-ACK (acknowledgement of synchronisation)
 - ACK (final acknowledgement)

**DNS** tells us **where** the server is.
**TCP** establishes a reliable communication channel **with** that server.

When I start a Nest.js app as:
```
await app.listen(3000)
```
I am telling the OS: "Please accept TCP connections on port 3000 and give them to me."

## TLS 

