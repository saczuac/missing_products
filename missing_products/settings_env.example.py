# DEBUG
DEBUG = True

# DJANGO SECRET KEY
SECRET_KEY = 'xh=yw8#%ob65a@ijq=2r41(6#8*ghhk7an)bcupk6ifd42bid+'

# ALLOWED HOSTS
ALLOWED_HOSTS = []

# DBS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'root',
        'PASSWORD': 'secret',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
