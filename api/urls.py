from django.urls import path

from .views.accounts import (CreateUserView, LoginView, LogoutView, get_refresh_view,
                             UserEditView, MaleUserListView, FemaleUserListView,
                             UserDetailView, EmailGetView, PointGetView,
                             TimeListView, RaceListView, PointEditView)

from .views.blog import (CreateBlogView, EditBlogView, CreateBlogNotThumbnailView,
                         ListBlogView, ListGenreView,
                         DetailBlogBeforPurchaseView, BuyBlogView, GetBoughtView,
                         BlogBodyView, ListBlogAuthorView, ListMineBlogView,
                         EditBlogNotThumbnailView)

from .views.point import (test_payment, save_stripe_info)

from .views.message import (CreateMessageFromMaleView, CreateMessageFromFemaleView, ListMessageBoxView)


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('token-refresh/', get_refresh_view().as_view()),

    path('create-user/', CreateUserView.as_view()),
    path('edit-user/', UserEditView.as_view()),
    path('female-user-list/', FemaleUserListView.as_view()),
    path('male-user-list/', MaleUserListView.as_view()),
    path('detail-user/<str:pk>/', UserDetailView.as_view()),
    path('email-get/', EmailGetView.as_view()),
    path('point-get/', PointGetView.as_view()),
    path('point-edit/', PointEditView.as_view()),
    path('time-list/', TimeListView.as_view()),
    path('race-list/', RaceListView.as_view()),

    path('create-blog/', CreateBlogView.as_view()),
    path('create-blog-not-thumbnail/', CreateBlogNotThumbnailView.as_view()),
    path('edit-blog/<str:pk>/', EditBlogView.as_view()),
    path('edit-blog-not-thumbnail/<str:pk>/', EditBlogNotThumbnailView.as_view()),
    path('list-blog/', ListBlogView.as_view()),
    path('list-mine-blog/', ListMineBlogView.as_view()),
    path('list-genre/', ListGenreView.as_view()),
    path('detail-blog-befor-purchase/<str:pk>/', DetailBlogBeforPurchaseView.as_view()),
    path('detail-blog-author/<str:author>/', ListBlogAuthorView.as_view()),
    path('blog-body/<str:pk>/', BlogBodyView.as_view()),
    path('blog-buy/', BuyBlogView.as_view()),
    path('is-bought/', GetBoughtView.as_view()),

    path('test-payment/', test_payment),
    path('save-stripe-info/', save_stripe_info),

    path('create-message-from-male/', CreateMessageFromMaleView.as_view()),
    path('create-message-from-female/', CreateMessageFromFemaleView.as_view()),
    path('list-message-from-female/', ListMessageBoxView.as_view()),
]
