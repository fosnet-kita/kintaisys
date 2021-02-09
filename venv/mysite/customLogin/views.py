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
    """ƒ†[ƒU“o˜^"""
    template_name = 'customLogin/user_create.html'
    form_class = CustomUserCreateForm

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super().get(request, **kwargs)

    def form_valid(self, form):
        # ‰¼“o˜^
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # ƒ[ƒ‹‘—M
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
    """–{“o˜^Š®—¹"""
    template_name = 'customLogin/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60 * 60 * 24)  # ƒfƒtƒHƒ‹ƒg‚Å‚Í1“úˆÈ“à

    def get(self, request, **kwargs):
        """token‚ª³‚µ‚¯‚ê‚Î–{“o˜^."""
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')

        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        # ŠúŒÀØ‚ê
        except SignatureExpired:
            return HttpResponseBadRequest()

        # token‚ªŠÔˆá‚Á‚Ä‚¢‚é
        except BadSignature:
            return HttpResponseBadRequest()

        # token‚Í–â‘è‚È‚µ
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoenNotExist:
            return HttpResponseBadRequest()

        if not user.is_active:
            # –â‘è‚È‚¯‚ê‚Î–{“o˜^‚Æ‚·‚é
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()

            # QRƒR[ƒh¶¬
            request.session["img"] = utils.get_image_b64(utils.get_auth_url(user.email, utils.get_secret(user)))

            return super().get(request, **kwargs)

        return HttpResponseBadRequest()


class CustomLoginView(LoginView):
    """ƒƒOƒCƒ“"""
    form_class = CustomLoginForm
    template_name = 'customLogin/login.html'

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super().get(request, **kwargs)
