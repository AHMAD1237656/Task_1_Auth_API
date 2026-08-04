from itsdangerous import URLSafeTimedSerializer
from django.conf import settings

serializer = URLSafeTimedSerializer(settings.SECRET_KEY)


def generate_reset_token(email):
    return serializer.dumps(email)


def verify_reset_token(token, max_age=600):
    try:
        return serializer.loads(token, max_age=max_age)
    except Exception:
        return None
    
def generate_email_token(email):
    return serializer.dumps(email, salt="email-verification")


def verify_email_token(token, max_age=86400):
    try:
        return serializer.loads(
            token,
            salt="email-verification",
            max_age=max_age,
        )
    except Exception:
        return None