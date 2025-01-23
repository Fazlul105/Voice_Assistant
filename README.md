# Voice_Assistant
Voice Assistant is a Python-based application that listens to user commands, processes them, and responds accordingly. 
Key Features:
1.	Speech Recognition:
o	Uses the speech_recognition library to process voice commands from the user.
2.	Text-to-Speech Output:
o	Implements the pyttsx3 library for generating spoken responses, creating a conversational experience.
3.	Time Inquiry:
o	Responds to queries about the current time, formatted as "Hour:Minute AM/PM".
4.	Web Search:
o	Recognizes commands like "search for" and opens Google in a web browser with the specified query.
5.	Exit Command:
o	Includes an "exit" command to gracefully terminate the program with a spoken farewell message.
6.	Error Handling:
o	Handles cases where speech is not recognized by providing a spoken apology.
________________________________________
Highlights:
1.	Interactive User Experience:
o	The assistant greets the user and continues listening in a loop, allowing multiple interactions within a single session.
2.	Voice-Based Control:
o	Eliminates the need for manual input, making it user-friendly and efficient.
3.	Dynamic Web Search:
o	Allows users to search the web with natural language commands, enhancing its utility.
4.	Modular Design:
o	Separates functionality into reusable functions (speak, listen, main), making the code easy to maintain and extend.
5.	Customizable:
o	The program can be expanded with additional commands or connected to APIs for tasks like weather updates, reminders, or home automation.


