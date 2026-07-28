# Unix commands

Personal cheat-sheet. One `##` per command — flags as a list, real commands in fenced blocks.

## grep — global / regular-expression / print

Search text inside files.

- `grep -r` — recurse through subdirectories
- `grep -n` — show line numbers for matches
- `grep -i` — case-insensitive
- `grep -rn` — recursive + line numbers together
- `grep -l` — list matching file names only
- `grep -c` — count matches per file
- `grep -E` — extended regex (ERE), less escaping than the default BRE (BRE)
- `grep --include="*.js"` — only search files matching a glob

```bash
grep -rn --include="*.js" "Bearer" .
```
Search recursively (with line numbers) for `Bearer`, only inside JavaScript files.

```bash
grep -rc "pattern" .
```
Count matches per file, e.g.:
```
==> ./controllers/user.js:3
==> ./services/auth.js:1
```

```bash
grep -rn "getBusinessEntityByBook" ./src/ --include=".ts" -A 5 -B 5 | grep -E "book|Book|BOOK|GOO|IREC"
```
Recurse with line numbers for `getBusinessEntityByBook` under `./src/`, only in `.ts` files, showing 5 lines of context after (`-A`) and before (`-B`) each match, then pipe the output through a second grep using an extended regex for the listed words.

## find — search a directory tree for files/directories

Recursively searches from a starting path for entries matching criteria (name, type, size, modification time…).

- `find . -type d -name "sdk"` — a directory named `sdk`
- `find . -type d -iname "akira*"` — directories matching the pattern, case-insensitive (`-i`)
- `find . -name ".env.example"` — files/directories named `.env.example`

```bash
find . -name "*.spec.ts" | xargs grep -l "bulk\BULK"
```
Find all `*.spec.ts` files, then search inside them for `bulk`/`BULK`, listing only the matching file names.

```bash
find . -name "*.spec.ts" | grep -l "bulk\BULK"
```
Here `grep` receives only the list of file names (not their contents, e.g. `./src/events/records.events.spec.ts`), so it searches for `bulk`/`BULK` in the file names themselves.

Skip `node_modules`:
```bash
find . -type d -name node_modules -prune -o -name "package.json" -print
find . -name "package.json" -not -path "*/node_modules/*"
```
Both filter out results inside `node_modules`. The `-prune` version is more efficient on large projects because `find` doesn't traverse those directories at all.

## xargs — extended arguments

Takes text from standard input and turns it into arguments for another command.

## ps — process status

- `ps aux` — all processes, detailed
- `ps -o pid,comm -ax` — show only the PID and command name

```bash
ps -o pid,comm -ax | grep "Visual Studio Code"
```
Show only the PID and command of the matching processes.

## ipconfig

> TODO: one-line gloss.

- `ipconfig getifaddr en0` — show your Wi-Fi IP address (en0 is usually Wi-Fi)

## ssh — secure shell

> TODO: add notes and examples.

## rsync — sync directories and files over the network

> TODO: add flags/examples.

## curl — Client URL (HTTP client)

- `-s` — silent; hide the progress meter and error messages
- `-H` — add a custom HTTP header
- `-I` — HEAD request; fetch only the response headers, not the body
- `-X <METHOD>` — set the HTTP method
- `-d '<data>'` — request body
- `-c cookies.txt` — cookie jar; store received cookies
- `-b cookies.txt` — send stored cookies (as a browser does automatically)

Call an API and pretty-print / extract from the JSON response:
```bash
curl -s -H "Authorization: Bearer $TOKEN" "https://test-nl.datahive.online/api/v2/registry-account/select-list?book=goo&type=short&accountId=28101" | jq
curl -s -H "Authorization: Bearer $TOKEN" "https://test-nl.datahive.online/api/v2/registry-account/select-list?book=goo&type=short&accountId=28101" | jq ".data[].value"
curl -s -H "Authorization: Bearer $TOKEN" "https://test-nl.datahive.online/api/v2/registry-account/select-list?book=goo&type=short&accountId=28101" | jq ".message"
```
Call the API with an auth token in the header (`-H`), silently (`-s`), then pipe to `jq` to pretty-print the response or pull out specific fields.

Impersonate a browser's CORS preflight handshake:
```bash
curl -s -i -X OPTIONS "https://test-nl.datahive.online/api/v2/registry-account/selct-list?book=goo&type=short&accountId=28101" \
-H "Origin: https://bid-offer-us-uat.datahive.online/" \
-H "Access-Control-Request-Method: GET" \
-H "Access-Control-Request-Headers: authorization" \
2>&1 | head -40
```
- `-H "Origin: ..."` — I'm a browser page loaded from this origin
- `-H "Access-Control-Request-Method"` — if this preflight succeeds, I plan to send a GET request
- `-H "Access-Control-Request-Headers"` — my real request will include an Authorization header

Cookie-based login flow:
```bash
curl -c cookies.txt -X POST https://api.example.com/login \
-H "Content-Type: application/json" \
-d '{"email": "test@example.com", "password": "1234"}'
```
The server can respond with the header `Set-Cookie: session_id=abc123`.

```bash
curl -b cookies.txt https://api.example.com/profile
```
Now curl sends the header `Cookie: session_id=abc123`.

## HTTP status codes

