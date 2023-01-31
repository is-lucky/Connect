from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import About
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        about = request.form.get('about')

        if len(about) < 1:
            flash('Nothing written!', category='error')
        else:
            new_about = About(data=about, user_id=current_user.id)
            db.session.add(new_about)
            db.session.commit()
            flash('New inputs added!', category='success')

    return render_template("profile.html", user=current_user)