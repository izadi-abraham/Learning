
g/re/p -  global/regular expresion/print 
Search texts inside files 


grep -r 
serach recursively through all subdirectories.

grep -n 
show the line number where the matches was found.

grep -i
Ignore uppercase/lowercase - case insensitive

grep -rn
combining recursive and line numbers together.

grep -rn --include="*.js" "Bearer" .
serach only in JavaScript files

grep -l
list file names only

grep -rc
count matches found
==> ./controllers/user.js:3
==> ./services/auth.js:1

grep -E
use Extended Regular Expressions (ERE) - less escaping 
normally grep uses Basic Regular Expressions (BRE)

grep -rn "getBusinessEntityByBook" ./src/ --include=".ts" A 5 B 5 | grep -E "book|Book|BOOK|GOO|IREC"
search recursively and show line numbers for the matches for the expression "getBusiness..." in the src directory, only look inside the file names ending with .ts, show 5 lines after the match found and 5 lines before
the match found, and pipe the output to grep for search using Extended Regular Expression for the words mentioned in the double quotes.


-------------------------------------------

find - search for files or directories by names.


find . -type d -name "sdk"
searches for a directory named sdk.

find . -name "*.spec.ts" | xargs grep -l "bulk\BULK"
find in the current directory all the files which their names end with .spec.ts and then search inside those files for the word bulk or BULK, and list only file names for the matches.

find . -name "*.spec.ts" | grep -l "bulk\BULK"
finds in the current directory all files which their names ends with .spec.ts and gives the output as a text file (this text file includes only the file names like ./src/events/records.events.spec.ts) to grep, so grep only
searches the words bulk or BULK in the file names.

find . -type d -iname "akira*"
find all directories that matches the pattern in their names (case insensetive - i)

-----------------------------------------

xargs - extended arguments
Takes text from standard input and converts it into arguments for another command.


-----------------------------------------

ps - Process Status


ps aux

ps -o pid,comm -ax | grep "Visual Studio Code"
show only pid anc command of the processes

-------------------------

ipconfig - ???


ipconfig getifaddr en0
show your ip address of the Wi-Fi (usually en0 is Wi-Fi)

----------------------------------------

ssh - secure shell

----------------------------------------

rsync - sync directories and files over the network ???

-------------------------------------


curl - Client URL - CURL is the http client


curl -s -H "Authorization: Bearer $TOKEN" "https://test-nl.datahive.online/api/v2/registry-account/select-list?book=goo&type=short&accountId=28101" | jq
curl -s -H "Authorization: Bearer $TOKEN" "https://test-nl.datahive.online/api/v2/registry-account/select-list?book=goo&type=short&accountId=28101" | jq ".data[].value"
curl -s -H "Authorization: Bearer $TOKEN" "https://test-nl.datahive.online/api/v2/registry-account/select-list?book=goo&type=short&accountId=28101" | jq ".message"
call the API with authorization token in header (-H), siletntly (-s) and then pipe it to jq (json processor) to pretty print the json response

401 - Unauthorized -> Means you are not authenticated -> missing/invalid/expired token

403 - Forbidden - Access Denied -> Means you are not authorized > Not allowed to access this resource

404 - Not Found - The requested resource does not exist (or the server chooses not to reveal that it exists)

409 - Conflict -> Trying to register a user withe the email that already exist

422 - Unprocessable Entity

201 - Created

204 - No Content -> There is no content in the body of the response, usually the preflight responses get this. In these preflight requests by browsers the answer is only in the header.

curl -s -i -X OPTIONS "https://test-nl.datahive.online/api/v2/registry-account/selct-list?book=goo&type=short&accountId=28101" \
-H "Origin: https://bid-offer-us-uat.datahive.online/" \
-H "Access-Control-Request-Method: GET" \
-H "Access-Control-Request-Headers: authorization" \
2>&1 | head -40

This is impersonating a browser's CORS preflight handshake
-H "Origin:..." -> I am a browser page loaded from this origin
-H "Access-...-Method" -> If this preflight succeds, I plan to send a GET request
-H "Access-...-Headers" -> My real request will include an Authorizatino header

curl -c cookies.txt -X POST https://api.example.com/login \
-H "Content-Type: application/json" \
-d '{"email": "test@example.com", "password": "1234"}'

Server can send this as header: Set-Cookie: session_id=abc123

curl -b cookies.txt https://api.example.com/profile

Now curl send this as header: Cookie: session_id=abc123

