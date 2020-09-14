from __future__ import unicode_literals
from django.urls import re_path
#from django.conf.urls import patterns,
from . import views

urlpatterns = [
 re_path(r'^$', views.EventMonthView.as_view(), name='list'),
    re_path(r'^month/shift/$', views.EventMonthView.as_view(), name='month_shift'),
    re_path(r'^event-list/shift/$', views.EventMonthView.as_view(), name='event_list_shift'),
    re_path(r'^cal-and-list/shift/$', views.EventMonthView.as_view(), name='cal_and_list_shift'),
    re_path(r'^event/(?P<pk>[\w-]+)/$', views.EventDetailView.as_view(), name='detail'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2}|\d)/$', views.EventMonthView.as_view(), name='list'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2}|\d)/(?P<day>\d{2}|\d)/$',views.EventDayView.as_view(), name='day_list'),

                       ]
