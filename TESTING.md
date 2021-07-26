# Testing

[View README](Insert README link)

## []()Table of Contents

-   [Validators]()
    -   [W3C Validators]()
    -   [JSHint Validator]()
    -   [pylint-django]()
    -   [Markdown]()
-   [User Story Testing]()
-   [Manual Testing]()
-   [Bugs]()
-   [User Testing]()


## Validators

This code for this application was put through vigorously tested online using the W3C Validators. During development, I manually tested the code and features of the application to identify any bugs. Once the website was successfully deployed, I continued testing using automatic testing.

### [W3C Validators]()

The W3C Markup Validator and W3C CSS Validator Services were used to validate the code on all of the pages across all apps, and to make sure that there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

HTML
CSS
JavaScript
Python
Markdown


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


## Manual Testing

Extensive manual testing was completed throughout the development of this application. Once the website was successfully deployed on Heroku, I completed rigorous manual testing to ensure each button and feature was functioning correctly.

### []()Navigation Bar

#### []()Desktop View

-   Search feature - searches all items in the database using a key word to find relevant search results by title or description
    
-   Siopa Worldwide Logo - returns the user to the home screen when clicked on
    
-   Account - reveals a dropdown menu when clicked on:
    
    -   If not authenticated:
        
        -   Register - directs the user to the registration page and invites them to create an account
            
        -   Login - directs the user to the login page
            
    -   If user is authenticated:
        
        -   Profile - directs the user to their unique profile page
            
        -   Logout - logs user out of their account, redirects the user to the home page
            
    -   If user is a superuser:
        
        -   Product Management - directs the user to the add product page
            
            
-   Shopping Bag - directs the user to their shopping bag