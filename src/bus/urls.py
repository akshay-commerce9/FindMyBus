from django.urls import path
from . import views

urlpatterns = [
    path("form/",views.formpage,name="formpage"),
    path("userreg",views.user_reg,name="userreg"),
    path("ownerreg",views.owner_reg,name="ownerreg"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("",views.home,name="guest_home"),
    path("adminhome/",views.adminhome,name="adminhome"),
    path("passengerhome/",views.passengerhome,name="passengerhome"),
    path("ownerhome/",views.ownerhome,name="ownerhome"),
    path("givecomplaint/",views.give_complaint,name="give_complaint"),
    path("viewcomplaint/",views.view_complaint,name="view_complaint"),
    path("delcomplaint/<int:id>",views.del_complaint,name="del_complaint"),
    path("viewusers/",views.view_users,name="view_users"),
    path("delpassenger/<int:id>",views.del_passenger,name="del_passenger"),
    path("delowner/<int:id>",views.del_owner,name="del_owner"),
    path("addbus/",views.add_bus,name="add_bus"),
    path("viewbus/",views.view_bus,name="view_bus"),
    path("delbus/<int:id>",views.del_bus,name="del_bus"),
    path("addroute/<int:id>",views.add_route,name="add_route"),
    path("viewroute/<int:id>",views.view_route,name="view_route"),
    path("delroute/<int:id>/<int:bsid>",views.del_route,name="del_route"),
    path("findbus", views.findbus, name="findbus"),
    path("ownercomplaint/",views.owner_complaint,name="owner_complaint"),
    path("track_bus",views.track_bus,name="track_bus"),


]
