# Добавьте 'portal' в INSTALLED_APPS
#INSTALLED_APPS = [
 #   ...
  #  'portal',
#]

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portal_korund',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
