from flask_mail import Mail, Message

mail = Mail(app)

def send_reset_password_email(email, token):
    reset_url = url_for('reset_password_with_token', token=token, _external=True)
    msg = Message('Reset Your Password',
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[email])
    msg.body = f'Click the following link to reset your password: {reset_url}'
    mail.send(msg)