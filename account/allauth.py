from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri

# 账户认证的 AllAuth 配置
class AccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_url(self, request, emailconfirmation):
        location = '/account/verify-email/{}'.format(emailconfirmation.key)
        return build_absolute_uri(None, location)