
  
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

  

  

Welcome alandoherty95,

  

  

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use.

  

  

## Gitpod Reminders

  

  

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

  

  

`python3 -m http.server`

  

  

A blue button should appear to click: _Make Public_,

  

  

Another blue button should appear to click: _Open Browser_.

  

  

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

  

  

A blue button should appear to click: _Make Public_,

  

  

Another blue button should appear to click: _Open Browser_.

  

  

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

  

  

To log into the Heroku toolbelt CLI:

  

  

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.

  

2. Scroll down to the *API Key* and click *Reveal*

  

3. Copy the key

  

4. In Gitpod, from the terminal, run `heroku_config`

  

5. Paste in your API key when asked

  

  

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidently make it public then you can create a new one with _Regenerate API Key_.

  

  

## Updates Since The Instructional Video

  

  

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

  

  

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

  

  

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

  

  

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

  

  

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

  

  

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

  

  

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

  

  

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

  

  

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

  

  

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a  href="https://github.com/Eventyret/vscode-bcdn"  target="_blank">README.md file at the official repo</a> for more options.

  

  

---

  

  

**[Siopa Worldwide](insert link to deployed website)**

  

  

  

  

Welcome to **[Siopa Worldwide](insert link to deployed website)** - a one stop shop for all your favourite Irish products. Siopa Worldwide is an e-commerce store, offering a range of popular Irish food and beverages. We are dedicated to keeping you stocked up with your favourite Irish food and drinks no matter where in the world you are located!

  

  

  

![Website Mockup](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/mockup-original.png?raw=true)

  

  

  

  

<span  id="top"></span>

  

  

  

  

![Siopa Worldwide Logo](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/siopa-logo-home.png?raw=true)

  

  

  

  

**[Siopa Worldwide](insert link to deployed website)** is a full-stack e-commerce application selling Irish goods around the globe. The website is designed to showcase the most sought-after food and beverages known to Ireland. Users of the application can browse through our growing range of products before purchasing their favourites. The user will be prompted to enter their personal details, delivery details and payment details when completing an order. The user will then receive an order confirmation via email. Siopa Worldwide allows users to create an account, update items in their shopping bag, complete purchases and view their order history.

  

  

  

  

## Table of Contents

  

  

  

  

1.  <a  href="#context">**Context**</a>

  

  

  

  

2.  <a  href="#ux">**User Experience (UX)**</a>

  

  

  

  

3.  <a  href="#scope">**Scope**</a>

  

  

  

  

4.  <a  href="#structure">**Structure**</a>

  

  

  

  

5.  <a  href="#wireframes">**Wireframes**</a>

  

  

  

  

6.  <a  href="#technologies">**Technologies**</a>

  

  

  

  

7.  <a  href="#database">**Database**</a>

  

  

  

  

8.  <a  href="#features">**Features**</a>

  

  

  

  

9.  <a  href="#testing">**Testing**</a>

  

  

  

  

10.  <a  href="#deployment">**Deployment**</a>

  

  

  

  

11.  <a  href="#credits">**Credits**</a>

  

  

  

  

12.  <a  href="#acknowledgements">**Acknowledgements**</a>

  

  

  

  

<span  id="context"></span>

  

  

  

  

## 1. Context

  

  

  

  

The purpose of this project is to create an e-commerce store specialising in the most sought-after Irish products. I chose this angle due to the bountiful number of Irish people who live outside of their homeland but still desire Irish products. Tens of thousands of Irish people emigrate to other countries every year. Typically, Irish people living abroad will find it difficult to source authentic Irish food and beverages. I was able to identify a niche market which can be utilised by anyone who craves Irish products regardless of their location in the world. In preparation for this project, I conducted research on friends, colleagues and family members to identify the most popular food and beverage products which are not easily found outside of Ireland.

  

  

  

The application is simply designed with user experience in mind. The website allows users to easily browse through the range of products in our database. Shoppers can use the sorting and searching features to easily find their desired products. The shoppers can add items to their bag with a running cost displayed in the top right corner at all times. The user can complete an order by making a purchase and a confirmation message will be sent via email. The website is intuitive and the purpose is immediately clear to any first-time visitors.

  

  

  

  

<span  id="ux"></span>

  

  

  

  

