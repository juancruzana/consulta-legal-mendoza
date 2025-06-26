from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models.users import User
from app.auth.forms import LoginForm, RegisterForm
from app import db
import logging

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        try:
            # CONSULTA A LA BASE DE DATOS
            user = User.query.filter_by(email=form.email.data).first()
            
            if user and user.check_password(form.password.data):
                login_user(user, remember=True)
                flash('Inicio de sesión exitoso', 'success')
                
                # Redirección después del login
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
            else:
                flash('Email o contraseña incorrectos', 'error')
                
        except Exception as e:
            logging.error(f"Error en login: {e}")
            flash('Error interno del servidor', 'error')
    
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = RegisterForm()
    
    if form.validate_on_submit():
        try:
            # CREAR NUEVO USUARIO EN LA BASE DE DATOS
            user = User(
                username=form.username.data,
                email=form.email.data.lower()
            )
            user.set_password(form.password.data)
            
            # GUARDAR EN LA BASE DE DATOS
            db.session.add(user)
            db.session.commit()
            
            flash('Registro exitoso. Ya puedes iniciar sesión', 'success')
            return redirect(url_for('auth.login'))
            
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error en registro: {e}")
            flash('Error al crear la cuenta. Intenta nuevamente', 'error')
    
    return render_template('auth/register.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada exitosamente', 'info')
    return redirect(url_for('main.index'))


