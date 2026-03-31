Query parameters are the instructions we send to the server to filter and organize the data before it’s sent back to us.
q (Query): The most important one. It tells GitHub’s search engine, "Find only things related to 'python'.


sort & order: These tell the database how to rank the results. Without them, we’d get a random mix; with them, we get the top-tier repos first. 

per_page: This is the volume control. It prevents the server from sending we 30+ results (the default) when we only need 2 or 5, saving bandwidth and memory. 



Why response.json() over response.text?
Think of response.text as a giant block of marble and response.json() as a finished statue.
response.text: Returns a raw string. If we want to get the "stars" for the first repo, we would have to write complex code to search through that string manually.
response.json(): Automatically parses that string into a Python Dictionary/List structure