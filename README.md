# Squirrel Tracker  



## Project Description
  
Squirrel Tracker is a web application that can keep track of all the known squirrels in Central Park. Through Squirrel Tracker, we can see a map that displays the location of the squirrel sightings. Information about whether a squirrel is eating, running, etc. is also available. In a word, no matter how you feel about squirrels, love them or afraid of them, want to see them or avoid them, this web application is exactly what you are looking for.  

## Background  

Eccentric billionaire Joffrey Hosencratz relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. He fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona has left him wanting. He would like to start keeping track of all the known squirrels and plans to start with Central Park. 

## Data Source  
  
2018 Central Park Squirrel Census  

## Dependencies 
 
Django

## Management Commands  
  
•	Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command.  
python manage.py import_squirrel_data /path/to/file.csv  
•	Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command.  
python manage.py export_squirrel_data /path/to/file.csv  

## Views  
 
•	A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map  
o	Located at: /map  
•	A view that lists all squirrel sightings with links to edit each  
o	Located at: /sightings  
•	A view to update a particular sighting  
o	Located at: /sightings/  
•	A view to create a new sighting  
o	Located at: /sightings/add  
•	A view with general stats about the sightings  
o	Located at: /sightings/stats  

## Contributors  
  
Group Name: Xinru & Siming  
Section Number: 01  
UNIs: [xw2780, sz2944]  
GitHub link: https://github.com/xw2780/project_Xinru_Siming  


