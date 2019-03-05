from .article import (
    ArticleDetailView,
    ArticleListView,
    ArticleManageView,
    ArticleDeleteView
)
from .category import (
    CategoryListView,
    CategoryManageView,
    CategoryDeleteView
)
from .media import (
    MediaListView,
    MediaManageView,
    MediaDeleteView
)
from .membergroup import (
    MemberGroupListView,
    MemberGroupManageView,
    MemberGroupDeleteView
)
from .user import (
    UserListView,
    UserManageView,
    UserDeleteView
)
from .main import home_redirect
from .prof import ProfView
from .student import StudentView
from .user import RegistrationView

__all__ =  [
    'ArticleDetailView',
    'ArticleListView',
    'ArticleManageView',
    'ArticleDeleteView',
    'CategoryListView',
    'CategoryManageView',
    'CategoryDeleteView',
    'home_redirect',
    'MemberGroupListView',
    'MemberGroupManageView',
    'MemberGroupDeleteView',
    'MediaListView',
    'MediaManageView',
    'MediaDeleteView',
    'ProfView',
    'StudentView',
    'RegistrationView',
    'UserListView',
    'UserManageView',
    'UserDeleteView',

]