-c -> Cookie jar - store cookies
-b -> Send cookies - As browser does automatically


---

find - searches a directory tree recursively for files and directories that match specified criteria (such as name, type, size, or modification time)


find . -name ".env.example"
find all files/directories named .env.example recursively from the current directory.

find . -type d -name node_modules -prune -o -name "package.json" -print
find . -name "package.json" -not -path "*/node_modules/*"
filters out results inside node_modules but find still traverses those directories. The prune version is more efficient on large projects.


---

docker ps
lists the Docker containers that are currently running.

docker exec postgres psql -U list -d list -c "\dt"
Inside the docker container `postgres`, connect to the PostgreSQL database `list` as user `list`, and print all tables.

docker exec postgres ...
run a command inside the running container named 'postgres'

psql
PostgreSQL command-line client

-U list
connect to the database as 'user: list'

-d list
connect to the database named list 'database: list'

-c "\dt"
run a SQL meta command and exit. List all tables in the current database and exit.

--- 

psql - PostgreSQL command-line client needs a database url so it can connect to the database

psql postgresql://list:changeme@localhost:5432/list
connects to my local databes which is running inside a docker container, with user as list, password as changeme,
and the DB name is list.

---

PostgreSQL meta commands

\dt
List all tables in the current databas.

\d items
shows the current shape of table named items. Including all the columns, types of columns, foreign keys, relations...

--- 

jq - A command-line JSON processor. It can pretty-print JSON and extract specific fields. Very useful when piping the output of `curl`.

jq ".scripts" ./package.json
prints the scripts object in the package.json file.

---

history - shows the history of commands that the current terminal's tab knows. So if you do reverse search then
it looks this history file up.

---

ctrl + r - (reverse-i-search)`': - Also called history search - Searches backward through your command history, 
starting with the most recent matching command. It looks up commands from the current terminal session and 
commands saved in your ~/.bash_history file from previous sessions.

ctrl + r - Each press of ctrl + r will go to the next older matching command.

Enter - Runs the command immediately.

Right arrow - The command is copied onto the command line so you can edit before running.

ctrl + g || ctrl + c - Will cancel or aborts the reverse search.

!git - Searches for last command begining with 'git'.

!?docker? - Searches for the last command containing docker.

---

evince file.pdf
Start evince and wiat for evince to exit. Many GUI programs don't detach automatically.

evince file.pdf &
Start evince and immediately give me my prompt back.
Usually we see something like:
[1] 12345 - [1] this is the job number (used by the shell) and 12345 is the PID.

gedit notes.txt &
firefox https://example.com &
vlc movie.mkv &

---

jobs - You can see list of jobs started from your current terminal.

[1]+ running evince file.pdf &

fg %1 - foreground - bring the job No.1 to the foreground.
Now the terminal is again waiting for evince to exit and you can not run other commands.

Ctrl+z - stops the process - While the terminal is waiting for the GUI app (evince in this case) to exit, if you press
ctrl+z then we stop the process ID, we DO NOT KILL the process, just STOP it. It is frozen.

And then if you use 

bg %1 - Resumes a stopped job and lets it continue in the background.

If we stopp the evince file.pdf command and in the GUI we try to interact with the pdf window which is still open then it doesnt respond.

---

kill %1 - stop job number 1.
kill 48291 - stop process with the PID 48291.

---

date - Prints the current date and time. It's an external executable program which is know by shell.

date +%F - Prints the date in this format YYYY-MM-DD - %F is a shortcut for %Y-%m-%d

--- 

which - shows where is ???

Bash itself provides built-in commands (like cd, echo, pwd), but it can also run external programs found in directories listed in your PATH.

cd -> bash built in
date -> external program -> /usr/bin/date
ls -> external program -> /usr/bin/ls
grep -> external program -> /usr/bin/grep

---

Regular Expressions

/^(\d{2})-(\d{2})-(\d{4})$/

^ - Begining of the match - This ensures that the match starts immediately at the first charactar.

\d - Any digit (0-9)

{2} - Exactly 2 times

() - Creates capturing group and it lets you extract parts of the match.
fullDatePattern = /^(\d{2})-(\d{2})-(\d{4})$/
const [entireMatch, day, month, year] = "15-07-2026".match(fullDatePattern)
enitireMatch -> "15-07-2026"
day -> "15"
month -> "07"
year -> "2026"

/^(\d{2})-(\d{2})-(\d{4})T(\d{2}):(2)$/ - Matches teh full date time pattern

--- 







