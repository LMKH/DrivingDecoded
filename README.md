# DrivingDecoded

## DrivingDecoded - Crack the Code. Pass the Test.

![homepage](readme-assets/images/readme-homepage.png)

## [View DrivingDecoded now on Heorku](https://driving-decoded-ef5da982f589.herokuapp.com/)

## Table of Contents

- [Introduction](#introduction)
- [User Experience](#user-experience)
- [UX Design](#ux-design)
- [Features](#features)
- [Tools Used](#tools-used)
- [Wireframes](#wireframes)
- [Agile Development](#agile-development)
- [Deployment](#deployment)
- [AI Augmentation](#ai-augmentation)
- [End Credits](#end-credits)

### Introduction

**DrivingDecoded** is a Django-based web application designed for people learning to drive. Users can create an account and log in to a personalised dashboard where they can document their learning journey. The site acts as a digital journal, allowing learners to:

- **Write new posts** about their driving experiences and progress.
- **View past entries** to track their improvement over time.
- **Maintain a personal learning diary** in an organised and easy-to-use interface.

#### Website Purpose

**DrivingDecoded** is designed to support learner drivers preparing for both their **theory and practical driving tests**. The website provides a simple, user-friendly space where learners can document how their lessons are going and reflect on their progress.

##### Target Audience

- **Learner drivers** preparing for their theory or practical driving tests.

- **New drivers** who want to stay motivated by seeing how far they've come over time.

- **Anyone wanting to keep clear learning notes in one place**.

The website is designed for learner drivers who want a straightforward, easy-to-use interface where they can record their thoughts, feelings, and experiences throughout their driving journey. It provides a calm, focused space for reflecting on lessons, tracking progress, and building confidence over time.

### User Experience

#### Verifications

Google Lighthouse was used to test the performance, accessibility, best practices, and SEO of the application.

The following pages were tested:

##### Lighthouse - Homepage

![lighthouse-homepage](readme-assets/images/lighthouse-homepage.png)

##### Lighthouse - Dash

![lighthouse-dash](readme-assets/images/lighthouse-dash.png)

##### Lighthouse - Journal Entry

![lighthouse-entry](readme-assets/images/lighthouse-entry.png)

All tested pages achieved a **full 100% score**, demonstrating strong performance, accessibility, and adherence to web best practices.

##### Manual Testing & Validation

Manual testing was carried out throughout development to ensure all features functioned as intended.

The following functionality was manually tested:

- User registration, login, and logout
- Restricted access to the dashboard for authenticated users only
- Creating, Reading, Updating, and Deleting (CRUD) journal entries
- Form validation and redirects after successful submission
- Navigation links and conditional navbar items
- Responsive layout across different screen sizes

All tested features behaved as expected.

#### User Stories

**MoSCoW Prioritisation**

**Must Have:** 

- Responsive UI/UX design. 
- Fully functional and working links. 
- User registration and login. 
- Clear, concise, and easy-to-understand interface.

**Should Have:** 

- Calming background colours and themes throughout.
- Notification of changes sent to the user.

**Could Have (Future Enhancements):** 

- Advanced search capabilities.
- Notifications for the user to see updates and/or reminders. I.e. time to revise.

**Won't Have:** 

- Overly complex or overwhelming content that could confuse users.

***First Time Visitor Goals***

-   **As a first-time visitor**, I want to be able to sign in or create an account quickly so I can start using the website without confusion.

-   **As a first-time visitor**, I want to immediately understand the purpose of the website so I can decide whether it supports my learning needs.

-   **As a first-time visitor**, I want a simple way to start documenting my driving journey.

***Returning Visitor Goals***

-   **As a returning visitor**, I want to easily access all my previous posts so I can reflect on past lessons and continue learning from my experiences.

-   **As a returning visitor**, I want access to trusted resources, such as official UK government websites for mock tests, so I can practice with accurate and reliable materials.

-   **As a returning visitor**, I want the ability to edit or update my past posts to keep my driving journal accurate and up to date.

***Frequent Visitor Goals***

-   **As a frequent visitor**, I want to quickly log new entries so I can keep my driving journal updated without any unnecessary steps.

-   **As a frequent visitor**, I want a clear, organised view of all my posts so I can quickly review specific lessons or experiences when needed.

-   **As a frequent visitor**, I want reliable access to learning resources so I can continue preparing for both theory and practical tests.

#### User Value

DrivingDecoded is designed to provide learner drivers with a simple, structured way to reflect on their driving lessons and track their progress over time.

**Key value to users includes:**

- Structured reflection:
    - Learner drivers can record lesson ratings, areas for improvement, and written reflections after each lesson, helping to reinforce learning and identify patterns over time.
- Progress tracking:
    - By reviewing previous journal entries, users can clearly see how their confidence and skills develop, providing motivation and reassurance throughout the learning process.
- Personalised experience:
    - Each user has a private dashboard where only their own entries are visible, creating a safe and focused space for reflection.
- Support beyond lessons:
    - The homepage provides quick access to trusted external resources, helping users continue learning outside of formal driving lessons.

### UX Design

#### Fonts

For simplicity, readability, and a uniform appearance across the application, the app uses the Arial sans serif font throughout. This choice ensures that text is easy to read on all devices and maintains a consistent style across pages.

#### Themes

The font colours are primarily black, with grey used occasionally for secondary text.

The background is white, ensuring strong contrast with the text for easy readability.

#### Logo

The **DrivingDecoded** logo was created using ***Canva AI***, allowing for a clean, sleek, distinctive design aligned with the website theme and brand. The image was then converted into favicon formats using ***Favicon.io*** to ensure clarity and consistency across browsers and devices, enhancing overall user recognition and experience.

***Full Website Logo***

![DrivingDecodedLogo](readme-assets/images/DrivingDecoded%20Logo.png)

***Favicon***

![DrivingDecodedFavicon](readme-assets/images/favicon.ico)

### Features

**Homepage**

- Welcoming landing page introducing DrivingDecoded
- Clear call-to-action buttons for registration and login
- Helpful external resources for learner drivers (e.g. DVSA, RAC)

![homepage-mobile](readme-assets/images/homepage-mobile.png)

**Journal Dashboard**

- Secure, user-only dashboard accessible after login
- Displays all journal entries created by the logged-in user
- Greets users by username for a personalised experience

![journaldash-mobile](readme-assets/images/journaldash-mobile.png)

**Journal Entries (CRUD)**

- Users can create new driving lesson journal entries
- Entries include:
    - Lesson rating
    - Areas for improvement
    - Written reflections
- Users can edit or delete previous entries
- Entries are ordered by most recent first

![journalentry-mobile](readme-assets/images/journalentry-mobile.png)

**User Authentication**

- Secure user registration and login
- Dashboard and journal entries are restricted to authenticated users
- Navigation options adapt based on login status

![userauth-mobile](readme-assets/images/userauth-mobile.png)

**Responsive Design**

- Mobile-first layout using Bootstrap
- Cards and content adapted to smaller screens
- Dashboard and homepage remain usable across devices

### Tools Used

#### Applications and Tools Used

- **VS Code** - Primary development environment.
- **Git & GitHub** - Used for version control, deployment, and documentation.
- **Heroku** - Used for hosting and deploying the site, providing a simple and reliable deployment workflow.
- **ChatGPT** - Used for learning support, including concept clarification and guidance when encountering challenges.
- **Canva AI** - Designed the project's steering-wheel logo.
- **Favicon.io** - Converted the logo into a full favicon set for browser compatibility.
- **Miro** - Used for creating the Entity Relationship Diagram (ERD).

#### Languages Used

- **Python** - Backend logic and server-side programming.
- **HTML5** - Structuring the web pages.
- **JavaScript** - Frontend interactivity and webpage responsiveness.

#### Libraries and Frameworks

- **Django** - Python web framework for backend development.
- **PostgreSQL** - Relational database used for storing and managing user data.
- **Bootstrap CSS** - CSS framework for responsive and mobile-first design.

### Wireframes

***Welcome Page Wireframe***

Below is the wireframe for the **welcome landing page**, which is the first screen users see when they visit the site.

At the top of the page, there is a welcome message which is the company moto.

Underneath the welcome message is the login section, which includes: 

- A clearly labelled **username input field** with a placeholder that reads 'Username'.
- A **password input field**, also with a placeholder reading 'Password'.
- A **'Remember Me'** checkbox that allows users to stay logged in on the device if desired.
- A **Login** button beneath the form fields.

Below the Login title there is a small line of text for new users: '**New Member? Sign Up'**, which will link to the registration page.

The layout is designed to be simple, accessible, and easy to navigate, allowing returning users to log in quickly and guiding new users to create an account.

![welcome-page-wireframe](readme-assets/images/Welcome-page-wireframe.png)

***Dashboard Wireframe***

The dashboard page displays all the journal entries belonging to the logged-in user. At the top of the page, the heading 'Your Entries' appears, with action buttons aligned to the right:
- **Edit Post**
- **Delete Post**
- **New Post**

The layout will adapt to the screen size used:
- **Large Desktop Screens**: Entries are displayed on a 3-column grid.
- **Tablet Screens**: The layout reduces to a 2-column grid.
- **Mobile Screens**: Entries are shown in a single-column layout for readability.

Additionally, on small screens (tablet and below), the three action buttons collapse so that the **New Post** button remains primary, and the **Edit** and **Delete** options are placed inside a dropdown menu to conserve space and improve usability.

![dashboard-wireframe](readme-assets/images/dashboard-wireframe.png)

***Journal Entry Wireframe***

Below is the wireframe for the **Journal Entry** page. This page allows users to create or update their driving-lesson journal entry in a simple and structured way. 

The design includes **two dropdown selectors**:
- **Lesson Rating** - allows the user to choose from a set of predefined options describing how well the lesson went (e.g. Well, Fair, Bad, etc.)
- **Room for Improvement** - displays a list of common areas the user may need to work on (e.g. Steering, Breaking, Attention to Roads, etc.)

Below the dropdowns is a **large text area**, where users can freely write their journal reflection for that lesson.

At the bottom of the page, the wireframe includes **three action buttons**: **Edit, Delete,** and **Save**.

This wireframe outlines the core user-interaction elements for creating and managing journal entries within the app.

![journal-entry-wireframe](readme-assets/images/journal-entry-wireframe.png)

***Entity Relationship Diagram (ERD)***

For this project, I planned the database structure carefully to support the online journal functionality. The database consists of **two main tables**:

1. User - stores authentication data for each user (username, email, password hash, etc.)

2. Journal Entry - stores all journal entries, linked to a specific user. Each entry includes:

    - lesson_rating - how the driving lesson went, chosen from a dropdown. User can pick from a selection of options such as "Fair", "Good", "Poor" etc. 
    - improvement_area - what the user needs to improve, chosen from a dropdown. User can pick from a selection of options such as "Attention", "Steering", "Breaking" etc.
    - notes - this is the text field for the user to create free-form reflections of their learning journey.
    - Timestamps for **created_at** and **updated_at**.

![drivingdecoded-erd-table](readme-assets/images/DrivingDecoded%20ERD%20Table.png)

I used **Miro** to create the board and organise the tables visually. I reviewed online examples and ChatGPT suggestions to make sure the tables included all necessary fields and that the data types were appropriate. For dropdowns like lesson ratings and improvement areas, I chose CharFields with predefined choices, which ensures that only valid options are stored.

### Agile Development

Throughout development, I followed an **agile approach** to building the application:

- After each push to GitHub or any set of changes, I reflected on how my progress toward completion had evolved.
- I adapted future development steps based on these reflections, ensuring that each iteration aligned with the current state of the project.
- New ideas were incorporated as they arose, and plans that no longer fit the project's direction were revised or removed.
- This iterative process allowed the project to remain flexible, responsive, and focused on producing a functional, user-friendly application. 

### Deployment

## [View DrivingDecoded now on Heorku](https://driving-decoded-ef5da982f589.herokuapp.com/)

This project is deployed on Heroku. The Heroku app is connected to this GitHub repository and automatically deploys from the main branch.

#### To GitHub

1. Created a new GitHub repository.
2. Initialised git in the local project folder.
3. Added the remote repository and push the code.

The GitHub repository stores the source code and is connected to Heroku for deployment.

#### To Heroku

1. Log in to Heroku and create a new app.
2. In the Heroku dashboard, go to deploy.
3. Select GitHub as the deployment method.
4. Connect the app to the GitHub repository.
5. I usually select manual deploy from the main branch, however you can select automatic deploys.

### AI Augmentation

**AIs used in creating this project**:

- ChatGPT
- Canva AI

**ChatGPT** was used as a learning and support tool throughout the development of this project. This was my first Django application, and AI assistance was used to help understand core concepts and best practices rather than generate a finished solution.

ChatGPT was used to support:

- Understanding Django project and app structure, including: 
    - Views, models, templates, URLs, and forms
    - How data flows between the database, views, and templates
- Guidance on implementing **CRUD functionality** for journal entries:
    - Creating new entries via forms
    - Displaying user-specific data on a dashboard
    - Editing and deleting entries securely
    - Redirecting users appropriately after actions
- Help with authentication-aware UI logic, such as:
    - Showing dashboard links only when a user is logged in
    - Displaying the logged-in user's username dynamically
    - Restricting access to user-specific content
- Assistance with Bootstrap-based layout and responsiveness, including:
    - Structuring mobile-friendly layouts
    - Using cards, buttons, and grid systems
    - Improving spacing and visual hierarchy on the homepage and dashboard
- Debugging common beginner issues, such as:
    - Template inheritance errors
    - URL reversing (i.e. NoReverseMatch)
    - View and template connection issues
    - Understanding error messages

The **DrivingDecoded** logo was created using ***Canva AI***, allowing for a clean, sleek, distinctive design aligned with the website theme and brand.

All code was written, tested, and integrated by myself, with ChatGPT acting as a guided support and learning aid throughout the build process.

### End Credits

Created by Liam Kavanagh 2025

#### Acknowledgements

- The user authentication system (login, registration, and navigation bar) was **implemented** by following along with the official bootcamp-provided tutorial videos.
- This foundation was then extended and adapted to support the custom journal dashboard and CRUD functionality used in this project.