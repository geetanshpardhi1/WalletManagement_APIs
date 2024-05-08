from django.urls import path,include
from myapp.views import UserRegistration,LogoutAPIView,UserLoginView,ExpenseListView,ExpenseGroupedByCategoryView,MonthlyExpenseView
from rest_framework_simplejwt.views import TokenRefreshView

#routing for expense
from rest_framework.routers import DefaultRouter
from .views import ExpenseCategoryViewSet

router = DefaultRouter()
router.register(r'categories', ExpenseCategoryViewSet)

urlpatterns = [
    path('register/',UserRegistration.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('', include(router.urls)),
    path('expenses/', ExpenseListView.as_view(), name='expense-list'),
    path('expenses/grouped/', ExpenseGroupedByCategoryView.as_view(), name='expense-grouped'),
    path('expenses/category/<int:category_id>/monthly/', MonthlyExpenseView.as_view(), name='monthly-expense'),

]



