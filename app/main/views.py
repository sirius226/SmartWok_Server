from flask import render_template, redirect, url_for, abort, flash, request,\
     current_app
from flask.ext.login import login_required, current_user
from . import main
from .forms import EditProfileForm, EditProfileAdminForm
from .. import db
from ..models import Role, User, Dish
from ..decorators import admin_required


@main.route('/')
def index():
    return redirect(url_for('.featured'))

@main.route('/featured')
def featured():
    feature = Dish.query.order_by(Dish.count_rev.desc()).limit(8)
    return render_template('featured.html', feature=feature)

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@main.route('/cooking')
def cooking():
    flash('Your recipe is transimitting to your wok!')
    return render_template('cooking.html')

@main.route('/rating')
def rating():
    flash('You can rate the dish here!')
    return render_template('rating.html')
    
@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        flash('The profile has been updated.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)

@main.route('/shopping')
def shopping():
    page = request.args.get('page', 1, type=int)
    pagination = Dish.query.order_by(Dish.id).paginate(
    page, per_page=current_app.config['SMARTWOK_DISH_PER_PAGE'],
    error_out=False)
    dishes = pagination.items
    return render_template('shopping.html', dishes = dishes, pagination=pagination)

@main.route('/createarecipe')
def createarecipe():
    return render_template('createarecipe.html')

@main.route('/dish/<dish_id>')
def dish(dish_id):
    dish = Dish.query.filter_by(id=dish_id).first_or_404()
    return render_template('dish.html', dish=dish)




