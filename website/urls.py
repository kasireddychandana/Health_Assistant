from django.urls import path,include
from .views import home, precautions, infectious, noncommunicable,genetic, neurological, mental, deficiency, preinfectious, prenoncommunicable, premental, preneurological, pregenetic, predeficiency,streamlit_view,contact_view,success
urlpatterns = [
    path('', home, name='home'),
    path('precautions/', precautions, name='precautions'),
    path('infectious/',infectious, name='infectious_precautions'),
    path('noncommunicable/', noncommunicable, name='noncommunicable'),
    path('genetic/', genetic, name='genetic'),
    path('neurological/', neurological, name='neurological'),
    path('mental/', mental, name='mental'),
    path('deficiency/', deficiency, name='deficiency'),
    path('preinfectious/', preinfectious, name='preinfectious'),
    path('prenoncommunicable/', prenoncommunicable, name='prenoncommunicable'),
    path('pregenetic/', pregenetic, name='pregenetic'),
    path('preneurological/', preneurological, name='preneurological'),
    path('premental/', premental, name='premental'),
    path('predeficiency/', predeficiency, name='predeficiency'), 
    path("streamlit/", streamlit_view, name="streamlit"),
    path('contact/', contact_view, name='contact'),
    path('success/', success, name='success'),
    
    
]
    # Add more URLs for other diseases

   


