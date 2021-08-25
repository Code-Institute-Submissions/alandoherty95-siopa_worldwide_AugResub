**[Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)** - a little taste of home!

Welcome to **[Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)** - a one stop shop for all your favourite Irish products. Siopa Worldwide is an e-commerce store, offering a range of popular Irish food and beverages. We are dedicated to keeping you stocked up with your favourite Irish food and drinks no matter where in the world you are located!

![Website Mockup](https://github.com/alandoherty95/siopa_worldwide/blob/master/resources/mockups/mockup-original.png?raw=true)

![Siopa Worldwide Logo](https://github.com/alandoherty95/siopa_worldwide/blob/master/resources/screenshots/siopa-logo-home.png?raw=true)

**[Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)** is a full-stack e-commerce application selling Irish goods around the globe. The website is designed to showcase the most sought-after food and beverages known to Ireland. Users of the application can browse through our growing range of products before purchasing their favourites. The user will be prompted to enter their personal details, delivery details and payment details when completing an order. The user will then receive an order confirmation via email. Siopa Worldwide allows users to create an account, update items in their shopping bag, complete purchases and view their order history.

## Table of Contents

1.  <a  href="#context">**Context**</a>

2.  <a  href="#ux">**User Experience (UX)**</a>

3.  <a  href="#design">**Design & Development**</a>

4.  <a  href="#usertesting">**User Stories**</a>

5.  <a  href="#wireframes">**Wireframes**</a>

6.  <a  href="#technologies">**Technologies**</a>

7.  <a  href="#features">**Features**</a>

8.  <a  href="#testing">**Testing**</a>

9.  <a  href="#deployment">**Deployment**</a>

10. <a  href="#credits">**Credits**</a>

11. <a  href="#acknowledgements">**Acknowledgements**</a>

<span  id="context"></span>

## 1. Context

The purpose of this project is to create an e-commerce store specialising in the most sought-after Irish products. I chose this angle due to the bountiful number of Irish people who live outside of their homeland but still desire Irish products. Tens of thousands of Irish people emigrate to other countries every year. Typically, Irish people living abroad will find it difficult to source authentic Irish food and beverages. I was able to identify a niche market which can be utilised by anyone who craves Irish products regardless of their location in the world. In preparation for this project, I conducted research on friends, colleagues and family members to identify the most popular food and beverage products which are not easily found outside of Ireland.

The application is simply designed with user experience in mind. The website allows users to easily browse through the range of products in our database. Shoppers can use the sorting and searching features to easily find their desired products. The shoppers can add items to their bag with a running cost displayed in the top right corner at all times. The user can complete an order by making a purchase and a confirmation message will be sent via email. The website is intuitive and the purpose is immediately clear to any first-time visitors.

<span  id="ux"></span>

## 2. User Experience (UX)

### The Five Planes of UX

#### The Strategy Plane

After conducting market research on friends, peers and family members

I identified a niche market which can be utilised by anyone who craves Irish food and beverages no matter where they are in the world. I want to create an application focusing purely on the most popular Irish goods which are not easily found outside of Ireland. Every shopper will have the ability to create their own account, safely provide their personal information and securely complete an order.

#### The Scope Plane

When deciding on the scope of my project, I decided to design a website allowing users to create an account, browse products, add items to their shopping cart and securely complete an order. The primary feature will be the capability to purchase a product through a secure checkout using Stripe Payments. Shoppers can easily sort products by name, price or category. Shoppers can easily search for products, using keywords. To improve the user experience, I want users to be notified of their actions, such as shopping bag updates as well as success and error messages.

#### The Structure Plane

After deciding on the features I wanted to include, I focused on the overall structure of the website. I want to keep the design clean and sleek. All potential customers will be able to search for a product using keywords but can also use a sorting feature depending on the needs of the user. I am using the grid system from Bootstrap to clearly display the content of each page. The navigation bar will change depending if the user is anonymous or logged in. Clicking 'Profile' in the navigation bar, reveals more options via a dropdown list. The store owner (admin), signed in as a superuser, can also access the product management page. The store owner will have the option to add, edit or delete items from the product range.

#### The Skeleton Plane

I wanted a clear, simple structure throughout the website. Each page will have a fixed navigation bar with consistent styling and prominent call-to-action buttons. There will be a large call-to-action button on the home screen to invite shoppers to browse all products. Each page has a unique heading so users are aware of which page they are on at all times. The products page displays all items neatly, allowing users to view multiple products on the same page. Clicking on a product will direct the shopper to a more detailed view about the individual item. Shoppers can simply add items to their shopping bag with a toast message appearing in the top right corner of the screen when an action is completed. Users can enter their personal information confident in the application's security features. Shoppers can complete their checkout and receive an email confirmation of their order.

#### The Surface Plane

From conducting research on similar e-commerce sites, I discovered most online stores are quite colourful and brimming with information. Conversely, I wanted to keep the design sleek and simple, only displaying relevant information to the user. Initially, I sketched ideas and wireframes onto paper, before recreating more advanced wireframes online. I designed all the pages for desktop and smaller screen sizes showing the structure and content on the different devices.

<span  id="design"></span>

## 3. Design & Development

During the research phase of this project, I posed the following questions to friends, family members and peers living abroad:

- Which Irish goods do you desire most while living abroad?

- Which online stores do you use for buying Irish goods?

- What are your favourite brands of Irish food and drinks?

- What kind of Irish goods can you purchase in your town or city?

- Is there any store specialising in Irish products in your town or city?

### Target Market

The e-commerce store is primarily targeting Irish people who are living abroad. It is difficult for most Irish people living in a foreign country to find their favourite Irish food and beverages. There is a niche market for selling Irish goods to Irish people living abroad.

### Overview

The website was designed with the following main objectives:

- To allow users to browse all products in our database using sorting and searching features

- To allow shoppers to complete an order by purchasing their desired products

- To allow shoppers to create an account and view previous orders

- To allow shoppers to contact the store owner by submitting a contact form

- To allow shoppers to read blog posts created by the store owner

### **Project Goals**

As an owner of this e-commerce store, I would like to:

- encourage users to visit the store

- encourage users to browse our range of products

- encourage users to buy products from the store

- encourage users to return to the website again

- create, update and delete items in our product range

- create, update and delete posts in our blog

- be contactable by shoppers using a contact form

### Application Features

- Browse products

- View product details

- Create an account

- Log in/log out

- Add items to shopping bag

- View items in shopping bag

- Edit and update items in shopping bag

- Delete items from shopping bag

- Complete an order

- View order history

- Search for specific items using keywords

- Sort items by name, price or category

- Contact form

- Blog posts

### Design Process

The primary design goal in mind when designing this application is to attract the customer to explore further. The landing page is bright and striking. There is a prominent call-to-action button inviting users to 'Shop Now'. This button will lead the user to the products page where they can browse all items in our product range.

- Design a bright and visually appealing application.

- Design an intuitive and easy to navigate website.

- Achieve a clean aesthetic displaying only the necessary information.

- Use Bootstrap4 features for the layout and structure of the application

- Use Bootstrap4 classes and components to provide structure as well as highlighting and enhancing different elements.

- Design an application which is responsive on all screen sizes.

- Design a logo that is simple, attractive and memorable.

The colour scheme chosen for this project was inspired by bright colours to give the website an attractive, vibrant look. The white background gives a sleek, neutral look to the application with green and black nicely complementing.

![Colour Scheme](https://github.com/alandoherty95/siopa_worldwide/blob/master/resources/screenshots/colour-palette.png?raw=true)

- **#FFFFFF White** is the backdrop of all headings and text on the website. The bright colour emphasises clarity and removes visual clutter. The black text is easily readable on the white background.

- **#169B62 Green** is used for some buttons seen throughout the website. The buttons were designed to be large and prominent. The bright green button on the white background grabs the attention of the user.

- **#FFFFFF Black** is used for headings and text on the website. The black text is easily read on the white background. Black is also used throughout the application for buttons.

#### Typography

![Indie Flower Font](https://github.com/alandoherty95/siopa_worldwide/blob/master/resources/screenshots/indie-flower-font.png?raw=true)

[Indie Flower Font](https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap) was used because of the bubbly, rounded edges. It grabs the user's attention in contrast to the straight, simple Oswald font.

![Oswald Font](https://github.com/alandoherty95/siopa_worldwide/blob/master/resources/screenshots/oswald-font.png?raw=true)

[Oswald Font](https://fonts.googleapis.com/css2?family=Oswald&display=swap) was used for the primary text because it is easy to read. Oswald is designed to be used freely across the internet by web browsers on desktop computers, laptops and mobile devices.

### Development Process

The whole development process is broken down into smaller stages to help in managing the project.

- During the research phase of this project, I posed the following questions to friends, family members and peers living abroad:

- Which Irish goods do you desire most while living abroad?

- Which online stores do you use for buying Irish goods?

- What are your favourite brands of Irish food and drinks?

- What kind of Irish goods can you purchase in your town or city?

- Is there any store specialising in Irish products in your town or city?

- Choose a consistent colour scheme

- Identify the necessary applications needed

- Create wireframes for each page for desktop, mobile and tablet

- Create a data set for the products application

- Create a minimum viable product

- Set up Django Framework

- Set up Allauth for authentication and registration

- Create a base.html page including navigation with common elements, links and scripts

- Create a home app to display a landing page

- Create a products app to display all items in our product range

- Create a bag app to display the contents of the shopping bag

- Create a checkout app allowing shopper to complete an order

- Create a profile app to save personal information and order history

- Create a blog app allowing the admin to create, update and delete posts

- Create a contact app allowing users to submit a message to the store owner

- Create additional elements contributing to the user experience such as toasts and messages

- Adjust and tailor the layout and styling of each page

<span  id="usertesting"></span>

## 4. User Stories

#### **As a first-time user, I would like to:**

**General**

- immediately understand the purpose and aim of the website

- be able to easily navigate through the site

- explore a website that appeals to me visually

- know where I am on the website at all times

- be informed of actions I take, successful or otherwise

**Products**

- browse through a range of products

- sort products by their relevant category

- search for a specific product using keywords

- view the individual product details on a separate page

- adjust the quantity of any product

**Shopping Bag**

- easily view the contents of my shopping bag

- easily view the total cost of my shopping bag at all times

- remove items from my shopping bag

- adjust the quantity of items for a specific product in my shopping bag

- see any changes I make to my bag reflected in the shopping bag grand total

- view the details of what is in my shopping bag

**Checkout**

- purchase items by checking out easily and securely

- receive a confirmation message of my order via email

- view the details of my order in the confirmation email

**Account**

- create an account easily and quickly

**Blog**

- read blog posts about the mission, values of the store as well as products

**Contact**

- submit a contact form to get in touch with the store owner

#### **As a registered user, I would like to:**

- log in and out easily and quickly

- reset my password if it is forgotten

- receive a confirmation message that I have successfully registered an account

- view my personal profile

- view my order history in my profile page

- save my default delivery details for future orders

- easily update my delivery information

#### **As a Superuser, I would like to:**

- access the admin panel easily

- create, update and delete categories

- add new items to our product range

- edit or delete existing items from our product range

- view and manage users of the site

- view and manage orders

- create, update and delete blog posts

- be contactable using a contact form

<span  id="wireframes"></span>

## 5. Wireframes

### Desktop Wireframes

![Home Page](https://github.com/alandoherty95/siopa_worldwide/blob/master/resources/wireframes/desktop-wireframes/index-wireframe.png?raw=true)

![Products Page](https://github.com/alandoherty95/siopa_worldwide/blob/master/resources/wireframes/desktop-wireframes/products-wireframe.png?raw=true)

![Product Detail Page](https://github.com/alandoherty95/siopa_worldwide/blob/master/resources/wireframes/desktop-wireframes/product-detail-wireframe.png?raw=true)

![Shopping Bag Page](https://github.com/alandoherty95/siopa_worldwide/blob/master/resources/wireframes/desktop-wireframes/bag-wireframe.png?raw=true)

![Checkout Page](https://github.com/alandoherty95/siopa_worldwide/blob/master/resources/wireframes/desktop-wireframes/checkout-wireframe.png?raw=true)

### Mobile Wireframes

![Mobile Wireframes 1](https://github.com/alandoherty95/siopa_worldwide/blob/master/resources/wireframes/mobile-wireframes/mobile-wireframes1.png?raw=true)

![Mobile Wireframes 2](https://github.com/alandoherty95/siopa_worldwide/blob/master/resources/wireframes/mobile-wireframes/mobile-wireframes2.png?raw=true)

<span  id="technologies"></span>

## 6. Technologies

### **Languages**

- **HTML** - used to create the main structure of the application

- **CSS** - used to position components and style the application

- **JavaScript** - used to for interactivity throughout website

- **Python** - used to handle backend functionality

### **Libraries and Frameworks**

- [Django](https://www.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

- [Bootstrap4](https://getbootstrap.com/) is a powerful front-end framework for faster and easier web development including forms, buttons and navigations.

- [Stripe](https://www.stripe.com/) offers payment processing software and application programming interfaces for e-commerce websites and mobile applications.

- [Google Fonts](https://fonts.google.com/) provides a curated collection of the best free fonts available online.

- [Font Awesome](https://fontawesome.com/) is a font and icon toolkit based on CSS.

- [jQuery](https://code.jquery.com/) is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling and CSS animation.

- [Pillow](https://pypi.org/project/Pillow/2.2.1/) is a Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) is an application that helps to manage Django forms.

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) is an integrated set of Django applications addressing authentication, registration and account management.

### **Project Management**

- [Git](https://git-scm.com/) is used for version control by making use of the Gitpod terminal to add, commit and push to Github.

- [Gitpod](https://gitpod.io/) is a platform that streamlines developer workflows by providing prebuilt, collaborative development environments in your browser - powered by VS Code.

- [Github](https://github.com/) is a provider of Internet hosting for software development and version control using Git.

- [Heroku](https://signup.heroku.com/) is a cloud platform as a service supporting several programming languages.

- [AWS](https://aws.amazon.com/) offers reliable, scalable, and inexpensive cloud computing services for storing files.

### **Tools**

- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) was used to inspect my website in Google Chrome.

- [Moqups](https://moqups.com/) was used to create mockups of the finished website.

- [Am I Responsive](http://ami.responsivedesign.is/) was used to check the responsiveness and compatibility of the application on different screen sizes.

- [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) was used to run reports about the performance, accessibility and best practices.

- [Favicon](https://favicon.io/favicon-converter/) was used to design a favicon for the application.

### **Resources**

- [Django Docs](https://docs.djangoproject.com/en/3.2/) were very helpful in setting up Django and to diagnose minor issues I experienced in development.

- [w3schools](https://www.w3schools.com/) is a great resource for all software development queries.

- [Stack Overflow](https://stackoverflow.com/) is an extremely helpful forum to pose questions and queries, which is used by other developers.

- [Stripe Docs](https://stripe.com/docs) were used in setting up Stripe Payments for my store. The documentation is clear and comprehensive.

## 7. Features

### Features unique to the admin:

- The admin has access to the CRUD functionality such as creating items, reading items, updating items and deleting items.

- The store owner (admin) has the ability to update the products in the store. The admin can add new products to the range by submitting the 'add product' form. After submission the product will be added to the database.

- The store owner has the ability to edit items in the product range. The admin can edit fields for product name, description, price etc on the 'edit products' form. Upon submission, the new details are saved in the database.

- The admin also has the ability to delete items in the product range. The admin can delete any products by clicking the delete button on the Products page or the Products Detail page.

- The admin has the capability to create new blog posts. The admin can add new posts to the blog by submitting the 'add post' form. After submission the post will be added to the blog.

- The admin can edit existing posts in the blog by updating the 'edit post' form. The new details will be updated in the blog.

- The admin can delete posts from the blog. The admin can delete any post by clicking the delete button on the Blog page or the Post Detail page.

### Features to implement in future:

- Pagination

Pagination can be added as the number of items in our store increases. Currently, there are 40 products in the store and so, pagination is not required but will be a useful addition in future.

- Product Ratings

Ratings will give users an opportunity to score their favourite products. Users will also be able to sort products by rating.

- Product Suggestion Form

Users will be given the opportunity to fill out a simple form if they would like to suggest a product that could be added to the store.

- Social Media Sign In

Signing in using social media accounts will make it much easier for users to register their account and will provide additional information for marketing purposes.

- Returns Policy

A policy can be implemented to allow customers to return goods if they are unsatisfied or have a change of mind. This will add to the legitimacy of the e-commerce store and will encourage more first-time users to shop on our website.

- Incoming Products

A feature can be implemented to promote products which will soon be available to purchase in the store. Future products can include suggestions from shoppers.

<span  id="testing"></span>

## 8. Testing

Please see [TESTING.md](https://github.com/alandoherty95/siopa_worldwide/blob/master/TESTING.md)

<span  id="deployment"></span>

## 9. Deployment

This application required the following to run:

- **Python3**

- **Django**

- **Django Allauth**

- **Stripe**

- **PIP**

> The full list of requirements can be found in the requirements.txt file

### Gitpod Reminders

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

- A blue button should appear to click: _Make Public_,

- Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.

2. Scroll down to the _API Key_ and click _Reveal_

3. Copy the key

4. In Gitpod, from the terminal, run `heroku_config`

5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

### **AWS**

[AWS](https://aws.amazon.com/console/) was utilised when deploying my application. AWS was used to host both the static and media files for this project. I took the following steps to set up AWS:

#### 1. Go to [AWS](https://aws.amazon.com/)

- Create an account
- Search for S3 and select it by clicking on it

#### 2. Create a new bucket

- Select the region closest to you
- Uncheck block all public access
- Click create bucket

#### 3. In the properties section:

- Turn on static web hosting
- Enter a default values for the index and error documents
- Click save

#### 4. In the permissions section

- Add the cors configuration
- Go to the bucket policy section
- Select policy generator
- The policy type will be s3 bucket policy
- Allow all principals by using the \* symbol
- Select get object

#### 5. Copy the ARN and paste it into the ARN box

- Click add statement
- Click generate policy
- Copy this policy into the bucket policy editor
- Select to allow access to all resources in this bucket by adding a /\* to the end of the resource key
- Click save button
- Go to the access control list section
- Set the list objects permission for everyone under the public access section

#### 6. Create a user with access to the bucket\*\*

- From the services menu, open IAM
- Click groups
- Create a new group

#### 7. Create the policy used to access the bucket

- Click policies
- Create policy
- Go to the JSON tab
- Select import managed policy
- Search for s3
- Import the s3 full access policy
- Get the bucket ARN from the bucket policy page in s3
- Paste it into the field
- Click on review policy
- Enter a name and description
- Click on create policy

#### 8. Attach the policy

- Go to groups
- Click on the group you just created
- Click attach policy
- Search for the policy you just created and select it
- Click attach policy

#### 9. Create a user

- Click add user
- Enter a name and give programmatic access
- Click on next button
- Click through to the end and then create user
- Download the CSV file which will contain the user access key and secret access key which need to be added to the Heroku config vars

<span  id="credits"></span>

## 10. Credits

- [Heroku](https://dashboard.heroku.com/apps) for supplying a platform for deploying my website.

- [Bootstrap](https://getbootstrap.com/) for providing a free and open-source CSS framework directed at responsive, mobile-first front-end web development.

- [W3Schools](https://www.w3schools.com/) for providing a wealth of information about HTML, CSS and JavaScript. It was a very informative and beneficial resource.

- [GitHub](https://github.com/) for hosting for software development and version control.

- [Google Fonts](https://fonts.google.com/) for making the web more beautiful, fast, and open through great typography. A resource that is very easy to use.

- [Slack](https://app.slack.com/client/T0L30B202/C016NG69WG3) community is always helpful and motivating. It is great for asking questions and discussing challenges.

- [Stack Overflow](https://stackoverflow.com/) for providing a platform for questions and answers by professional and enthusiast programmers.

- [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma/) for offering a comprehensive course and walk-through project.

- [Stack Overflow](https://stackoverflow.com/) for providing a forum for posing questions and queries relating to software development.

- [YouTube](https://www.youtube.com/) for supplying countless videos and tutorials on a range of subjects,

- [Google](https://www.google.com/) for providing a search engine to find answers in seconds.

<span  id="acknowledgements"></span>

## 11. Acknowledgements

- My Code Institute Mentor [Nishant Kumar](https://github.com/nishant8BITS/) for his continuous help and guidance.

- The Code Institute team for being available to answer any questions or queries I may have.

- My friends lent me their time to demonstrate the website while offering proposals and constructive feedback.

- My peers and colleagues for providing invaluable feedback and suggestions before selecting the products to sell in our store.

- My family for putting up with me during this project and for providing ideas and feedback along the way.

### Disclaimer

This website was developed for educational purposes.
