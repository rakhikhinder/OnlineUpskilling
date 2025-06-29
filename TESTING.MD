### OnlineUpskilling  - Testing

Visit the deployed site: https://onlineupskilling-1cd3c53acce4.herokuapp.com/
![OnlineUpSkilling-Learning Platform](https://github.com/rakhikhinder/OnlineUpskilling/blob/card/image%201%20.jpeg)


### AUTOMATED TESTING
W3C Validator
W3C Validator was used to validate all HTML pages and the CSS stylesheet.

### 📱 Mobile Performance Test

![Mobile Performance](https://github.com/rakhikhinder/OnlineUpskilling/blob/card/static/image/Screenshot%202025-06-29%20143854.png)

Performance test conducted using [PageSpeed Insights](https://pagespeed.web.dev/) to evaluate speed, accessibility, and best practices on mobile devices.

---

### 💻 Desktop Performance Test

![Desktop Performance](https://github.com/rakhikhinder/OnlineUpskilling/blob/card/static/image/Screenshot%202025-06-29%20143835.png)

Performance test conducted using [PageSpeed Insights](https://pagespeed.web.dev/) to evaluate speed, accessibility, and best practices on desktop devices.


Use the site on any device	Responsive design tested on multiple devices
Easy navigation	Intuitive buttons and layout

Below are the screenshots of the results:

![Performance Metrics](https://github.com/rakhikhinder/OnlineUpskilling/blob/card/static/image/Screenshot%202025-06-29%20143746.png)

![Accessibility Metrics](https://github.com/rakhikhinder/OnlineUpskilling/blob/card/static/image/Screenshot%202025-06-29%20143803.png)

![Best Practices Metrics](https://github.com/rakhikhinder/OnlineUpskilling/blob/card/static/image/Screenshot%202025-06-29%20143820.png)

![Overall PageSpeed Result](https://github.com/rakhikhinder/OnlineUpskilling/blob/card/static/image/Screenshot%202025-06-29%20143835.png)



### Full Testing
Tested devices:

 ### Laptop: dell inspiron i5 5000 ”

 ### Mobile: iPhone 13, iPhone XR, Pixel 6

### Browsers: Chrome, Safari, Firefox

### Additional feedback gathered from testers on multiple devices with 


### Manual Testing
### Home Page


| Feature                     | Expected Outcome                                                                     | Testing Performed                                           | Result                    | Pass/Fail |
|----------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------|----------------------------|-----------|
| Navbar links               | All nav links should navigate correctly to their respective pages                     | Clicked each nav link                                       | Navigated as expected      | Pass      |
| Registration button        | Opens the registration form/modal                                                     | Clicked registration                                        | Registration form shown    | Pass      |
| Login button               | Opens the login form/modal                                                            | Clicked login                                               | Login form shown           | Pass      |
| View Product button        | Navigates to the product details page                                                 | Clicked on "View Product"                                   | Product page loaded        | Pass      |
| Reload after login         | User should remain logged in after refreshing the page                                | Logged in, refreshed page                                   | Still logged in            | Pass      |
| Back button functionality  | Clicking browser back button returns to previous screen                               | Navigated forward and used browser back                     | Returned correctly         | Pass      |
| Button hover effect        | All buttons should change background to blue on hover                                 | Hovered over all clickable buttons                          | Background changed to blue | Pass      |
| Title click reload         | Clicking on the site title should reload the home page                                | Clicked on the site title                                   | Home page reloaded         | Pass      |
| Post-login links visible   | Profile and Subscription links should appear after successful login                   | Logged in and checked the navbar                            | Links were visible         | Pass      |



### Register Page

| Feature              | Expected Outcome                                                                 | Testing Performed                                           | Result                    | Pass/Fail |
|---------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------|----------------------------|-----------|
| Username field       | Allows user to input a valid username                                              | Entered text in username field                              | Username accepted          | Pass      |
| Password field       | Allows user to input a secure password                                             | Entered password                                             | Password accepted          | Pass      |
| Confirm Password     | Must match the password entered above                                              | Entered matching and non-matching passwords                 | Shows error on mismatch / allows match | Pass |
| Submit button        | Submits the form only when all fields are valid                                    | Filled valid inputs and clicked submit                      | Form submitted successfully | Pass      |
| Submit button        | Prevents submission when required fields are empty or invalid                      | Tried submitting empty form                                 | Form not submitted, error shown | Pass |
| Home button          | Redirects to the home page                                                         | Clicked home button                                         | Navigated to home page     | Pass      |
| Hover effect         | All buttons should change background to blue on hover                             | Hovered over submit and home buttons                        | Background changed to blue | Pass      |

### Login Page

| Feature              | Expected Outcome                                                             | Testing Performed                          | Result                        | Pass/Fail |
|---------------------|------------------------------------------------------------------------------|--------------------------------------------|-------------------------------|-----------|
| Username field       | Allows user to input a valid username                                        | Entered username                           | Username accepted             | Pass      |
| Password field       | Allows user to input a password                                              | Entered password                           | Password accepted             | Pass      |
| Submit button        | Submits the form only when both fields are filled correctly                  | Entered valid credentials and clicked submit | Logged in successfully        | Pass      |
| Submit button        | Prevents submission with empty or invalid fields                             | Tried submitting empty/invalid inputs      | Form not submitted, error shown | Pass    |
| Hover effect         | Submit button should change background to blue on hover                      | Hovered over the submit button             | Background changed to blue    | Pass      |

### Subscription Page

| Feature                 | Expected Outcome                                                  | Testing Performed                                | Result                           | Pass/Fail |
|------------------------|-------------------------------------------------------------------|-------------------------------------------------|---------------------------------|-----------|
| Plan selection dropdown | Dropdown should list available plans: Basic and Premium          | Clicked dropdown and viewed options              | Both Basic and Premium options shown | Pass      |
| Select plan            | User can select either Basic or Premium plan                      | Selected each plan option                         | Selection updated correctly      | Pass      |
| Subscribe button       | Clicking subscribe redirects to the payment page                  | Selected a plan and clicked Subscribe             | Redirected to payment page       | Pass      |
| Payment page load      | Stripe payment gateway loads correctly                            | Arrived at payment page                            | Stripe payment form displayed    | Pass      |
| Hover effect           | Buttons and dropdown have hover effects                           | Hovered over dropdown and subscribe button        | Visual hover effect visible      | Pass      |

### Stripe Payment Page

| Feature             | Expected Outcome                                      | Testing Performed                      | Result                         | Pass/Fail |
|---------------------|-------------------------------------------------------|--------------------------------------|--------------------------------|-----------|
| Payment form load   | Stripe payment form loads correctly                   | Navigated to payment page             | Payment form visible            | Pass      |
| Back button         | Clicking back returns to the previous subscription page | Clicked back button                   | Redirected to subscription page| Pass      |
| Loading indicator   | Shows loading while payment is processing             | Submitted payment and observed UI    | Loading spinner displayed       | Pass      |
| Payment success flow| After successful payment, user is redirected/confirmed | Completed payment                     | Redirect or confirmation shown  | Pass      |
| Payment failure flow| On payment failure, user sees an error or retry option| Submitted invalid payment             | Error displayed, retry possible | Pass      |
| Hover effect        | Buttons change style on hover                          | Hovered over buttons                  | Visual hover effect visible     | Pass      |
