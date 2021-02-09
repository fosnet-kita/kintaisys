from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads,dumps
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import get_template
from django.views import generic
from .forms import CustomUserCreateForm
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from . import utils

User = get_user_model()

class UserCreate(generic.CreateView):
    """���[�U�o�^"""
    template_name = 'customLogin/user_create.html'
    form_class = CustomUserCreateForm

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super().get(request, **kwargs)

    def form_valid(self, form):
        # ���o�^
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # ���[�����M
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': domain,
            'token': dumps(user.pk),
            'user': user
        }
        subject_template = get_template('customLogin/mail/subject.txt')
        message_template = get_template('customLogin/mail/message.txt')
        subject = subject_template.render(context)
        message = message_template.render(context)
        user.email_user(subject, message)
        return redirect('customLogin:user_create_done')
        
        
        
class UserCreateComplete(generic.TemplateView):
    """�{�o�^����"""
    template_name = 'customLogin/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60 * 60 * 24)  # �f�t�H���g�ł�1���ȓ�

    def get(self, request, **kwargs):
        """token����������Ζ{�o�^."""
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')

        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        # �����؂�
        except SignatureExpired:
            return HttpResponseBadRequest()

        # token���Ԉ���Ă���
        except BadSignature:
            return HttpResponseBadRequest()

        # token�͖��Ȃ�
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoenNotExist:
            return HttpResponseBadRequest()

        if not user.is_active:
            # ���Ȃ���Ζ{�o�^�Ƃ���
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()

            # QR�R�[�h����
            request.session["img"] = utils.get_image_b64(utils.get_auth_url(user.email, utils.get_secret(user)))

            return super().get(request, **kwargs)

        return HttpResponseBadRequest()


class CustomLoginView(LoginView):
    """���O�C��"""
    form_class = CustomLoginForm
    template_name = 'customLogin/login.html'

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super().get(request, **kwargs)
