## Orbital Milestone 3
- Group: Team GGEZ
- Members: PAN YONGJING, YOON KI HYUN
- Level of Achievement: Apollo 11
- Type of Project: Website Application

## **[Click Here to view our website](https://masterggez.pythonanywhere.com)**

### Dummy Account
Username: thomasjohnson23

Password: orbitalpassword

Alternatively, you can sign up to create your own account!

## **[Click Here to access admin site](https://masterggez.pythonanywhere.com/admin)**

### Admin Account
Username: superadmin23

Password: orbitalpasswordadmin

**PLEASE DO NOT DELETE OUR DATABASE**


## Website Application: MakaNUS

Food and dining forms an important part of life in university. Apart from being a necessary mean of survival, food bring pleasure to our lives and in many instances, acts as a mean for us to gather and socialize. This is especially apparent in the NUS campus, where there are a myriad of food options consisting of cuisines from all around the world. Therefore, there exist a need for platforms where NUS students and staffs can easily look up food places on campus, as well as be provided information about the various outlets.

MakaNUS is an food information and review website that contains information about stalls and restaurants within and around NUS. It allows users to get information about dining options in and around NUS, as well as a platform to share food experiences, rate and review food places and menu items. In addition, it allows for users to share real-time updates with regards to the waiting time and crowd condition of respective food places.

## User Flow and Interface

- At the home page, users will be able to search for food items, food stalls, campus locations and information. Alternatively, they can choose to sign up for an account and subsequently login to enjoy the full features of the website (e.g. rate, review food items etc).
- Upon entering a search, users will be shown a list of existing stalls and restaurants that fit their search criteria. They can sort them according to restaurant name, restaurant rating and number of reviews. Click on a restaurant's name to proceed to the restaurant's page.

- Restaurant's page consist of basic restaurant's details (e.g. rating, location, address, opening hours etc.). Users can also see the estimated waiting time and crowd condition of the restaurant at that point in time (based on inputs of other users). Users can rate the restaurant, write a review and upload a photograph. If the users happen to be at the restaurant, they can choose to contribute information regarding the estimated waiting time and crowd condition in order to help other users (e.g. warn people away coming to the restaurant if crowd condition is very busy).
- At the Reviews tab, users can view reviews written by other users, and rate the reviews. The reviews are sorted by their ratings. If the review is written by a user himself, he has the option of editing or deleting the review.
- At the Photos tab, users can view photos uploaded by other users. If the photo is taken by a user himself, he has the option of deleting the photo.
- At the Menu tab, users can see the dishes available in the restaurant. Users can rate the dishes. Click on a dish's name to proceed to the dish's page. Users also have the option of adding a dish onto the menu by clicking the "Add to Menu" button below. Do note that dish added by users will have to be approved by site administrators before they appear on the Menu tab.

- Dish page contains basic information (e.g. dish ratings, the restaurant it belongs to etc.). Users can rate the dish and write reviews. They can read reviews of the dish written by other users, and rate those reviews. Similar to restaurant reviews, if the dish review is written by a user himself, he has the option of editing or deleting the review.

- Lastly, users can view their own profile by clicking on the top right arrow --> "My Profile". They would be able to access their basic information, and can choose to edit their profile information. They would also be able to view all their restaurant reviews, dish reviews and photos uploaded. They can choose to edit or delete them.

### Authentication

- Users are able to sign up for an account, and login and login out of the account.  
- Username provided by the user has to be unique. Password confirmation is required.
- Passwords are hashed to for security purposes, and even administrators will not be able to see users' passwords.
- Login is required for users to be able to rate, contribute reviews and upload photos.
- One login session is 600 seconds (10 minutes) if 'remember me' is not checked and 1209600 seconds (14 days) if 'remember me' is checked

### Administrator

- The admin site can be access by the URL "../admin".
- It allows to full access to all databases including user information, restaurant and menu details, ratings and reviews.
- Administrators have the ability to add, modify and remove objects in the database such as users, profile information, restaurant, dishes and reviews etc.
- However, as user passwords are hashed, administrators do not have the ability to access users' accounts as first person.
- New menu items contributed by users are be tagged as unverified Dish column in the database. Administrators can choose to check a verification box to enable the new dish to be displayed publicly.

### Estimated Waiting Time and Crowd Condition

- Users who are present at food places can provide real-time updates about the estimated waiting time and crowd condition at that particular location. This could help deter people from going to a extremely packed food place, and potentially prevent overcrowding, especially during peak periods.
- Estimated Waiting Time is computed by the average of all users' inputs for the past 30 minutes from current time.
- Crowd condition also takes into consideration the average of users' inputs for the past 30 minutes from current time.

### View Website (via localhost)

- Clone repository
- Install Python 3.6 (make sure to add python to PATH)
- Install Django 2.0.5 (via pip)
- Open Command Prompt Terminal, set directory to the project folder "orbital2018"
- Run "python manage.py runserver" on terminal
- Copy local server address into browser

### Website Deployment

- Made use of free web hosting service from pythonanywhere.com to deploy our website.
- View our  website at **[https://masterggez.pythonanywhere.com](https://masterggez.pythonanywhere.com)**.

### Project Log
<pre>
Orbitee 1: Pan Yongjing (Back End developer, web hosting), Orbitee 2: Yoon Ki Hyun (Front End developer)
___________________________________________________________________________________________________
| Orbitee 1(hrs) | Orbitee 2(hrs) |   Date   |                      Task                           |
|________________|________________|__________|____________________________________________________ |
|      43        |       44       |          |                    Milestone 1                      |
|      31        |       36       |          |                    Milestone 2                      |
|       6        |                |  30/06   |              Setting up back end (django)           |
|      10        |        8       |  01/07   |Setting up back end&combining back end with front end|
|       4        |                |  03/07   |               Setting up database                   |
|       1        |        2       |  04/07   |    Input of randomised values for testing & design  |
|                |        3       |  06/07   |            Design changes to the website            |
|      10        |       10       |  08/07   |    Discussion & Major front end & back end update   |
|       2        |                |  09/07   |                    Debugging                        |      
|       1        |                |  10/07   |                    Debugging                        |
|       2        |        4       |  11/07   |          Debugging & Redesign of the website        |
|                |        3       |  12/07   |          HTML/CSS styling & commenting              |
|       7        |        4       |  14/07   |        Major front end & back end update            |
|      10        |       10       |  15/07   |        Major front end & back end update            |
|       4        |        4       |  16/07   |            Git practice with our mentor             |
|       6        |        4       |  18/07   |  Git practice with our mentor + backend development |
|       3        |                |  19/07   |     Back end (restaurant page, search, pagination)  |
|       2        |                |  21/07   |           Back end (profile page skeleton)          |
|                |        6       |  22/07   |                    Front end                        |
|       2        |        1       |  23/07   |                  Minor back end                     |
|                |        3       |  24/07   |                    Front end                        |
|                |        2       |  26/07   |               Front end (Modal)                     |
|       2        |                |  27/07   |                 Work on database                    |
|       6        |        4       |  28/07   |          Front end & back end edits                 |
|                |       10       |  29/07   |           Front end javascript & styling            |
|      12        |        6       |  30/07   |Major back end update & front end styling&MILESTONE 3|
|       2        |                |  31/07   |              Minor back end & web hosting           |
---------------------------------------------------------------------------------------------------
|      166       |       164      |          |                    Grand Total                      |
</pre>

