# ds3002-project2

## Project Description
The goal of this project was to create and publish an interactive Discord bot in a test server. The bot provides users with quotes using the quotable API and can perform three functions: retrieve a random quote, retrieve a quote by a specified author, and retrieve 5 random quotes containing a keyword. We created a Docker build which was then deployed in Lightsail so it could be run on any machine.

## How to Use it
The bot exists in the test server specified in the Data Project 2 document. The bot can perform three functions:

1.	Retrieve a random quote using the quotable API.
    The bot performs this function when a message containing the phrase ‘random quote’ is typed in the chat.
    
    Example:
    ![image](https://user-images.githubusercontent.com/88460223/144660975-2275666a-ff3f-4453-b026-0b68c002604d.png)

2.	Retrieve a quote by a specified author.
    The bot performs this function when a message containing the phrase ‘quote by’ is typed in the chat.
    
    Example:
    ![image](https://user-images.githubusercontent.com/88460223/144661121-1c62902e-29d1-41c5-b601-0e2bedbca672.png)

3.	Retrieve 5 random quotes containing a specified keyword.
    The bot performs this function when a message containing the phrase ‘keyword:’ is typed in the chat.
    
    Example:
    ![image](https://user-images.githubusercontent.com/88460223/144661213-be25407e-7068-45cf-94f9-efdced4ae953.png)

## Benchmarks
1. Your bot should recognize a "help" or "info" message and return user instructions.
  
  Example:
  ![image](https://user-images.githubusercontent.com/88460223/144661614-fbbfc7f4-bf18-4fc9-bd1f-bebcc011188d.png)
  
2. Your bot should provide at least three commands or functions.
    
   The bot can (1) retrieve a random quote, (2) retrieve a random quote by a specific author, (3) retrieve 5 random quotes containing a specified keyword

3. Your bot should reply promptly with an intelligent response or an informative error message.

  Example (informative error for keyword search):
  ![image](https://user-images.githubusercontent.com/88460223/144662116-451f4f10-3786-4b76-80fa-80437e0f234b.png)

  Example (informative error for author search): 
  ![image](https://user-images.githubusercontent.com/88460223/144661810-48693739-48f1-4c8d-ab5e-01504a6fee7e.png)
  
   Note: if the bot is unable to successfully make an API call (for example in the random quote function) it will respond with the message: 'Unable to retrieve a quote from the API'

4. Your bot should integrate with at least one external data source that you can document and describe. This could be a database system or API.

  The bot connects to the quotable API. See references for more information about the API.

5. Submit all code in a standalone GitHub repository in your account. 
  
  Done.
  
## Sources
https://realpython.com/how-to-make-a-discord-bot-python/ 

https://opensourcelibs.com/lib/quotable

