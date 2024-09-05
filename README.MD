

# Gig Reviews
Gig reviews is a website where users can post about their gigs they have been to and would like to leave a review about it on the page it is aimed towards musical people and who have a love for music. It also lets users comment on blog posts, add thier own blog posts and ive also added a gig wishlist feature for gigs they want to see in the future

# Rationale 
The "Gig Reviews" website is designed to create a vibrant and interactive community platform for music enthusiasts. It provides a space for users to share their experiences and opinions on recent gigs they have attended. The platform enhances user engagement through various features that support content creation, interaction, and community building.

## Key Features and Their Rationales

### User Authentication and Access Control

**Rationale:** 
Restricting certain actions, such as posting reviews, to authenticated users helps maintain a high quality of content and encourages genuine contributions. By requiring users to sign up and log in, the site ensures accountability and enhances security. This restriction helps prevent spam and misuse, providing a trustworthy environment for sharing reviews.

### Blog and Gig Review System

**Rationale:**
The core feature of the site is the ability for users to create, read, update, and delete (CRUD) their own blog posts about gigs. This system allows users to share their personal experiences, opinions, and ratings of the gigs they have attended. It fosters a community of music lovers who can connect over shared interests, creating a rich repository of reviews and discussions.

### Personalized Blog Post Management

**Rationale:**
Allowing users to edit and delete their own posts provides control over content and ensures that users can correct or remove information as needed. Admins have broader control to manage content, maintaining the site's cleanliness and appropriateness. This functionality supports user autonomy while also ensuring the integrity and quality of the content presented on the platform.

### Comment System

**Rationale:**
Enabling users to comment on blog posts enhances the platform's interactivity. It allows users to provide feedback, share additional thoughts, and engage in discussions, which contributes to a more engaging and dynamic community. This interaction helps build a sense of community and encourages active participation among users.

### Security Measures

**Rationale:**
Implementing CSRF protection and secure handling of user input (such as comments) is crucial for protecting the site from common web vulnerabilities and ensuring the integrity of user data. These security measures help prevent attacks and unauthorized access, safeguarding both user information and the overall stability of the site.

### Dynamic Content Display

**Rationale:**
Displaying user-generated content such as blog posts and comments dynamically ensures that the most recent and relevant information is visible to users. This feature keeps the content fresh and engaging, encouraging users to return and interact with new posts and comments.

### Administrative Functionality

**Rationale:**
Providing admin functionality for managing users, posts, and comments ensures oversight and control over the content and user interactions. This feature is important for maintaining the site's quality and integrity, allowing admins to address issues and enforce community standards effectively.


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

For the colour scheme I have gone with a fun pastel colour with all of the colours complimenting eachother and a simple design so users know what they're looking at as soon as they load the page.

# Data Schema Overview

The **Gig Reviews** website uses Flask and SQLAlchemy for database management. The data schema defines the structure of our database tables and their relationships. Below is a detailed description of each table and its relationships.

## Schema Breakdown

### User Table (`User` Class)

- **Table Name:** `users`
- **Columns:**
  - `id`: Unique identifier for each user (Primary Key).
  - `email`: User’s email address (must be unique).
  - `password`: User’s password.
  - `first_name`: User’s first name.
  - `is_admin`: Boolean flag to indicate if the user is an admin.
- **Relationships:**
  - `notes`: One-to-many relationship with the `Note` table (a user can have multiple notes).
  - `comments`: One-to-many relationship with the `Comment` table (a user can have multiple comments).
  - `blog_posts`: One-to-many relationship with the `BlogPost` table (a user can have multiple blog posts).

### Note Table (`Note` Class)

- **Table Name:** `notes`
- **Columns:**
  - `id`: Unique identifier for each note (Primary Key).
  - `data`: Content of the note.
  - `user_id`: Foreign Key linking to the `users` table.
  - `is_public`: Boolean flag to indicate if the note is public.

### BlogPost Table (`BlogPost` Class)

- **Table Name:** `blog_posts`
- **Columns:**
  - `id`: Unique identifier for each blog post (Primary Key).
  - `title`: Title of the blog post.
  - `content`: Content of the blog post.
  - `user_id`: Foreign Key linking to the `users` table.
  - `created_at`: Timestamp of when the blog post was created.
- **Relationships:**
  - `comments`: One-to-many relationship with the `Comment` table (a blog post can have multiple comments).

### Comment Table (`Comment` Class)

