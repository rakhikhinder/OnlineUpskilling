### OnlineUpskilling  - Testing

Visit the deployed site: https://onlineupskilling-1cd3c53acce4.herokuapp.com/

CONTENTS
AUTOMATED TESTING

W3C Validator

JavaScript Validator

Lighthouse

MANUAL TESTING

Testing User Stories

Full Testing

### AUTOMATED TESTING
W3C Validator
W3C Validator was used to validate all HTML pages and the CSS stylesheet.

index.html - Passed 

game.html - Passed with 1 warning (empty <h2>, populated dynamically via JS)

scores.html - Passed 

404.html - Passed 

500.html - Passed 

style.css - Passed 

JavaScript Validator
JSHint was used to validate all JavaScript files.

main.js - Passed 

quiz.js - Passed with 1 warning (async usage, ES8 feature)

scores.js - Passed 

Note: Some warnings about unused variables were incorrect as those variables are used in function scope or dynamically.

Lighthouse
Lighthouse testing was performed in Chrome DevTools for desktop and mobile views.

Desktop
Performance: 100

Accessibility: 100

Best Practices: 100

SEO: 100


Mobile
Performance: 98

Accessibility: 100

Best Practices: 100

SEO: 100


MANUAL TESTING
Testing User Stories
First Time Visitors
User Goal	How It's Achieved
Understand the purpose of the site quickly	Clear title, description and CTAs
Use the site on any device	Responsive design tested on multiple devices
Easy navigation	Intuitive buttons and layout

### Returning Visitors
User Goal	How It's Achieved
Play again easily	Replay buttons and persistent links
Increase difficulty	Option to choose difficulty

### Frequent Visitors
User Goal	How It's Achieved
Improve score and track it	High scores feature
Challenge self with harder levels	Multiple difficulties supported

### Full Testing
Tested devices:

 ### Laptop: MacBook Pro 14”

 ### Mobile: iPhone 13, iPhone XR, Pixel 6

### Browsers: Chrome, Safari, Firefox

### Additional feedback gathered from testers on multiple devices with 

### Feature Testing Summary
Each section below includes expected results, testing steps and actual outcomes.

### Homepage
Feature	Expected Outcome	Result	Pass/Fail
Title click	Redirects to homepage	Redirect successful	
How to Play Modal	Opens instructions	Works correctly	
Buttons hover effect	Changes color on hover	All worked	
Cursor style cursor on hover	Cursor displays correctly	

### Game Page
Feature	Expected Outcome	Result	Pass/Fail
Difficulty selection	Loads correct API questions	Console confirmed correct call	
Score counting	10 pts per correct answer	Working correctly	
Answer validation	Correct/incorrect visual feedback	Border and buttons update properly	
Next button	Loads next question or ends game	Functions as expected	

### End of Quiz
Feature	Expected Outcome	Result	Pass/Fail
Score display	Shows final score	Displays correctly	
Team name input	Enables submit button	Works as intended	
Submit	Adds to high scores, redirects	Redirects to scores page	

### High Scores Page
Feature	Expected Outcome	Result	Pass/Fail
High scores list	Displays top 10	Sorts and displays correctly	
Play again/home buttons	Redirect appropriately	Both work correctly	

### 404 / 500 Pages
Feature	Expected Outcome	Result	Pass/Fail
Buttons redirect	Go Home, Play Again, View Scores	All function properly	
Cursor hover effects  and hover styles	All behave correctly	
