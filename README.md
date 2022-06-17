# Welcome to the study-buddy wiki!

## Home page

![Screenshot from 2022-06-17 10-43-34](https://user-images.githubusercontent.com/80586987/174229742-1c2cd774-dac6-4c4d-aaa6-d2cace97bd1b.png)

### The home page contains mainly four components:
1. Navbar
2. Topics component
3. Feed component
4. Activity component

***

### Navbar
* Logo of the app
* Name of the app
* Search field (search for rooms)
   *   Contains an input field named "q"
   *   Filters out room objects based on either room name , topic name, or description from database
* If user is authenticated, show avatar , user name.
   *   else show default avatar and login option
   *   if user clicked on user name field then it will direct to update-user route.

* drop down menu for settings and logout

***

### Topics Component
* We query all the topics from the database and passed only the first five of them to this component
* Display 5 topics +more link (for viewing and searching for more topics)
* If user clicks on one of the topics they are redirected to that particular topic containing all rooms (used a query string )


***

### Feed Component
* Display all the study rooms available (sorted in ascending order of update and create date)
* Each room contains:
   * Host name
   * Created since
   * Room name
   * Number of participants
   * Topic Name


***

 

### Activity Component
* 