## 2. User Experience (UX)

  

  ### The Five Planes of UX

#### []()The Strategy Plane

After conducting market research on friends, peers and family members
I identified a niche market which can be utilised by anyone who craves Irish food and beverages no matter where they are in the world. I want to create an application focusing purely on the most popular Irish goods which are not easily found outside of Ireland. Every shopper will have the ability to create their own account, safely provide their personal information and securely complete an order.

#### []()The Scope Plane

When deciding on the scope of my project, I decided to design a website allowing users to create an account, browse products, add items to their shopping cart and securely complete an order. The primary feature will be the capability to purchase a product through a secure checkout using Stripe Payments. Shoppers can easily sort products by name, price or category. Shoppers can easily search for products, using keywords. To improve the user experience, I want users to be notified of their actions, such as shopping bag updates as well as success and error messages.

#### []()The Structure Plane

After deciding on the features I wanted to include, I focused on the overall structure of the website. I want to keep the design clean and sleek. All potential customers will be able to search for a product using keywords but can also use a sorting feature depending on the needs of the user. I am using the grid system from Bootstrap to clearly display the content of each page. The navigation bar will change depending if the user is anonymous or logged in. Clicking 'Profile' in the navigation bar, reveals more options via a dropdown list. The store owner (admin), signed in as a superuser, can also access the product management page. The store owner will have the option to add, edit or delete items from the product range.

#### []()The Skeleton Plane

I wanted a clear, simple structure throughout the website. Each page will have a fixed navigation bar with consistent styling and prominent call-to-action buttons. There will be a large call-to-action button on the home screen to invite shoppers to browse all products. Each page has a unique heading so users are aware of which page they are on at all times. The products page displays all items neatly, allowing users to view multiple products on the same page. Clicking on a product will direct the shopper to a more detailed view about the individual item. Shoppers can simply add items to their shopping bag with a toast message appearing in the top right corner of the screen when an action is completed. Users can enter their personal information confident in the application's security features. Shoppers can  complete their checkout and receive an email confirmation of their order.



#### []()The Surface Plane

From conducting research on similar e-commerce sites, I discovered most online stores are quite colourful and brimming with information. Conversely, I wanted to keep the design sleek and simple, only displaying relevant information to the user. Initially, I sketched ideas and wireframes onto paper, before recreating more advanced wireframes online. I designed all the pages for desktop and smaller screen sizes showing the structure and content on the different devices.

  

### Design Process

  

  

  

During the research phase of this project, I posed the following questions to friends, family members and peers living abroad:

  

  

  

- Which Irish goods do you desire most while living abroad?

  

  

- Which online stores do you use for buying Irish goods?

  

  

- What are your favourite brands of Irish food and drinks?

  

  

- What kind of Irish goods can you purchase in your town or city?

  

  

- Is there any store specialising in Irish products in your town or city?

  

  

### Target Market

  

  

  

The e-commerce store is primarily targeting Irish people who are living abroad. It is difficult for most Irish people living in a foreign country to find their favourite Irish food and beverages. There is a niche market for selling Irish goods to Irish people living abroad.

  

  

  

### Overview

  

  

  

  

The website was designed with three main objectives:

  

  

  

  

- To allow users to browse all products in our database using sorting and searching features

  

  

  

  

- To allow shoppers to complete an order by purchasing their desired products

  

  

  

  

- To allows shoppers to create an account and view previous orders

  

  

  

### **Project Goals**

  

  

- As an owner of this e-commerce store, I would like to:

  

  

- to encourage users to visit the store

  

  

- to encourage users to browse our range of products

  

  

- to encourage users to buy products from the store

  

  

- to encourage users to return to the website again

  

  

- to create, update and delete items in our product range

  

  

  

### **User Stories**

  

  

  

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

  

  

**Create Account**

  

  

  

- create an account easily and quickly

  

  

  

#### **As a registered user:**

  

  

  

- log in and out easily and quickly

  

  

- reset my password if it is forgotten

  

  

- receive a confirmation message that I have successfully registered an account

  

  

- view my personal profile

  

  

- view my order history in my profile page

  

  

- save my default delivery details for future orders

  

  

- easily update my delivery information

  

  

  

#### **As a Superuser:**

  

  

  

- access the admin panel easily

  

  

- create, update and delete categories

  

  

