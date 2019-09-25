from django.urls import path
from django.conf.urls import url
from .views import ApplianceList, SubscriptionList, api_root, ApplianceDetails

urlpatterns = [
    path('', api_root),
    path('appliance/', ApplianceList.as_view(), name=ApplianceList.name),
    path('subscribe/', SubscriptionList.as_view(), name=SubscriptionList.name),
    url(r'^appliance/?P<pk>[0-9]+)/$', ApplianceDetails.as_view(), name="Details"),
    url(r'^appliance/?P<name>[a-zA-Z]+)/$', ApplianceDetails.as_view(), name="Details By Name"),
]
