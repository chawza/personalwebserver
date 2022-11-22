use blog;

 -- User Creation  
 CREATE TABLE user (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    username CHAR(255) NOT NULL
);

INSERT INTO user(username) values ('budi');

select id from user;
 
 -- Table cration
CREATE TABLE post (
	id BIGINT AUTO_INCREMENT,
	title CHAR(255) NOT NULL,
	author_id BIGINT NOT NULL,
    content LONGTEXT NOT NULL,
    add_date DATETIME DEFAULT CURRENT_TIMESTAMP(),
    last_edit DATETIME DEFAULT CURRENT_TIMESTAMP(),
    tag JSON,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES blog.user(id)
);

describe blog.post;

insert into post (title, author_id, content) values(
	'first post', 1, '#My first post\nA paragraph'
);

insert into post (title, author_id, content, tag) values(
	'second post', 1, '#My first post\nA paragraph', '["programming"]'
);

select * from post;