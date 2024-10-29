var button = document.getElementById('button');

button.onclick = function (){
    //1. Create a new object XMLHttpRequest
    var xhr = new XMLHttpRequest();
    
    // 2. Specify the request type in the endpoint URL 'https://jsonplaceholder.typicode.com/posts'
    xhr.open('GET', 'https://jsonplaceholder.typicode.com/posts', true);
    
    // 3. Define what to do on change of request state
    xhr.onreadystatechange = function() {
        //4. verifico che la richiesta sia terminata con successo
        if (xhr.readyState === 4 && xhr.status === 200) {
            
            //5. Parse JSON content of the request
            var response = JSON.parse(xhr.responseText);
            
            // 6. Print the first post on the console
            console.log(response);
            
            // 7. Select the post container from the DOM
            var Container = document.getElementById('postsContainer');
            Container.innerHTML = ' ';
            
            // 8. Iterate over the posts to create the visualization
            for(post of response){
                // 9. Create a div for each post
                var postDiv = document.createElement('div');
                
                // 10. Create HTML content for each post with concatenated strings
                postDiv.innerHTML = "<h3>Post " + post.id + ": " + post.title + "</h3>" + "<p>" + post.body + "</p>";
                postDiv.className = 'post';

                // 11. Append the post to the postContainer
                Container.appendChild(postDiv);
            }
            
        }
    }

   
    // 12. Send the request to the server
    xhr.send();
}