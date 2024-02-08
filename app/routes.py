from app import app, db
from flask import redirect, render_template, request, url_for, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app.forms.form_login import LoginForm

from app.models.contact import Contact
from app.models.post import Post
from app.models.comment import Comment

from app.forms.form_contact import ContactForm
from app.forms.form_register import UserForm
from app.forms.form_post import PostForm


# rotas de user
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.login()
        login_user(user, remember=True)
        return redirect(url_for("index"))

    return render_template("system/login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserForm()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for("index"))

    return render_template("user/register.html", form=form)


@app.route("/")
def index():
    return render_template("index.html")


# rotas de contato
@app.route("/contact", methods=["GET", "POST"])
@login_required
def contact():
    form = ContactForm()
    if request.method == "POST":
        if form.validate_on_submit():
            form.save()
            return redirect(url_for("index"))

    return render_template("contact/contact.html", form=form)


@app.route("/contact/getList", methods=["GET", "POST"])
@login_required
def getList():
    search = ""
    if request.method == "GET":
        search = request.args.get("search", "")

    dados = Contact.query.order_by()

    if search != "":
        dados = dados.filter_by(name=search)

    list = dados.all()

    for item in list:
        if item.answered == 1:
            item.answered = "Sim"
        else:
            item.answered = "Não"

    return render_template("contact/contact-list.html", list=list)


@app.route("/contact/<int:id>", methods=["GET", "POST"])
@login_required
def getContact(id):
    contact = Contact.query.get(id)

    if contact is not None:
        if contact.answered == 1:
            contact.answered = "Sim"
        else:
            contact.answered = "Não"

    return render_template("contact/contact-detail.html", contact=contact)


# contact utilizando form do html (não recomendado)
@app.route("/contact-old", methods=["GET", "POST"])
@login_required
def contact_old():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        contact = Contact(name=name, email=email, subject=subject, message=message)

        db.session.add(contact)
        db.session.commit()

    return render_template("contact/contact-old.html")


# rotas de post
@app.route("/post", methods=["GET", "POST"])
@login_required
def get_posts():
    posts = Post.query.all()
    for post in posts:
        post.created_formatted = post.get_created_formatted()

    return render_template("post/post-list.html", posts=posts)


@app.route("/post/add", methods=["GET", "POST"])
@login_required
def add_post():
    form = PostForm()
    if request.method == "POST":
        if form.validate_on_submit():
            form.save(current_user.id)
            return redirect(url_for("index"))

    return render_template("post/post.html", form=form)


@app.route("/post/<int:id>", methods=["GET", "POST"])
@login_required
def get_post(id):
    post = Post.query.get(id)
    print(post)
    return render_template("post/post-detail.html", post=post)


# rotas comentários
@app.route("/comment/add", methods=["GET", "POST"])
@login_required
def add_comment():
    data = request.get_json()
    user_id = data.get("user_id")
    post_id = data.get("post_id")
    text = data.get("text")

    if request.method == "POST":
        comment = Comment(user_id=user_id, post_id=post_id, text=text)
        if comment.save(user_id, post_id, text):
            return jsonify(
                {"success": True, "message": "Comentário recebido com sucesso!"}
            )

    return jsonify({"error": True, "message": "Comentário não pode ser salvo."})
