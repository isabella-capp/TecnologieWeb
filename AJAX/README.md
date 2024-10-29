# Ajax Exercises

Here there are the exercises proposed by the professor during the lab on Ajax that introduce how to load data and manage form submissions. Each exercise includes instructions for using asynchronous requests and dynamically updating the DOM based on server responses.

## Exercise 1 – Loading Posts via Ajax

In this exercise, you will load posts from a server and display them in the browser.

### Instructions

1. In `index.html`, there is a button.
2. Define a callback function for the button’s "click" event to:
   - Make an Ajax request to `https://jsonplaceholder.typicode.com/posts` to retrieve posts.
   - For each retrieved post, create a `<div>` with the class "post" and insert it into the `<div>` with the ID `postContainer`.

## Exercise 2 – Ajax and Form Submission

This exercise involves submitting a registration form using Ajax and handling the server’s response to display feedback to the user.

### Instructions

1. In `index.html`, there is a registration form.
2. In `script.js`, define a callback function for the form’s "onSubmit" event to:
   - Send the entered data via Ajax to `https://httpbin.org/post`.
   - Interact with the DOM based on the server’s response:
     - **On success**: Display the message "User «username» created" in the form (retrieve the username from the server response).
     - **On error**: Display an error message in the form.

---

These exercises focus on using Ajax to manage dynamic content and form interactions, providing a foundation for building responsive web applications.
