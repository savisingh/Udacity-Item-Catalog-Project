# Project: Item Catalog - Savneet Singh

README for a Item Catalog project using SQLite database and JSON APIs.
Running the Python code will give webpages where Sports and particular Sport Items for that Sport are listed.
Based on authentication and authorization of the user the user can edit, delete and add new Sport Items.
The python file to be executed in the virtual machine is called
 `application.py`

## Required Libraries and Dependencies

- Python
  - Install **Python 2.7.14** at https://www.python.org/downloads/ 
- Vagrant
  - Install **Vagrant** at https://www.vagrantup.com/downloads.html
- Virtual Box 
  - Install **Virtual Box 5.1** at https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
  
## How to Run the Project

- Bring the virtual machine up using the commands `vagrant up` followed by `vagrant ssh`
- `cd` into the `vagrant/catalog` directory
- Run the command `python category.py` to populate the database. A file called **sportcategorieswithusers.db** will now appear in your directory
- Run the command `python application.py` to access the webpage at `http://localhost:5000/...` where `...` refers to the API endpoints.

## Notes for the User 

- For any type of user you will be able to see:
	- The home page which will list the Sports along with the Latest Added Items
	- Details of a Sport Item (name and description)
- If you are able to login in you can:
	- **add** a new Sport Item
	- **delete** a Sport Item
	- **edit** a Sport Item

## API Endpoints

- `/` and `/catalog` show the home page with the Sport List and Latest Items List
- `/login` lets you login using Google Sign In
- `/catalog/newSportItem` lets you create a New Sport Item
- `/catalog/<sport_item>/edit` lets you edit an existing Sport
- `/catalog/<sport_name>/<sport_item>/delete` lets you delete an existing Sport Item
- `/catalog/<sport_name>/<sport_item>` lets you see the details of an existing Sport Item


## Note for the reviewer

- I tried to comply with the PEP8 guidelines in `application.py` but by complying completely (usually as the length of a line is too large) the file doesn't run in vagrant, so I reverted a couple changes. 
  
