import random


from flask import Flask,render_template
import requests
all_post=[]

app=Flask(__name__)


@app.route('/')
@app.route('/index/')
def home():
    global all_post
    post_url="https://api.npoint.io/7376a33db249acb36f5d"
    response = requests.get(post_url)
    print(response)

    all_post = response.json()
    return render_template('index.html',posts=all_post)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    global all_post
    req_post=None
    for blog_post in all_post:
       if blog_post["id"]==post_id:
            req_post=blog_post
            print(f"ID:{post_id}------> {req_post['title']}")


    return render_template('post.html', posts=req_post)
            
        
    
    


if __name__ == "__main__":

    app.run(debug=True, use_reloader=True)