from flask import Flask,redirect,render_template,request 
import sqlite3
app=Flask(__name__,template_folder="./template")

@app.route("/",methods=["POST","GET"])
def main():
     if request.method=='POST':
         return redirect('/home')
     return render_template("main.html")


@app.route("/home",methods=['POST','GET'])
def home():
    if request.method=="POST":
        title=request.form["title"]
        story=request.form["story"]
        conn=sqlite3.connect("base.sqlite3")
        c=conn.cursor()
        c.execute("INSERT INTO blog (title,story) values(?,?)",(title,story))
        conn.commit()
        conn.close()
        return redirect("/story")                                                               
    return render_template("home.html")


@app.route("/story",methods=["POST","GET"])
def story():
    conn=sqlite3.connect("base.sqlite3")
    c=conn.cursor()
    c.execute("select * from blog")
    blog=c.fetchall()
    print(blog)
    return render_template("story.html",blogs=blog)



@app.route("/stories",methods=["POST","GET"])
def stories():
    conn=sqlite3.connect("base.sqlite3")
    c=conn.cursor()
    c.execute("select * from blog")
    blog=c.fetchall()
    print(blog)
    return render_template("stories.html",blogs=blog)


@app.route("/update-story", methods=["POST"])
def update_story():
    blog_id = request.form["blog_id"]
    title = request.form["title"]
    story = request.form["story"]

    conn = sqlite3.connect("base.sqlite3")
    c = conn.cursor()
    c.execute("UPDATE blog SET title = ?, story = ? WHERE id = ?", (title, story, blog_id))
    conn.commit()
    conn.close()

if __name__==("__main__"):
    app.run(debug=True)

    