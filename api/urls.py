from django.urls import include, path

app_name = 'api'
urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('social/', include('social.urls')),
    path('curia/', include('curia.urls')), 
    path('praesidium/', include('praesidium.urls')), 
    path('meetings/', include('meetings.urls')), 
    path('works/', include('works.urls')), 
    path('finance/', include('finance.urls')), 
    path('reports/', include('reports.urls')), 
    path('feedback/', include('contact.urls')), 
] 