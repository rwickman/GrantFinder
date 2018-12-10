# Individual Assignment Specifications

- Team: GrantFinder
- Iteration: 2

## Special Roles

- Project Coordinator: Ryan (Team Member Name)
- Quality Assurance Czars:
  - Adam
  - Mac (Team Member Name)
- Video Demo Creators:
  - xxx, 999 (Team Member Name, Number of Points; filled in at end of iteration)
  - xxx, 999 (Team Member Name, Number of Points; filled in at end of iteration)
- Demo-Booth Operator: Chris (Team Member Name; filled in at end of iteration)

## Tasks: Mac (Team Member Name)

### Task: Results Sorting(Task Name)
- Description: Sort results descending by cosine value(Task Description)
- How to Evaluate: Cosine value should be shown in the results page after a search, and should be sorted such that the highest cosine value is listed first. (Instructions)
- Outcome of Task: xxx (Description; filled in at end of iteration)
- Issue: xxx (Issue Number; filled in at end of iteration)
- Pull Request: xxx (Pull Request Number; filled in at end of iteration)

### Task: Enhance Results List navigation (Task Name)
- Description: Add page numbers, total number of results, firstpage, lastpage, and results per page to results page (Task Description)
- How to Evaluate: If the above fields are preset, this should be completed. Some less important features may not make through, such as results per page. (Instructions)
- Outcome of Task: xxx (Description; filled in at end of iteration)
- Issue: xxx (Issue Number; filled in at end of iteration)
- Pull Request: xxx (Pull Request Number; filled in at end of iteration)

### Task: Integrate “Favoriting” into results page. (Task Name)
- Description: Users should be able to favorite a result from the search page, and favorited listings should be indicated by highlight or star. (Task Description)
- How to Evaluate: xxx (Instructions)
- Outcome of Task: xxx (Description; filled in at end of iteration)
- Issue: xxx (Issue Number; filled in at end of iteration)
- Pull Request: xxx (Pull Request Number; filled in at end of iteration)


## Tasks: Ryan (Team Member Name)

### Task: LSA (Task Name)
- Description: Need to perform LSA on the generated term vectors (Task Description)
- How to Evaluate: It will be able to correctly compute the LSA matrix when through each grant’s term vector (Instructions)
- Outcome of Task: xxx (Description; filled in at end of iteration)
- Issue: xxx (Issue Number; filled in at end of iteration)
- Pull Request: xxx (Pull Request Number; filled in at end of iteration)


### Task: Compute Cosine Similarity and connect to search (Task Name)
- Description: For each grant, compute the cosine similarity between itself and the keyword vector entered by the user. Then return the grants who's similarity returns a value the exceeds a heuristic threshold. (Task Description)
- How to Evaluate: As long as the results page will receive these computed values, the search engine should work (Instructions)
- Outcome of Task: xxx (Description; filled in at end of iteration)
- Issue: xxx (Issue Number; filled in at end of iteration)
- Pull Request: xxx (Pull Request Number; filled in at end of iteration)


## Tasks: Chris (Team Member Name)

### Task: User Profiles (Task Name)
- Description: I will add user login features. Users will be able to register and login with a username and password. (Task Description)
- How to Evaluate: Users should be able to create a personal profile, using their email address for their username.(Instructions)
- Outcome of Task: xxx (Description; filled in at end of iteration)
- Issue: xxx (Issue Number; filled in at end of iteration)
- Pull Request: xxx (Pull Request Number; filled in at end of iteration)

### Task: Back Button (Task Name)
- Description: Add a backlink from the show page to the results page. (Task Description)
- How to Evaluate: Users should be able navigate from the show page to the results page without using web browsers back button.(Instructions)
- Outcome of Task: xxx (Description; filled in at end of iteration)
- Issue: xxx (Issue Number; filled in at end of iteration)
- Pull Request: xxx (Pull Request Number; filled in at end of iteration)


## Tasks: Adam

### Task: Fix Connection between Search Bar and Results Page
- Description: I need to use the newly created LSA function to have the search bar create a cosine for the term entered, and then send this information to the Results page, having the results to be limited to only cosine factors above 0.21.
- How to Evaluate: To evaluate, simply enter a term into the search bar and hit search. The results page that then follows should list Grants that contain the term entered. Make sure to take note of the cosine values of each one, as they should be listed from greatest to least, and there should be no cosine value smaller than 0.21.
- Outcome of Task: xxx (Description; filled in at end of iteration
- Issue: xxx (Issue Number; filled in at end of iteration)
- Pull Request: xxx (Pull Request Number; filled in at end of iteration)

### Task: Create a NavBar at the Top of the Views
- Description: I will need to add a Navigation Bar to the top of all of our pages, so that there is ease in travelling from page to page, as well as ease in logging in. The bar will also have a search bar within it.
- How to Evaluate: To evaluate, simply look to the top of any page and see if there is a bar there. Simple task, but the real evaluation comes from seeing if the bar allows the user to move between the pages. Also make sure you can get to the login screen from the bar. Lastly, use the Search Bar within the NavBar. If everything works, then the task has been completed correctly.
- Outcome of Task: xxx (Description; filled in at end of iteration)
- Issue: xxx (Issue Number; filled in at end of iteration)
- Pull Request: xxx (Pull Request Number; filled in at end of iteration)

### Task: Make Search Page UI
- Description: I need to make the UI for the search page more pleasing to the eye. This is not detrimental to the program’s performance, but it is indicative of a better application overall. I will make the page look more colorful and add a logo for the application.
- How to Evaluate: Look at the search page, if it shows signs that it has been made aesthetically pleasing, with a logo above the search bar, then this task has been completed correctly.
- Outcome of Task: xxx (Description; filled in at end of iteration)
- Issue: xxx (Issue Number; filled in at end of iteration)
- Pull Request: xxx (Pull Request Number; filled in at end of iteration)