import os
import json
import mysql.connector
from flask import Flask, request

conn = mysql.connector.connect(
  user=os.environ['DB_USERNAME'],
  password=os.environ['DB_PASSWORD'],
  host=os.environ['DB_CONN_HOSTNAME'],
  port=os.environ['DB_CONN_PORT'],
  database=os.environ['DB_NAME']
)

cursor = conn.cursor(dictionary=True)
cursor2 = conn.cursor()

POST_PER_PAGE = 10

app = Flask(__name__)
@app.route("/api/blog/post")
def get_posts():  
  params = request.args
  page = int(params['page']) or 1

  limit = f'{(page - 1) * POST_PER_PAGE}, {(page*POST_PER_PAGE) - 1}'
  is_get_content = ', post.content' if bool(params['page']) == True else ''
  
  query = f"""
    select
      post.id, post.title{is_get_content}, post.add_date,
      post.last_edit, post.tag, user.username as author
    from post
    inner join user on post.author_id = user.id
    order by add_date desc limit {limit};
  """

  cursor.execute(query)
  posts = []
  for post in cursor:
    if post['tag'] is not None:
      post['tag'] = json.loads(post['tag'])
    posts.append(post)

  # TODO: Give pagination info for client
  
  return { 'posts': posts }

if __name__ == '__main__':
  app.run()
  conn.close()
  print('conn.closed')
