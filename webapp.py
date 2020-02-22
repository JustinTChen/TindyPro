#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 18:58:10 2020

@author: JustinChen
"""
from flask import Flask
from flask import render_template, flash, redirect, url_for, session, jsonify, request
from TinderBot import TinderBot
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired
import os

root = r'./'
os.chdir(root)
#%%
app = Flask(__name__, template_folder='static')
app.config['SECRET_KEY'] = 'tindytindy'

class loginForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password')
    submit = SubmitField('Login')

@app.route('/')
@app.route('/home')
def home():
    form = loginForm()
    if form.validate_on_submit():
        session['user'] = form.user.data.lower()
        seesion['pass'] = form.password.data.lower()
        bot = TinderBot(session['user'], session['pass'])
        bot.login()
        return redirect(url_for('home'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
    