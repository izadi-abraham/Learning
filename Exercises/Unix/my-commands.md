
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

402 - Forbidden -> Means you are not authorized > Not allowed to access this resource

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
