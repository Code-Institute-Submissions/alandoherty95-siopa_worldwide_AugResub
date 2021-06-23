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

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

---


**[Siopa Worldwide](insert link to deployed website)**

  

  

Welcome to **[Siopa Worldwide](insert link to deployed website)** - a one stop shop for all your favourite Irish products. We are dedicated to keeping you stocked up with Irish food and drinks no matter where in the world you are located!

  

  

![Website Mockup](insert website mockup)

  

  

<span id="top"></span>

  

  

![Reciprocate Logo](insert website logo)

  

  

**[Siopa Worldwide](insert link to deployed website)** is a full-stack application selling Irish goods around the globe. The website is designed to showcase the most popular Irish food, beverages and as well as other products.

  

  

## Table of Contents

  

  

1. <a href="#context">**Context**</a>

  

  

2. <a href="#ux">**User Experience (UX)**</a>

  

  

3. <a href="#scope">**Scope**</a>

  

  

4. <a href="#structure">**Structure**</a>

  

  

5. <a href="#wireframes">**Wireframes**</a>

  

  

6. <a href="#technologies">**Technologies**</a>

  

  

7. <a href="#database">**Database**</a>

  

  

8. <a href="#features">**Features**</a>

  

  

9. <a href="#testing">**Testing**</a>

  

  

10. <a href="#deployment">**Deployment**</a>

  

  

11. <a href="#credits">**Credits**</a>

  

  

12. <a href="#acknowledgements">**Acknowledgements**</a>

  

  

<span id="context"></span>

  

  

## 1. Context

  

  

The purpose of this project is to create an e-commerce store specialising in Irish goods. I chose this angle due to the bountiful number of Irish people who live outside of their homeland but still desire Irish products. Typically, Irish people living abroad will find it difficult to source authentic Irish food and beverages. I was able to identify a niche market which can be utilised by anyone who craves Irish products regardless of their location in the world. In preparation for this project, I conducted research on friends, colleagues and family members to identify the most popular food and beverage products which can not be easily found outside of Ireland.

  

The application is designed with user experience in mind. The website allows users to easily browse through the range of products in our database. Shoppers can use the sorting and searching features to easily find their desired products. The shoppers can add items to their bag with a running cost displayed in the top right corner at all times. The user can complete an order by making a purchase and a confirmation message will be sent via email. The website is intuitive and the purpose is immediately clear to any first-time visitors.

  

  

<span id="ux"></span>

  

  

## 2. User Experience (UX)

  

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

  ## **Technologies Used**

### **Languages**

-   **HTML**  - used to create the main structure of the application
-   **CSS**  - used to position components and style the application
-   **JavaScript**  - used to for interactivity throughout website
-   **Python**  - used to handle backend functionality

### **Libraries and Frameworks**

-   [Django](https://www.djangoproject.com/)
-   [Bootstrap4](https://getbootstrap.com/)
-   [Stripe](https://www.stripe.com/)
-   [Google Fonts](https://fonts.google.com/)
-   [Font Awesome](https://fontawesome.com/)
-   [jQuery](https://code.jquery.com/)
-   [Pillow](https://pypi.org/project/Pillow/2.2.1/)
-   [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
-   [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

### **Project Management**

-   [Git](https://git-scm.com/)
-   [Gitpod](https://gitpod.io/)
-   [Github](https://github.com/)
-   [Heroku](https://signup.heroku.com/)

### **Tools**

-   [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
-   [Moqups](https://moqups.com/)
-   [Am I Responsive](http://ami.responsivedesign.is/)
-   [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en)
-   [Favicon](https://favicon.io/favicon-converter/)


### **Resources**

-   [Django Docs](https://docs.djangoproject.com/en/3.2/)
-   [w3schools](https://www.w3schools.com/)
-   [Stack Overflow](https://stackoverflow.com/)