- add new items to our product range

  

  

- edit or delete existing items from our product range

  

  

- view and manage users of the site

  

  

- view and manage orders

  

  

## **Design and Development**

-   Browse products
-   View product details
-   Create an account
-   Log in/log out
-   Add items to shopping bag
-   View items in shopping bag
-   Edit and update items in shopping bag
-   Delete items from shopping bag
-   Complete an order
-   View order history
-   Search for specific items using keywords
-   Sort items by name, price or category

  

### **Design Process**

  

  

The primary design goal in mind when designing this application is to attract the customer to explore further. The landing page is bright and striking. There is a prominent call-to-action button inviting users to 'Shop Now'. This button will leads the user to the products page where they can browse all items in our product range.

  

- Design a bright and visually appealing application.

  

- Design an intuitive and easy to navigate website.

  

- Achieve a clean aesthetic displaying only the necessary information.

  

- Use Bootstrap4 features for the layout and structure of the application

  

- Use Bootstrap4 classes and components to provide structure as well as highlighting and enhancing different elements.

  

- Design an application which is responsive on all screen sizes.

  

- Design a logo that is simple, attractive and memorable.

  
The colour scheme chosen for this project was inspired by bright colours to give the website an attractive, vibrant look. The white background gives a sleek, neutral look to the application with green and black nicely complementing.
    
  [Colour Scheme](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/colour-palette.png?raw=true)
   
-   **#FFFFFF White**  is the backdrop of all headings and text on the website. The bright colour emphasises clarity and removes visual clutter. The black text is easily readable on the white background.
    
-   **#169B62 Green**  is used for some buttons seen throughout the website. The buttons were designed to be large and prominent. The bright green button on the white background grabs the attention of the user.

-   **#FFFFFF Black**  is used for headings and text on the website. The black text is easily read on the white background. Black is also used throughout the application for buttons. 
  
  #### Typography

[Indie Flower Font](https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap) was used because of the bubbly, rounded edges. It grabs the user's attention in contrast to the straight, simple Oswald font.

