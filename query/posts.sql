-- get the last 10 post by date
select * from post order by add_date desc limit 10;

-- get the last 10 post by date and get author referencen name
select
	post.id, post.title, post.content, post.add_date,
    post.last_edit, post.tag, user.username as author
from post
inner join user on post.author_id = user.id
order by add_date desc limit 10;

-- count all posts
SELECT COUNT(*) FROM post;