from itsdangerous import URLSafeTimedSerializer

s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

def generate_reset_token(email):
    return s.dumps(email, salt='reset-password')

def verify_reset_token(token, max_age=3600):
    try:
        email = s.loads(token, salt='reset-password', max_age=max_age)
    except SignatureExpired:
        return None
    return email