[Oswald Font](https://fonts.googleapis.com/css2?family=Oswald&display=swap)
was used for the primary text because it is easy to read. Oswald is designed to be used freely across the internet by web browsers on desktop computers, laptops and mobile devices.
 

#### **Development Process**

  

  

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

  

- Create a home app

  

- Create a products app to display all items in our product range

  

- Create a bag app to display the contents of the shopping bag

  

- Create a checkout app

  

- Create a profile app

  

- Create additional elements contributing to the user experience such as toasts and messages

  

- Adjust and tailor the layout and styling of each page

  

  

## **Wireframes**

  

  

![Home Page](https://github.com/alandoherty95/siopa_worldwide/blob/master/wireframes/desktop-wireframes/index-wireframe.png?raw=true)

  

  

![Products Page](https://github.com/alandoherty95/siopa_worldwide/blob/master/wireframes/desktop-wireframes/products-wireframe.png?raw=true)

  

  

![Product Detail Page](https://github.com/alandoherty95/siopa_worldwide/blob/master/wireframes/desktop-wireframes/product-detail-wireframe.png?raw=true)

  

![Shopping Bag Page](https://github.com/alandoherty95/siopa_worldwide/blob/master/wireframes/desktop-wireframes/bag-wireframe.png?raw=true)

  

![Checkout Page](https://github.com/alandoherty95/siopa_worldwide/blob/master/wireframes/desktop-wireframes/checkout-wireframe.png?raw=true)

  

## **Technologies Used**

  

  

### **Languages**

  

  

-  **HTML** - used to create the main structure of the application

  

-  **CSS** - used to position components and style the application

  

-  **JavaScript** - used to for interactivity throughout website

  

-  **Python** - used to handle backend functionality

  

  

### **Libraries and Frameworks**

  

  

-  [Django](https://www.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

  

-  [Bootstrap4](https://getbootstrap.com/) is a powerful front-end framework for faster and easier web development including forms, buttons and navigations.

  

-  [Stripe](https://www.stripe.com/) offers payment processing software and application programming interfaces for e-commerce websites and mobile applications.

  

-  [Google Fonts](https://fonts.google.com/) provides a curated collection of the best free fonts available online.

  

-  [Font Awesome](https://fontawesome.com/) is a font and icon toolkit based on CSS.

  

-  [jQuery](https://code.jquery.com/) is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling and CSS animation.

  

-  [Pillow](https://pypi.org/project/Pillow/2.2.1/) is a Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.

  

-  [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) is an application that helps to manage Django forms.

  

-  [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) is an integrated set of Django applications addressing authentication, registration and account management.

  

  

### **Project Management**

  

  

-  [Git](https://git-scm.com/) is used for version control by making use of the Gitpod terminal to add, commit and push to Github.

  

-  [Gitpod](https://gitpod.io/) is a platform that streamlines developer workflows by providing prebuilt, collaborative development environments in your browser - powered by VS Code.

  

-  [Github](https://github.com/) is a provider of Internet hosting for software development and version control using Git.

  

-  [Heroku](https://signup.heroku.com/) is a cloud platform as a service supporting several programming languages.

  

  

### **Tools**

  

  

-  [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)

  

-  [Moqups](https://moqups.com/)

  

-  [Am I Responsive](http://ami.responsivedesign.is/)

  

-  [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en)

  

-  [Favicon](https://favicon.io/favicon-converter/)

  

  

### **Resources**

  

  

-  [Django Docs](https://docs.djangoproject.com/en/3.2/)

  

-  [w3schools](https://www.w3schools.com/)

  

-  [Stack Overflow](https://stackoverflow.com/)

  

-  [Stripe Docs](https://stripe.com/docs)

## **Features**
  
Features unique to the admin:

The store owner (admin) has the ability to update the products in the store. The admin can add new products to the range by submitting the 'add product' form. After submission the product will be added to the database.

The store owner has the ability to edit items in the product range. The admin can edit fields for product name, description, price etc on the 'edit products' form. Upon submission, the new details are saved in the database.

The admin also has the ability to delete items in the product range. The admin can delete any products by clicking the delete button on the Products page or the Products Detail page.

## **Testing**

  ### **Resolved Bugs**
- The function allowing user to remove items from the shopping bag wasn't functioning. I realised I forgot to pass 'data' through when submitting the request. I test the function after inputting data to ensure it works correctly.
`$.post(url, data)
.done(function() {
location.reload();
});`
  
- The subtotal calculation was not displaying in the shopping bag. After investigation, I realised the structure of my html table was incorrect. I rearranged the html code and used the code snippet below to correctly calculate the subtotal of each item in the shopping bag. 
`<p  class="my-0">€{{ item.product.price | calc_subtotal:item.quantity }}</p>`

- The error (screenshot below) was displaying in the terminal. I sought help from a Code Institute tutor who kindly pointed out that the code snippet below should be in `checkout/init.py` instead of `bag/init.py`. 
`default_app_config = 'checkout.apps.CheckoutConfig'`

![Improperly Configured Error](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/error-improperly-configured.png?raw=true)

- My initial attempt to deploy to Heroku failed and displayed `{“error”:”Forbidden”}` in the preview panel. Displayed `“IP address mismatch”`in the browser.
![Error 503 Heroku](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/error-503-heroku.png?raw=true)

Stripe Payments

1. Click your checkout button

2. Fill out the payment details with the test card information:

  

- Enter `4242 4242 4242 4242` as the card number.

- Enter any future date for card expiry.

- Enter any 3-digit number for CVC.

- Enter any billing postal code.

  

3. Click Pay.

4. You’re redirected to your new success page.

  

**Payment Intent Process**

Step 1: When a user hits the checkout page, the checkout view will call out to stripe and create a payment intent for the current amount of the shopping bag

  

Step 2: When stripe creates it, it’ll have a secret that identifies it which will be returned to us and we'll send it to the template as the client secret variable.

  

Step 3: Then in the JavaScript on the client side, it’lll call the confirm card payment method from stripe JS using the client secret which will verify the card number.

  

[https://stripe.com/docs/payments/accept-a-payment-synchronously](https://stripe.com/docs/payments/accept-a-payment-synchronously)

  

  

[https://stripe.com/docs/payments/handling-payment-events](https://stripe.com/docs/payments/handling-payment-events)

  

- No authentication (default U.S. card): `4242 4242 4242 4242`.

- Authentication required: `4000 0027 6000 3184`.

