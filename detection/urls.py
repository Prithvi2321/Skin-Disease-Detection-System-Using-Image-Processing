from django.urls import path
from .import views
from .views import login_user, register_user, logout_user, detect_page, process_image, results_page
from .views import process_image

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import  generate_pdf

urlpatterns = [
    path('', views.home, name='home'),
    path('common-diseases/', views.common_diseases, name='common_diseases'),
    path('login/', login_user, name='login_user'),
    path('signup/', register_user, name='register_user'),
    path('logout/', logout_user, name='logout_user'),

    path('contact/', views.contact, name='contact'),  # Contact Page
    path('submit-contact/', views.submit_contact, name='submit_contact'),  # Contact Form Submission
    path('about/', views.about, name='about'),

    
    path('detect/', detect_page, name='detect'),
    path('process/', process_image, name='process_image'),
    path('results/', results_page, name='results'),
    # path('generate_pdf/', generate_pdf, name='generate_pdf'),
    path('generate-pdf/', generate_pdf, name='generate_pdf'),

    


]


# Add static files serving in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
