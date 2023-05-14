import random


from flask import Flask, render_template, request
import requests
all_post=[]

app=Flask(__name__)

def sentMail(msg):
    import smtplib
    email="your.ex.daddy8@gmail.com"
    password="lpgfzommjqmtjlda"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="mamunurrashid.s.bd@gmail.com",
            msg=f"Subject: Feedback from Bloging site\n\n {msg}"

        )
    print("sent mail")

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

@app.route('/contact', methods=["POST"])
def receive_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phn = request.form['phn']
        msg = request.form['msg']

        body=f"Name:{name}\n" \
             f"Email: {email}\n" \
             f"Cell: {phn}\n" \
             f"Message: {msg}\n"
        sentMail(body)

    return render_template('form-entry.html',msg="Msg sent successfuly")
        
    
    


if __name__ == "__main__":

    app.run(debug=True, use_reloader=True)