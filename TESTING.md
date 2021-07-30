# Testing

[View README](https://github.com/alandoherty95/siopa_worldwide/blob/master/README.md)

## []()Table of Contents

- [Getting Set Up]()

- [HTML Validator]()

- [W3C Validators]()

- [JSHint Validator]()

- [Python Checker]()

- [Code Beautify]()

- [Deployment]()

- [User Story Testing]()

- [Manual Testing]()

- [Bugs]()

- [User Testing]()

## Getting Set Up

1. Create repository using the [Code Institute Gitpod template](https://github.com/Code-Institute-Org/gitpod-full-template).

2. To install django, enter ‘pip3 install django’ in the terminal.

3. To create the project in the current directory, enter ‘django-admin startproject siopa-worldwide .’ in the terminal.

4. Create a basic gitignore file by entering ‘touch .gitignore’ in the terminal.

5. Run the project by entering ‘python3 manage.py runserver’ in the terminal and exposing port 8000.

6. Stop the server by typing ‘Control + C’ in the terminal.

7. Run the initial migrations by entering ‘python3 manage.py migrate’ in the terminal

8. Create a superuser to log in as admin by entering ‘python3 manage.py createsuperuser’ in the terminal.

9. Enter username, email address and password when prompted in the terminal.

10. To push changes to GitHub, enter ‘git add -A’ in the terminal to add all the files.

11. Enter ‘git commit -m ‘Initial commit’ to provide a commit message.

12. Enter ‘git push’ to push commit to the repo.

### [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

To use the Django Allauth templates, enter ‘pip3 install django-allauth==0.41.0’ in the terminal.

The request context processor here allows allauth and django to access the HTTP request object in our templates. The authentication backends we added give us a really nice feature, allowing users to sign into our store simply using their email address.

The applications we added to our installed apps are allauth and account. The allauth app allows all the basic user account features like logging in and out, user registration and password resets. The other one is for social accounts which specifically handles logging in via social media providers like Facebook and Google. This features will be developed in upcoming versions of the application.

## Code Validators

This code for this application was put through vigorously tested online using the W3C Validators. During development, I manually tested the code and features of the application to identify any bugs. Once the website was successfully deployed, I continued testing using automatic testing.

### [W3C Validators]()

The W3C Markup Validator and W3C CSS Validator Services were used to validate the code on all of the pages across all apps, and to make sure that there were no syntax errors in the project.

- [W3C Markup Validator](https://validator.w3.org/)

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

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

- Password: \***\*\*\*\*\*\*\***

- Logged in as alandoherty95@gmail.com

To prevent Heroku from trying to collect static files when we deploy the application:

- Enter ‘heroku config:set DISABLE_COLLECTSTATIC=1 --app siopa-worldwide'

- Enter ‘git push heroku master'

I created the application on the website rather than in the CLI, so I had to initialise the Heroku git remote:

- Enter ‘heroku git:remote -a siopa-worldwide'

- Re-enter 'git push heroku master'

# User Stories Table

![User Stories Table](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/user-stories.png?raw=true)

# Manual Testing Steps

## 1. Home

### General :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click every navigation bar option

### Logged in users have more options in navigation bar :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Check if navigation bar contains  
   Siopa Worldwide  
   Products  
   Food
   Drinks
   Search bar  
   User profile icon  
   Shopping bag icon
4. Click user profile icon and login with details for registered user
5. Check that the following options appear when the user profile icon is clicked:
   Product Management
   Profile
   Logout

### Search bar :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on search bar
4. Input keyword and click on search icon
5. View all items relating to keyword

### Shop Now button :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on 'Shop Now' button
4. View all products

## 2. Products

### Shop for products :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on the 'Shop Now' button
4. Browse range of products

### Sort products :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on the 'Shop Now' button
4. Click dropdown list of sorting options
5. Sort items in ascending or descending order according to:  
   Price
   Name
   Category

### Browse categories :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on the 'Shop Now' button
4. Click Kids - T-Shirt or Grown Ups - Sweatshirts
5. Check different card design for regular, sale(red) and pre-order(blue) items

### Anonymous user :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on the 'Shop Now' button
4. Choose any product by clicking on the image
5. Opens product detail page containing:
   Product name
   Product image  
   Description  
   Add to bag button  
   Continue shopping button

## 3. Shopping bag

### Empty shopping bag :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on shopping bag icon
4. Displays message 'Your shopping bag is currently empty.' with a button to continue shopping

### Add item to shopping bag :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on the 'Shop Now' button
4. Choose any product by clicking the image
5. Click add to bag button
6. Displays contents of shopping bag in toast message

### Open shopping bag :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on shopping bag icon
4. View all contents of shopping bag

### Update quantity of item in shopping bag :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on the 'Shop Now' button
4. Choose any product by clicking the image
5. Click add to bag button
6. Displays contents of shopping bag in toast message
7. Click on quantity increment button
8. Increases quantity of item in shopping bag

### Checkout from shopping bag notification :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on the 'Shop Now' button
4. Choose any product by clicking the image
5. Click add to bag button
6. Displays contents of shopping bag in toast message
7. Click on complete order button
8. Fill out required details for delivery and payment
9. Click on pay button
10. Displays order summary

### Checkout from shopping bag page :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on the 'Shop Now' button
4. Choose any product by clicking the image
5. Click add to bag button
6. Click on shopping bag icon
7. Click on complete order button
8. Fill out required details for delivery and payment
9. Click on pay button
10. Displays order summary on checkout success page

### Remove item in shopping bag notification :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on the 'Shop Now' button
4. Choose any product by clicking the image
5. Click add to bag button
6. Displays contents of shopping bag in toast message
7. Click on trash icon
8. Removes item from shopping bag

### Remove item on shopping bag page :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on the 'Shop Now' button
4. Choose any product by clicking the image
5. Click add to bag button
6. Click on shopping bag icon
7. Click on trash icon
8. Removes item from shopping bag

## 4. Checkout :white_check_mark:

### Checkout for an anonymous User :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on the 'Shop Now' button
4. Choose any product by clicking the image
5. Click add to bag button
6. Click on shopping bag icon
7. Click on complete order button
8. Fill out required details for delivery and payment (test credit card: 4242 4242 4242 4242)
9. Click on pay button
10. Displays order summary on checkout success page

### Checkout for a registered user :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click on the 'Shop Now' button
4. Choose any product by clicking the image
5. Click add to bag button
6. Click on shopping bag icon
7. Click on complete order button
8. Details for user and delivery should already be populated if user provided details previously
9. Enter payment details (test credit card: 4242 4242 4242 4242)
10. Click on pay button
11. Displays order summary on checkout success page

## 5. Sign Up :white_check_mark:

### Sign Up :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click user profile icon
4. Click Register
5. Enter details in the form
6. Click update information button
7. Login with username and password

## 6. Sign In :white_check_mark:

### Sign In :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click user profile icon
4. Click Login
5. Login with username and password

## 7. Profile :white_check_mark:

1. Open Browser
2. Open [Siopa Worldwide](https://siopa-worldwide.herokuapp.com/)
3. Click user profile icon and login with username and password
4. Click on user account icon
5. Click on profile
6. Displays personal details and order history

## 8. Product Management :white_check_mark:

Product Management :white_check_mark:

- Add new product :white_check_mark:
- Edit an existing product :white_check_mark:
- Delete a product :white_check_mark:

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

![Manual Testing Table 1](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/manual-testing-table1.png?raw=true)

![Manual Testing Table 2](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/manual-testing-table2.png?raw=true)

#### Toast Messages

![Add product to bag toast](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/toast-add-product-to-bag.png?raw=true)

> Adding a product to shopping bag

![Deleted product from bag toast](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/toast-deleted-product.png?raw=true)

> Successfully deleted a product to shopping bag

![Deleted product from bag toast](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/toast-edit-product.png?raw=true)

> Editing details for a product

![Order confirmation toast](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/toast-order-confirmation.png?raw=true)

> Order confirmation

![Signed in toast](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/toast-signed-in.png?raw=true)

> Signed in to account

> ![Signed out toast](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/toast-signed-out.png?raw=true)

> Signed out of account

![Updated product toast](https://github.com/alandoherty95/siopa_worldwide/blob/master/media/toast-updated-product.png?raw=true)

> Updated product details

### Navigation Bar

#### Desktop View

### Checked with HTML Validator

- bag.html
- checkout_success.html
- checkout.html
- index.html
- add_product.html
- edit_product.html
- product_detail.html
- products.html
- profile.html
- nav-bar.html
- mobile-header.html
- base.html
- toast_error.html
- toast_info.html
- toast_success.html
- toast_warning.html

### Checked with CSS Validator

- base.css
- checkout.css
- profile.css

## Automated Testing

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

### Unresolved Bugs

In mobile view, the shopping bag display the current amount in dollars. In all other views, it is displayed correctly in euro.

### Making Stripe Payments

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

Step 3: Then in the JavaScript on the client side, it'll call the confirm card payment method from stripe JS using the client secret which will verify the card number.

[https://stripe.com/docs/payments/accept-a-payment-synchronously](https://stripe.com/docs/payments/accept-a-payment-synchronously)

[https://stripe.com/docs/payments/handling-payment-events](https://stripe.com/docs/payments/handling-payment-events)

- No authentication (default U.S. card): `4242 4242 4242 4242`.

- Authentication required: `4000 0027 6000 3184`.
