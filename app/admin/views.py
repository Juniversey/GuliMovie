from functools import wraps

from flask import render_template, url_for, redirect, flash, session, request

from app.admin.forms import LoginForm
from app.admin import admin
from app.models import Admin


def admin_login_req(func):
    @wraps(func)
    def decorator_function(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return func(*args, **kwargs)

    return decorator_function


@admin.route('/')
@admin_login_req
def index():
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data['account']).first()
        if not admin.check_pwd(data['pwd']):
            flash('密码错误！')
            return redirect(url_for('admin.login'))
        session['admin'] = data['account']
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('admin/login.html', form=form)


@admin.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('admin.login'))


@admin.route('/tag_add')
@admin_login_req
def tag_add():
    return render_template('admin/tag_add.html')


@admin.route('/tag_list')
def tag_list():
    return render_template('admin/tag_list.html')


@admin.route('/movie_add')
def movie_add():
    return render_template('admin/movie_add.html')


@admin.route('/movie_list')
def movie_list():
    return render_template('admin/movie_list.html')


@admin.route('/preview_add')
def preview_add():
    return render_template('admin/preview_add.html')


@admin.route('/preview_list')
def preview_list():
    return render_template('admin/preview_list.html')


@admin.route('/user_list')
def user_list():
    return render_template('admin/user_list.html')


@admin.route('/comment_list')
def comment_list():
    return render_template('admin/comment_list.html')


@admin.route('/moviecol_list')
def moviecol_list():
    return render_template('admin/moviecol_list.html')


@admin.route('/oplog_list')
def oplog_list():
    return render_template('admin/oplog_list.html')


@admin.route('/adminloginlog_list')
def adminloginlog_list():
    return render_template('admin/adminloginlog_list.html')


@admin.route('/userloginlog_list')
def userloginlog_list():
    return render_template('admin/userloginlog_list.html')


@admin.route('/auth_add')
def auth_add():
    return render_template('admin/auth_add.html')


@admin.route('/auth_list')
def auth_list():
    return render_template('admin/auth_list.html')


@admin.route('/role_add')
def role_add():
    return render_template('admin/role_add.html')


@admin.route('/role_list')
def role_list():
    return render_template('admin/role_list.html')


@admin.route('/admin_add')
def admin_add():
    return render_template('admin/admin_add.html')


@admin.route('/admin_list')
def admin_list():
    return render_template('admin/admin_list.html')
