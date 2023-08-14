from flask_app import app
from flask import Flask, request, render_template, redirect, session, flash
from flask_app.models.models_cookie import Cookie



@app.route('/')
def index():
    cookies = Cookie.get_all()
    print(cookies)
    return render_template('dashboard.html', cookies = cookies)

@app.route('/new_order')
def new_order():
    return render_template('create.html')

@app.route('/create_order', methods=["POST"])
def create_order():
    if not Cookie.order_validator(request.form):
        return redirect('/new_order')
    data = {
        "name" : request.form["name"],
        "cookie_type" : request.form["cookie_type"],
        "number_of_boxes" : request.form["number_of_boxes"]
    }
    Cookie.create(data)
    return redirect('/')

@app.route('/edit/<int:cookie_id>')
def edit_cookie(cookie_id):
    data = {
        'id' : cookie_id
    }
    cookie = Cookie.get_one(data)
    return render_template('edit.html', cookie = cookie)

@app.route("/update/<int:cookie_id>", methods=["POST"])
def update_cookie(cookie_id):
    if not Cookie.edit_validator(request.form):
        return redirect('/edit/4')
    Cookie.update(request.form, cookie_id)
    return redirect('/')



