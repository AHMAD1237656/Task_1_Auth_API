from django.urls import path
from .views import (
    RegisterView,
    UserProfileView,
    UpdateProfileView,
    ChangePasswordView,
    ForgotPasswordView,
    ResetPasswordView,
    VerifyEmailView,
    GenerateEmailVerificationTokenView,
    AdminDashboardView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("profile/update/", UpdateProfileView.as_view(), name="update-profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path( "forgot-password/",ForgotPasswordView.as_view(), name="forgot-password"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-password"),
    path( "generate-email-token/", GenerateEmailVerificationTokenView.as_view(), name="generate-email-token"),
    path("verify-email/", VerifyEmailView.as_view(), name="verify-email"),
    path("admin-dashboard/", AdminDashboardView.as_view(), name="admin-dashboard"),
]