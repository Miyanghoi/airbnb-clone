from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# . 은 같은 폴더에 있는 models를 호출한다는 의미
from . import models


# decorator(@붙은 것)
# 아래와 같은 것이 admin.site.register(models.User, CustomUserAdmin) (Django doc.에 나와있음)
# 뜻은 admin패널에서 User를 보고 싶어 임
# 이 User를 Control할 class는 CustomUserAdmin이야
# 반드시 class명 위에 따라붙어야 실행됨
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    # class CustomUserAdmin(admin.ModelAdmin):

    """Custom User Admin"""
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )


# Shift + Alt + A
"""     list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = (
        "language",
        "currency",
        "superhost",
    )
 """
