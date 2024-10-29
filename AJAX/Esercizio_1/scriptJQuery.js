$('#button').on('click', function() {
    $.ajax({
        url: 'https://jsonplaceholder.typicode.com/posts',
        type: 'GET',
        contentType: 'application/json',
        success: function(response) {
            $('#postsContainer').html('');

            var posts = response;
            for (var post of posts) {
                console.log(post);
                const $newDiv = $('<div>');
                $newDiv.addClass('post');
                $newDiv.html('<h3>Post ' + post.id + ': ' + post.title + '</h3><p>' + post.body + '</p>');

                $('#postsContainer').append($newDiv);
            }
        },
    });
});
