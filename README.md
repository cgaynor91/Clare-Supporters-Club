# Clare Supporters Club
## Milestone Project Four 



[![Build Status](https://travis-ci.org/cgaynor91/Clare-Supporters-Club.svg?branch=master)](https://travis-ci.org/cgaynor91/Clare-Supporters-Club)

Find the deployed project can be found at: https://clare-supporters-club.herokuapp.com/

### User Experience (UX)
#### Project Purpose

The focus of this application is to create on online platform for people who support the County Clare in respect of GAA. The application will allow users to become part of an online community that can buy merchandise of their favourite club at discount prices while contributing to the club itself. 

The user will be able to view all the products that the application has to offer however if they wish to purchase from the site at the discounted prices they must register and become a member of The Clare Supporter's Club. 

The project uses a postrges database and the application is set up with the Django framework.

This application is targeted at all supporters of County Clare of all ages and disciplines with merchandise on the website to accomodate everyone. 

#### User Stories

- As a user I’d like to be able to buy specific branded merchandise from the website, which would support my County
- As a user, I’d like for the website to be user-friendly and easy to navigate
- As a user, I’d like to be able to search the website/database for merchandise available.
- As a user, I'd like to be able to access the data and experience all the site has to offer, regardless of device and browser type being used
 
#### Design Ideas
When I was thinking about the site design I decided I wanted to keep the colours of the county prevelant in it and also have images of the team prominent on the page. I wanted the site to be relatively easy to use as I was conscious that this site's target market is all age groups. 

##### Font
I wanted the font to be a bold blue colour - fitting in with the Clare theme. I also wantde the font weight to be quiet heavy as I was conscious that the site may be accessed by older people who may find smaller text harder to read. 
##### Colour Scheme
The colour scheme for me was a no brainer, the Clare colours of saffron and blue. Although the colours themselves may not marry very well, as the site is aimed to be accessed by Clare supporters I don't think the colour scheme would offend them. 
##### Icons
I utilised font-awesome icons for my social links and also for my nav bar, just to add a nice visual touch. 

### Wireframes

As is tradition for me, my wireframes don't look exactly like my finished project. 

On my wireframe of the products page I did not have a carousel of images as I felt that it may clutter up the site too much, however as the site progressed I felt the product page was lacking in something of impact and photo's of the team the user supports was a nice way to break up the page. 


### Features
#### Current Features
- Feature 1 – Navigation
    - The nav bar displays a logo for the Clare Supporters Club and links with social icons encourage the user to register, login and view cart. 
    - The options displayed will change on the navbar depending if the user is "logged in" or "logged out". Should the user be "logged in" the navbar will display a "log out" option and a profile option. 
- Feature 2 – Home Page/Product Page
    - Here the user sees a carousel of images from previous Clare Match events. If they scroll down they are greeted with the merchandise that is availableto them and the price. 
    - When logged in the user will be able to access the user’s account page as well as being able to log out.
    - If the user is not logged in they will have the option to go to the registration page or alternatively add items to their cart and then register before checking out the items. 
- Feature 3 – Search Bar
    - The search bar is available across the application and allows the user to search for particular merchandise that they would like to view/purchase. 
- Feature 4 – Register
    - Users can use the site to view merchandise without registering however if they wish to purchase merchandise at the discounted rate on the website they cannot do so unless they register to Clare Suppoerts Club. 
    - When the user registers their data is stored in the database and remembered for future logins. 
    - Usernames must be unique and should a user select a name that has already been used they will be advised of same. 
- Feature 5 – Log In
    - If a user is registered, they can navigate to the login page from the navbar where their data will have been stored in the database requiring them to enter their email and password. 
    - Should a user forget thier password they can click on the "Forgot your password?" link and they will be directed to the relevant page to be issued a new one. 
    - Once the user logs out a message will be displayed to advise them that they have logged out successfully. 
- Feature 6 – Cart
    - As the user is shopping they will be able to see how many items are in their cart by the icon in the navbar. 
    - The user can edit the quantity of items in their cart by clicking on the cart icon and editing the quantity before checkout
    - The user will then be able to access the checkout from the cart by clicking on the checkout button, however this will take them to a login screen should they not logged in already.
- Feature 7 – Checkout
    - At checkout the user will have to fill out a form with their shipping details and also their credit card information. 
    - The checkout feature is only available for users who have signed up for Clare Supporters Club
    - Once the user has paid a message will be displayed to advise them of same. 
- Feature 13 - Log Out
    - When a user decides they want to log out of the site, the option to do so is located on the navbar once the user is logged in.
    - Once the user chooses to log out, they will be taken back to the home page as a guest, with the default nav options available for a guest user (Home, Reviews, Register, Log In, Merchandise, Cart).
#### Future Features
- Ideally I would love for users to be able to leave a product review after purchasing
- I would also like to implement an area for users to discuss their shared interest of Clare as I feel this would help expand the site and enforce a positive community feel. 


### Technologies Used
- Amazon AWS Cloud 9
    - Amazon AWS Cloud 9 was the IDE I used for this project, and I really feel it will be the last time I do. 
#### Front-end technologies
- HTML5

- CSS3

- Javascript/JQuery

- Bootstrap

- Font Awesome

#### Back-end technologies
- Python

- Django

#### Databases
- Postgres/SQLite3
    - Postgres was used for the database for the deployed project.
    - SQLite used in test environment
#### Version control
- Git & GitHub
    - Git used for version control
    - GitHub used as a remote repository
#### Deployment
- Heroku

#### Payment processing
- Stripe API




