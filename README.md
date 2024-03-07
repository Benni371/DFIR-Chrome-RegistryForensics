# DFIR-Chrome-RegistryForensics
A repo with files pulled from a practice image I created to help students understand chrome and registry forensics. Along with the lesson, I gave them a couple questions they had to find the answers to while investigating the hindsight file and the registry hives.

## Files
+ `SAM`, `SYSTEM`, `SOFTWARE`, `NTUSER.DAT` are all registry hives. I didnt clean the sam hive so thats why the two log files are there for it so they can be replayed to get the clean hive.
+ `Hindsight Report` was generated from using a program called...you guessed it Hindsight. Its a tool made by Ryan Benson that scours the the Chrome databases stored in C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default folder and pulls out artifacts like searches, downloads, visited sites, etc.
+ `q.txt` are the questions and answers that I had the students search for and submit flags for
+ `server.py` is a flask web server that displays the questions and has a place of the students to submit their flags to. Its not robust or fancy by any means but it does its job

## Use of Repo
Anyone who wishes to share this is more than welcome too. Basically, run the server.py file (`python3 server.py`)and have students navigate to <your_private_ip>:5000 and they should be able to connect to it. It will present them with a login screen to put in a username and then they will have access to the questions and submission form. Flag submissions should be `challX_answer` format. If you need more clarification check the server.py file for the `CHALLS` array. You can edit or modify the specific criteria for how flags are submitted there.
