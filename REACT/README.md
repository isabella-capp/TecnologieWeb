# React Exercises Overview

This document provides an explanation of the React exercises proposed during the Web Technologies course. The exercises cover fundamental React concepts, such as components, state management, routing, and integration with Flask for API communication. Below are the exercises with their detailed descriptions.

[Download the exercises](../mnt/data/08.React.zip)

The downloadable zip file contains partial code provided during class. Each exercise required completing the missing parts to achieve full functionality as described.

## Exercise 1: Image Gallery

### Objective
Create an image gallery using two React components:

### Tasks
1. **ImageComponent**: 
   - Inputs: 
     - An image URL
     - A description
   - Functionality: Renders the image and its description within a `div`.

2. **Gallery**:
   - Inputs: 
     - A list of images
   - Functionality:
     - Creates an `ImageComponent` for each image in the list.
     - Contains a button to add a new image.

### Implementation Details
- Use **class-based React components**.
- Bind event-handling methods properly.
- Use **component state** to track loaded images.

### Follow-up Task
- Convert class-based components to **functional components**:
  - Eliminate the use of component state.
  - Use **props** to manage image data.
  - Avoid using `setState`. Manually re-render the `Gallery` component when adding new images.

## Exercise 2: Dynamic Routing

### Objective
Transform the provided website into a single-page application (SPA) using React.

### Tasks
1. Convert each page into a React component.
2. Implement **dynamic routing** to navigate between components.
3. Replace existing navigation links with a top navigation menu.

### Important Notes
- Avoid using JSX for rendering components.
- Integrate React with Flask without relying on Node.js.
- In real-world scenarios, React is typically used with Node.js, but this example is for educational purposes.

## Exercise 3: Flask API + React

### Objective
Transform pages to interact with Flask APIs using React components and AJAX.

### Tasks
1. **Team Page**:
   - Create a React component that fetches team data from a Flask API endpoint (`api/team`).
   - Render the team information dynamically.

2. **Books Page**:
   - Create a React component connected to the `api/books` endpoint.
   - Fetch and display a list of books.
   - Add functionality to insert a new book and send it to the API via the same endpoint.

---

These exercises provide foundational skills for integrating React with a Flask backend, building dynamic SPAs, and managing state and routing effectively. They also illustrate React’s versatility, even when working without advanced toolchains like Node.js or modern bundlers.

