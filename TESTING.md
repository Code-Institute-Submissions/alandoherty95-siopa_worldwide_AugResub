# Testing

[View README](https://github.com/alandoherty95/siopa_worldwide/blob/master/README.md)

## []()Table of Contents

- [HTML Validator](https://validator.w3.org/#validate_by_input)

- [W3C Validators](https://jigsaw.w3.org/css-validator/)

- [JSHint Validator](https://jshint.com/)

- [Python Checker](https://www.pythonchecker.com/)

- [Code Beautify](https://codebeautify.org/markdown-formatter)

- [Deployment]()

- [User Story Testing]()

- [Manual Testing]()

- [Bugs]()

- [User Testing]()

## Validators

This code for this application was put through vigorously tested online using the W3C Validators. During development, I manually tested the code and features of the application to identify any bugs. Once the website was successfully deployed, I continued testing using automatic testing.

### [W3C Validators]()

The W3C Markup Validator and W3C CSS Validator Services were used to validate the code on all of the pages across all apps, and to make sure that there were no syntax errors in the project.

- [W3C Markup Validator](https://validator.w3.org/)

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

HTML

CSS

JavaScript

Python

Markdown

## Deployment

Before deploying my application on Heroku, I had to take some steps to ensure a successfully deployment.
Firstly, in order to use Postgres, we installed `dj_database_url` and `psycopg2`:

- Enter ‘pip3 install dj_database_url’

- Enter ‘pip3 install psycopg2-binary’

- Enter ‘python3 manage.py showmigrations'

- Enter ‘python3 manage.py migrate'

- Enter ‘python3 manage.py loaddata categories'

- Enter ‘python3 manage.py loaddata products'

We also installed unicorn, which acts as the web server:

- Enter ‘pip3 install gunicorn’

- Enter ‘pip3 freeze > requirements.txt’

To log into Heroku, I had to use my email address and the API key from Heroku:

- heroku login -i

- heroku: Enter your login credentials

  - Email: alandoherty95@gmail.com

  - Password: ******\*\*******

  - Logged in as alandoherty95@gmail.com

To prevent Heroku from trying to collect static files when we deploy the application:

- Enter ‘heroku config:set DISABLE_COLLECTSTATIC=1 --app siopa-worldwide'

- Enter ‘git push heroku master'

I created the application on the website rather than in the CLI, so I had to initialise the Heroku git remote:

- Enter ‘heroku git:remote -a siopa-worldwide'

- Re-enter 'git push heroku master'

## User Stories Table

![User Stories Table](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/user-stories.png?raw=true)

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

## Screenshots

![Desktop Home](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/ss-index.png?raw=true)
The home screen grabs the user's attention with vibrant colours and a prominent call-to-action button. The purpose of the website is immediately clear. Users are encouraged to 'Shop Now'.

![Desktop Sign In](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/ss-sign-in.png?raw=true)

The sign in page is simple and effective in encouraging registered users to log into their profile. First-time users are invited to sign up if they have not created an account yet. There is also the option of resetting passwords if they have forgotten.

![Desktop Sign Up](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/ss-sign-up.png?raw=true)

The sign up page is also pretty simple, requiring just five fields to be filling out when registering. Users are prompted to enter their email address, username and password in order to create an account. Registered users are asked to sign in if they have already created an account.

![Mobile Profile](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/ss-mobile-profile.png?raw=true)

The profile page allows users to save their personal details to ensure a quicker checkout when completing an order. All previous order are displayed on the profile page so user's can view their order history.

![Mobile Empty Bag](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/ss-mobile-empty-bag.png?raw=true)

The shopping bag page informs users when their bag is empty and encourages them to continue shopping. The Siopa Worldwide logo is also displayed here when the shopping bag is empty. If any items are added to the shopping bag, they will appear here in a table with a breakdown of costs.

![Mobile Search Crisps](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/ss-mobile-search-crisps.png?raw=true)

The search feature found at the top of the screen is very useful in finding specific products. Users can enter keywords such as "crisps" or "cheese" and will be shown all results relating to that specific keyword. It is a quick and effective way of finding desired items.

![Mobile Sort Name](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/ss-mobile-sort-name.png?raw=true)

The sorting function can be used to display products in a certain order. By selecting an option from the dropdown list, users can sort by price, category or name in ascending or descending order. This offers offers al alternative way of browsing through the items in our store.

![Mobile Sort Price](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/ss-mobile-sort-price.png?raw=true)

Users can also sort items by price in order of highest to lowest or lowest to highest. This gives users the opportunity to browse products based on their budgetary requirements.

## Manual Testing

Extensive manual testing was completed throughout the development of this application. Once the website was successfully deployed on Heroku, I completed rigorous manual testing to ensure each button and feature was functioning correctly.

### Navigation Bar

#### Desktop View

### Checked with HTML Validator

bag/templates/bag/

- bag.html

checkout/templates/checkout/

- checkout_success.html
- checkout.html

home/templates/home/

- index.html

products/templates/products/

- add_product.html
- edit_product.html
- product_detail.html
- products.html

profiles/templates/profiles/

- profile.html

templates/includes/

- nav-bar.html
- mobile-header.html

templates/

- base.html

templates/includes/toasts/

- toast_error.html
- toast_info.html
- toast_success.html
- toast_warning.html

### Checked with CSS Validator

static/css/

- base.css

checkout/static/checkout/css/

- checkout.css

profiles/static/profiles/css/

- profile.css


## Automatated Testing

- Home

97 Performance
78 Accessibility
100 Best Practices
100 SEO

- Products

90 Performance
77 Accessibility
100 Best Practices
100 SEO


- Product Detail

98 Performance
70 Accessibility
93 Best Practices
100 SEO

- Shopping Bag

98 Performance
68 Accessibility
100 Best Practices
100 SEO


- Checkout

87 Performance
82 Accessibility
100 Best Practices
100 SEO


- Profile

95 Performance
78 Accessibility
100 Best Practices
100 SEO

- Add Product

98 Performance
66 Accessibility
100 Best Practices
100 SEO


- Edit Product

97 Performance
60 Accessibility
100 Best Practices
90 SEO


## Bugs

### Resolved Bugs

### **Resolved Bugs**

- Issue: The function allowing the user to remove items from the shopping bag wasn't functioning.
  - Fix: I realised I forgot to pass 'data' through when submitting the request. I test the function after inputting data to ensure it works correctly.

`$.post(url, data).done(function() {location.reload();});`

- Issue: The subtotal calculation was not displaying in the shopping bag.
  - Fix: After investigation, I realised the structure of my html table was incorrect. I rearranged the html code and used the code snippet below to correctly calculate the subtotal of each item in the shopping bag.

`<p class="my-0">€{{ item.product.price | calc_subtotal:item.quantity }}</p>`

- The error (screenshot below) was displayed in the terminal when running my application in Gitpod.
  - Fix: I sought help from a Code Institute tutor who kindly pointed out that the code snippet below should be in `checkout/init.py` instead of `bag/init.py`.

`default_app_config = 'checkout.apps.CheckoutConfig'`

![Improperly Configured Error](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/error-improperly-configured.png?raw=true)

- Issue: My initial attempt to deploy to Heroku failed displaying `{“error”:”Forbidden”}` in the preview panel and `“IP address mismatch”`in the browser.
  - Fix: With tutor assistance, a typo was identified in the Procfile. The application deployed successfully after correcting typo.

![Error 503 Heroku](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/error-503-heroku.png?raw=true)

- Issue: On the checkout success page, street_address1 was displayed twice mistakenly because the variable `{{ order.street_address1 }}` was duplicated in the html code.

  - Fix: I corrected this by changing the second line to `{{ order.street_address2 }}` instead. Output is now working as expected.

- Issue: Some allauth forms were not displaying correctly, hidden behind the navigation bar.

  - Fix: I updated `{% block content %}` to `{% block inner_content %}` on each allauth template instead. This resolved the issue with styling of each form.

- Issue: The button for updating the quantity of items in the shopping bag was not functioning.
  - Fix: I realised the their was a mismatch between the ID in bag.html and the relevant JS code. I updated the ID in the JS code to `('.update-qty')`. This issue was resolved after testing.

