To do list

figure out why style.css isnt working 

make the footer stick to the bottom of the page 

make sure all the backend works

style the website into a blog website where users who have signed up can add and delete blog posts


the main rationale for this website is so for users to log on and see updates towards the website and update thier profiles to their liking 

MAJOR TO DO LIST 

MAKE SURE USERS CAN CREATE, READ UPDATE AND DELETE STATUS'
ADD REQUIREMENTS.TXT FILE
DEFINE WHAT THE WEBSITE IS USED FOR (COMMUNITY NOTICE BOARD)

MAKE SURE USERS CAN SEE OTHER PEOPLES NOTES ON THE PAGE ON THE MAIN HOME PAGE 

contact heroku about issue signing up to deploy website

make it so admin can only delete blog posts
figure out why url isnt working for home

to do

add admin role
make sure users can delete thier profiles


add admin restrictions

# Gig Reviews
Gig reviews is a website where users can post about their gigs they have been to and would like to leave a review about it on the page it is aimed towards musical people and who have a love for music. It also lets users comment on blog posts, add thier own blog posts and ive also added a gig wishlist feature for gigs they want to see in the future

# User Stories
The purpose of Gig reviews is to let users display their thoughts on the musicians they have seen recently and to see any other reviews about gigs they maybe interesed in from other users

### User Goals
* To learn more about Music
* To have a platform for people to express their opinion about the latest music
* To create a gig wishlist of artists who they would like to see
* To have the option to delete and edit posts the user has made
* To have the option to comment on other users blogs

### Site Owner goals 

* To make a music community where people can express their thoughts on the recent gigs they have been to
* Make a fully functioning blog page where users can, create, read, update and delete thier own posts
* Ensure that only logged-in users can post reviews and comments.
* Make a database where when users have stored their information it can be seen from the admin panel for the admin 
* To give the option for users to remove themselves off the database


# UX Design

Unfortunately due to time constraints and techincal issues I havent been able to fully implement my design into the website so it is very basic at the moment.

But I have gone with a grey/blue/white colour scheme for the majority of the website, with the main purpose of the blog being in the center,





 # WireFrames Desktop

 For the wireframes I didn't have a wireframe designer so I designed the app on Adobe Photoshop.

 ![image](assets/docs/imgdocs/oscarswireframe.png)
 Early Wireframe 
   ![image](assets/docs/imgdocs/wireframe-oscars-main.png "Name page wireframe desktop")
    Here is the wireframe for the main index page, it is a bit different from the final result as the website wasn't mobile friendly at the start so I modified it to make it more mobile friendly. 

   ![image](assets/docs/imgdocs/wireframe-desktop-name.png "main quiz wireframe")
    The Gallery wireframe.

# Features 

1. A Name bar where the username is required to move onto the next stage of the quiz.
   ![image](assets/docs/imgdocs/empty-name.png)
2. A right/wrong answer message depending on if the user got the answer correct or not.
   ![image](assets/docs/imgdocs/wrong-answer.png)
3. A try again button and score round up at the end of the quiz to show the total score for the user.
   ![image](assets/docs/imgdocs/try-again.png)
4. A feature using jquery to show the name on the users quiz card when they are playing the quiz. It also shows up at the end aswell.
   ![image](assets/docs/imgdocs/name-entered.png)

## Future features
 For the future features I would like to add a shop page to the website where the user can click on the image and buy the image from the website and for it to be printed onto a canvas.

# Technologies Used 
* Google Fonts
* Adobe PhotoShop
* HTML 
* CSS
* VSCode
* Code Anywhere 
* Blackbox AI
* Github.com
* Git
* Font Awesome
* Am I Reponsive
* Jquery
* Javascript

# Manual testing 

## Manual Testing Table for Sign-Up Page

| Action                         | Predicted Outcome                               | Outcome |
|:-------------------------------|:-----------------------------------------------:|--------:|
| Enter valid email              | Form accepts email and allows further input     | works   |
| Enter invalid email            | Displays error or prevents form submission      | works   |
| Enter valid first name         | Form accepts the first name and allows further input | works |
| Leave first name field empty   | Displays error or prevents form submission      | works   |
| Enter matching passwords       | Form accepts passwords and allows form submission | works |
| Enter non-matching passwords   | Displays error indicating passwords do not match | works   |
| Click submit with valid inputs | Form submits successfully, redirects to next page or shows success message | works |
| Click submit with invalid inputs | Form does not submit, displays appropriate error messages | works |
| Check CSRF token inclusion     | Form includes a valid CSRF token                | works   |

## Manual Testing Table for Login Page

| Action                         | Predicted Outcome                               | Outcome |
|:-------------------------------|:-----------------------------------------------:|--------:|
| Enter valid email              | Form accepts email and allows further input     | works   |
| Enter invalid email            | Displays error or prevents form submission      | works   |
| Enter valid password           | Form accepts the password and allows form submission | works |
| Leave password field empty     | Displays error or prevents form submission      | works   |
| Click login with valid inputs  | Form submits successfully, redirects to dashboard or home page | works |
| Click login with invalid inputs| Form does not submit, displays appropriate error messages | works |
| Check CSRF token inclusion     | Form includes a valid CSRF token                | works   |

## Manual Testing Table for Profile Page