- **Table Name:** `comments`
- **Columns:**
  - `id`: Unique identifier for each comment (Primary Key).
  - `content`: Content of the comment.
  - `user_id`: Foreign Key linking to the `users` table.
  - `blog_post_id`: Foreign Key linking to the `blog_posts` table.
  - `created_at`: Timestamp of when the comment was created.

## Summary

- **Tables:** `users`, `notes`, `blog_posts`, `comments`
- **Primary Keys:** Unique identifiers for each table (`id` columns).
- **Foreign Keys:** Links between tables (e.g., `user_id` in `notes` and `comments`, `blog_post_id` in `comments`).
- **Relationships:**
  - **One-to-Many:** One `User` can have multiple `notes`, `comments`, and `blog_posts`.
  - **One-to-Many:** One `BlogPost` can have multiple `comments`.

This schema ensures that data is organized efficiently and relationships between different entities are properly maintained. It provides a clear structure for how data is stored and linked within the application.


 # WireFrames Desktop

 For the wireframes I didn't have a wireframe designer so I designed the app on Adobe Photoshop.
1. Wireframe for profile
![image](assets/docs/imagedocs/wireframe-profile.png)

2. Wireframe for mainpage
![image](assets/docs/imagedocs/wireframe-main-page.png)

# Features 

1. An admin dashboard for the admin to see the database
   ![image](assets/docs/imagedocs/admin-dash.png)
2. Blog form to submit a blog 
   ![image](assets/docs/imagedocs/feature-blog.png)
3. A nav bar so users can easily navigate the website
   ![image](assets/docs/imagedocs/feature-nav-bar.png)
4. Sign up form
   ![image](assets/docs/imagedocs/feature-sign-up.png)
5. login form
   ![image](assets/docs/imagedocs/login-feature.png)
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
* Jinja
* SQL
* Flask, admin, login and migrate and flaskSQLAlchemy
* Werkzueg
* WTForms

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


![image](assets/docs/imagedocs/edit-blog-post.png)

![image](assets/docs/imagedocs/edit-note.png)

![image](assets/docs/imagedocs/login.png)

![image](assets/docs/imagedocs/sign-up-valid.png)



### Lighthouse Report 
![image](assets/docs/imagedocs/lighthouse.png)
Lighthouse report.

# Challenges and Bugs

1. CRSF Token wasn't in the right line of code
![image](assets/docs/imagedocs/bug-docs/crsf-token.png)

2. Url endpoints ended up conflicting and throwing the app off until i changed the route
![image](assets/docs/imagedocs/bug-docs/end-point.png)
![image](assets/docs/imagedocs/bug-docs/end-points.png)

3. import bugs, resolved when I used captials correctly
![image](assets/docs/imagedocs/bug-docs/import-error.png)

4. added user id later in the database and it wasnt being reconigzed until I migrated the database
![image](assets/docs/imagedocs/bug-docs/no-user-id.png)

5. SQL wasn't installed properly 
![image](assets/docs/imagedocs/bug-docs/hadnt-installed-sql.png)

6. note wasn't imported at the top of the page.
![image](assets/docs/imagedocs/bug-docs/note-not-defined.png)
![alt text](assets/docs/imagedocs/bug-docs/note-not-defined-solution.png)

I had made a previous account called "Twinwinter" on my email address robertwinterburn@hotmail.co.uk and I had made a new account to make my name a bit more professional and readable (RWinterburn) but when I started making commits they came from "Twinwinter" on one and "RWinterburn" from another I don't know wether it was to do with me from switching from gitpod.io and codeanywhere to VScode need to figure this problem out for future developments as I haven't figured it out yet. So you will see commits from both of my Github accounts, dont think this has happened again. Resolved by git.

I did run into a problem I had to sign up for gitpod.io with my student account after I already had started my website so there will be a commit name saying "RWinterburn2" it is linked to my student email.

I tried signing up for Heroku so I had to find alternatives and it slowed my project to a halt for a few days finding a solution asked for an extended deadline on the project but I only managed to get a request form in at the last minute(Managed to fix heroku by starting new account unfortunately im getting charged at the minute though for add ons)



# Am I responsive 

![alt text](assets/docs/imagedocs/am-i-responsive.png) 
Am I Responsive test

# Deployment and Development 

### Heroku deployment 


* Login: Open your terminal and log in to Heroku: heroku login
* Create an App: heroku create gig-reviews 
* Deploy: git push heroku main 
* View: heroku open


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


### Deployment on Cloud Flare
Currently isn't working asked for an extension on deadline to resolve

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











