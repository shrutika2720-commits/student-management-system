diff --git a/aai_lab_project/urls.py b/aai_lab_project/urls.py
index 0000000..0000000 100644
--- a/aai_lab_project/urls.py
+++ b/aai_lab_project/urls.py
@@
 from django.contrib import admin
 from django.urls import path, include
 
 urlpatterns = [
     path('admin/', admin.site.urls),
-    path('', include('students.urls', namespace='students')),
+    path('', include('students.urls', namespace='students')),
+    path('accounts/', include('accounts.urls', namespace='accounts')),
 ]
