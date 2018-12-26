from .views import home,trial
from django.conf.urls import url,include

urlpatterns = [
    url(r'home/$',home),
    url(r'home/trial$',trial,name='trial'),

]
