# Tasty Recipes

This is my DJANGO project for [Python Web](https://softuni.bg/modules/75/python-web) course at SoftUni.  

Website for recipes, products and cooking courses. It has custom user functionality, custom admin panel and custom permissions.

### CSS is optimized for 16:9 resolution (1920x1080).

## Home page

<img src="examples/home_page.jpg">

### Navigation bar and Footer
When user is not authenticated.

<img src="examples/nav_bar.jpg">
<img src="examples/footer.jpg">

When user is logged in.

<img src="examples/nav_bar_logged_user.jpg">
<img src="examples/footer_logged_user.jpg">


## Recipes
This is the main page of the site. It is public and the recipes can be seen by everyone.

The recipes can be filtered by a selected category.

<img src="examples/recipes_dashboard.gif">

In order to add a recipe, the user must be registered.  
A recipe can be edited or deleted via the 'Edit' and 'Delete' buttons.  
They are shown below the recipe's description area only when the current user is the author of that recipe.

After a recipe is deleted, the user is redirected to 'My recipes' page.

<img src="examples/recipe_add_edit_delete.gif">


## Profile
When an user is registered, a default profile picture is set and 'My Profile Page' label is shown.  
If the user updates First and Last name from the edit page, 'My Profile Page' is changed with profile's names.

<img src="examples/profile_signUp_edit_delete.gif">

### My Recipes
From this page, the user can see all the recipes that it's author of.  
If the user hasn't added any recipes, a 'Add recipe' button is shown.

<img src="examples/my_recipes.gif">

When the user deletes his profile, its recipes also gets deleted.



## Products
Public page with products.  
They can only be added, edited and deleted by users with 'Staff' status.

<img src="examples/products.gif">


## Cooking Courses
Public page with recomended cooking courses.  
They can only be added, edited and deleted by users with 'Staff' status.

Courses don't have own pages  with details like the recipes and the products.  
Instead, when they are clicked, the user is redirected to the course's link.

<img src="examples/courses.gif">


## Search
The input is searched in all 3 main_app models - 'Recipe', 'Product' and 'Course'.

<img src="examples/search.gif">


## Admin Panel

<img src="examples/admin_panel.gif">


## Errors 
404

<img src="examples/not_found.jpg">

403 and 500

<img src="examples/forbidden.jpg">
