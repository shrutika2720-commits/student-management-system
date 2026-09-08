diff --git a/aai_lab_project/settings.py b/aai_lab_project/settings.py
index 0000000..0000000 100644
--- a/aai_lab_project/settings.py
+++ b/aai_lab_project/settings.py
@@
 INSTALLED_APPS = [
@@
     'students',
+    'accounts',
 ]
@@
 STATIC_URL = '/static/'
 DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
+
+# Auth settings
+LOGIN_REDIRECT_URL = '/' 
+LOGOUT_REDIRECT_URL = '/' 
+
+# Use console email backend for password reset in development
+EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
+DEFAULT_FROM_EMAIL = 'no-reply@example.com'