| Code | Meaning               | Note                                                     |
| ---- | --------------------- | -------------------------------------------------------- |
| 201  | Created               |                                                          |
| 204  | No Content            | body empty; typical browser preflight response (answer is in the header) |
| 302  | Found (temp redirect) | new URL in the `Location:` header, temporary — keep using the original in future |
| 401  | Unauthorized          | not authenticated — missing/invalid/expired token        |
| 403  | Forbidden             | authenticated but not authorized to access the resource  |
| 404  | Not Found             | resource doesn't exist (or the server won't reveal it)   |
| 409  | Conflict              | e.g. registering a user with an email that already exists |
| 422  | Unprocessable Entity  |                                                          |

## docker

- `docker ps` — list currently running containers
- `docker exec <container> <cmd>` — run a command inside a running container

```bash
docker exec postgres psql -U list -d list -c "\dt"
```
Inside the running container `postgres`, connect to the PostgreSQL database `list` as user `list`, and print all tables. (See `psql` for the flags.)

## psql — PostgreSQL command-line client

Needs a database URL (or connection flags) so it can connect to the database.

- `-U list` — connect as user `list`
- `-d list` — connect to database named `list`
- `-c "\dt"` — run one SQL / meta command and exit

```bash
psql postgresql://list:changeme@localhost:5432/list
```
Connect to my local database running inside a Docker container — user `list`, password `changeme`, database `list`.

## PostgreSQL meta commands

- `\dt` — list all tables in the current database
- `\d items` — show the shape of the table `items` (columns, types, foreign keys, relations…)

## jq — command-line JSON processor

Pretty-prints JSON and extracts specific fields. Very useful when piping `curl` output.

```bash
jq ".scripts" ./package.json
```
Print the `scripts` object from `package.json`.

## history — command history

Shows the command history the current terminal tab knows. Reverse search (`Ctrl-r`) looks this history file up.

## Ctrl-r — reverse history search

Searches backward through your command history — current session plus commands saved in `~/.bash_history` from previous sessions — most recent match first.

- `Ctrl-r` — press again to step to the next older matching command
- `Enter` — run the command immediately
- `Right arrow` — copy it to the prompt so you can edit before running
- `Ctrl-g` / `Ctrl-c` — cancel / abort the search
- `!git` — run the last command beginning with `git`
- `!?docker?` — run the last command containing `docker`

## evince — background a GUI app with &

- `evince file.pdf` — start it and wait for it to exit (many GUI programs don't detach automatically)
- `evince file.pdf &` — start it and return the prompt immediately

```
[1] 12345
```
`[1]` is the job number (used by the shell), `12345` is the PID.

Other GUI apps the same way:
```bash
gedit notes.txt &
firefox https://example.com &
vlc movie.mkv &
```

## jobs — list shell jobs

Lists jobs started from the current terminal.

```
[1]+ running evince file.pdf &
```

- `fg %1` — bring job 1 to the foreground (the terminal waits for it again; you can't run other commands)
- `Ctrl-z` — stop (freeze) the foreground job — does NOT kill it, just stops it
- `bg %1` — resume a stopped job and let it continue in the background

If you stop `evince` and then try to interact with its still-open PDF window, it won't respond.

## kill — stop a job or process

- `kill %1` — stop job number 1
- `kill 48291` — stop the process with PID 48291

## date — current date and time

An external executable program known to the shell.

- `date` — print the current date and time
- `date +%F` — print `YYYY-MM-DD` (`%F` is shorthand for `%Y-%m-%d`)

## which — show the path of an external command

Bash has built-in commands (`cd`, `echo`, `pwd`) and also runs external programs found in the directories listed in your `PATH`.

- `cd` — bash built-in
- `date` — external → `/usr/bin/date`
- `ls` — external → `/usr/bin/ls`
- `grep` — external → `/usr/bin/grep`

## Regular expressions

```
/^(\d{2})-(\d{2})-(\d{4})$/
```

- `^` — beginning of the match; ensures it starts at the first character
- `\d` — any digit (0-9)
- `{2}` — exactly 2 times
- `()` — capturing group; lets you extract parts of the match

```js
const fullDatePattern = /^(\d{2})-(\d{2})-(\d{4})$/
const [entireMatch, day, month, year] = "15-07-2026".match(fullDatePattern)
// entireMatch -> "15-07-2026"
// day          -> "15"
// month        -> "07"
// year         -> "2026"
```

```
/^(\d{2})-(\d{2})-(\d{4})T(\d{2}):(2)$/
```
Matches the full date-time pattern.

## xdg-open / open — open a file with the default app

- `xdg-open fileName.suffix` — Linux; xdg = Cross-Desktop Group. Opens the file, URL, or directory with the default application.
- `open fileName.suffix` — same thing on macOS.

## head — print the first lines of a file

- `head -n <N> <file>` — display the first N lines of the file

## dig — Domain Information Groper

Query DNS servers. Mainly used to troubleshoot DNS issues.

## lsof — list open files

- `lsof /etc/passwd` — all processes that have this file open
- `lsof -p 3806` — all open file descriptors of this process
- `lsof -i` — open file descriptors that are internet sockets (TCP & UDP)
- `lsof -iTCP` — only TCP sockets
- `lsof -iUDP` — only UDP sockets
- `lsof -iTCP -sTCP:LISTEN` — only TCP listening sockets
- `lsof -iTCP -sTCP:ESTABLISHED` — only TCP established connections