| Action                                      |                  Predicted Outcome                         |  Outcome  |
|:--------------------------------------------|:----------------------------------------------------------:|----------:|
| View Profile Page                           | User's first name and email are displayed correctly         | works     |
| Log in as Admin and view Profile Page       | "Go to Admin Panel" link is visible and functional          | works     |
| Log in as Non-Admin and view Profile Page   | "Go to Admin Panel" link is not visible                     | works     |
| Submit "Delete Profile" form                | Profile is deleted after confirmation prompt                | works     |
| Submit "Delete Profile" form without CSRF   | Form submission fails, CSRF token error is shown            | works     |
| Add a gig review with valid inputs          | Review is successfully added and displayed                  | works     |
| Add a gig review with empty fields          | Form displays error messages, does not submit               | works     |
| Add a gig to wishlist                       | Gig is added to the wishlist and appears in the list        | works     |
| Delete a gig from wishlist                  | Gig is removed from the wishlist                            | works     |
| Edit a gig in wishlist                      | Gig's details are updated and changes are reflected         | works     |
| Submit a wishlist form without CSRF         | Form submission fails, CSRF token error is shown            | works     |
| Attempt to delete a profile without confirmation | Profile is not deleted, stays intact                      | works     |

## Manual Testing Table for Home Page

| Action                                      |                  Predicted Outcome                         |  Outcome  |
|:--------------------------------------------|:----------------------------------------------------------:|----------:|
| View Home Page                              | Page displays a title, intro section, and content based on user status | works     |
| Visit page as unauthenticated user          | Login prompt with sign-up and sign-in options are displayed | works     |
| Visit page as authenticated user            | Login prompt is not visible; user sees gig reviews and posts | works     |
| Check blog post display                     | Blog posts are listed with title, content, author, and timestamp | works     |
| Attempt to edit a post as post owner        | Edit option is visible and functional for the post owner    | works     |
| Attempt to delete a post as post owner      | Delete option is visible and functional for the post owner  | works     |
| Attempt to edit/delete a post as non-owner  | Edit and Delete options are not visible for non-owners      | works     |
| Attempt to edit/delete a post as admin      | Edit and Delete options are visible and functional for admin | works     |
| Add a comment to a post                     | Comment is successfully added and displayed under the post  | works     |
| Delete own comment                          | Delete option is visible and comment is successfully removed | works     |
| Attempt to delete comment as non-owner      | Delete option is not visible for comments made by others    | works     |
| Submit any form without CSRF token          | Form submission fails, CSRF token error is shown            | works     |
| View post with comments                     | Comments are displayed with content, author, and timestamp  | works     |
| View post without comments                  | "No comments yet" message is displayed                      | works     |
| View page with no blog posts                | "No reviews available" message is displayed                 | works     |



## W3C Validation 
Managed to fix these few errors by finding the lines of code referenced on the page and removing the stray tags and correctly formating the code. Here are the results. 
![image](assets/docs/imgdocs/admin-dash.png)


![image](documents/valid-css.png "valid css") 


### Am I Responsive 
![image](assets/docs/imgdocs/responsive.png)

### Lighthouse Report 
![image](assets/docs/imgdocs/lighthouse.png)
Lighthouse report looks good on this.

# Challenges and Bugs
The only bugs I got were unclosed elements and stray tags. Some titles weren't formatted correctly which you can see here.
At first the webpage was not valid as seen by this screenshot here 
![image](assets/docs/imgdocs/jest-bug.png)
![image](assets/docs/imgdocs/Jest-bug-two.png)

I also ran into a script error which I managed to solve with some research.
![image](assets/docs/imgdocs/script-error.png)

![image](assets/docs/imgdocs/script-fix.png)

Here is also the invalid w3c html test ![image](assets/docs/imgdocs/w3c-valid-error.png)

Ran into a bug during media queries on CSS trying to make the start button show on below 320px but I couldn't figure out where I was going wrong.

I ran into another problem again on my Github, I had made a previous account called "Twinwinter" on my email address robertwinterburn@hotmail.co.uk and I had made a new account to make my name a bit more professional and readable (RWinterburn) but when I started making commits they came from "Twinwinter" on one and "RWinterburn" from another I don't know wether it was to do with me from switching from gitpod.io and codeanywhere to VScode need to figure this problem out for future developments as I haven't figured it out yet. So you will see commits from both of my Github accounts.

# Deployment and Development 

### Deployment 

To deploy the website the user must 
* Log in to Github.com.
* Go to "settings".
* Click "pages" under "codes and automation".
* Select "deploy from a branch" and select the "main" branch.
* Then select "/(root)" 
* Click "save" to save the Github page source.
* Go to "code".
* Click on the yellow circle on the page repository.
* You will see the backend working on building the website when this is complete go to "settings"
* Click "pages" 
* You should see the website link https://rwinterburn.github.io/project-3
* Click on the link and you will see the website.

### Development 
For future development go to https://github.com/RWinterburn/project-3
* Click the green "code" button.
* Copy the URL
* Go to your cloud based coding site. e.g. Code Anywhere or Gitpod.io
* click on "new workspace". 
* Paste in the repository URL
* Click create and it will create the code space for you.

#### VSCode Development
For future development go to https://github.com/RWinterburn/project-3
* Click the green "code" button.
* Copy the URL
* Open "command palette in VSCode (CTRL + SHIFT + P)
* Click the option "Git Clone"
* Click "clone from Github"
* Paste in the Repository URL 
* Hit "Enter"
* A window will pop up on your computer asking you to choose you repository destination, choose an appropriate folder. 
* Select the repository destination and the workspace will click open. 
* You may get the option saying "Do you trust this author? click Yes"

# Tutorials Used & external code implimented
Code has been partially used from these websites, most of the time when I first implimented it it wouldn't work as intended until I changed the parameters.
* W3Schools
* Stackoverflow
* YouTube: https://www.youtube.com/watch?v=dam0GPOAvVI
* Chat GPT











