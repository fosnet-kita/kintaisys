import base64
import qrcode
from io import BytesIO
import onetimepass


def get_secret(user):
    """
    �{���͔閧����ݒ肷��񂾂낤���ǁA�ʓ|�Ȃ̂ŁA�u���[���A�h���X�v�Ɓu�o�^�����v�������������m���g���B��ӂɂȂ�΂Ƃ肠�����������ȂƁB�B�B
    """
    return base64.b32encode(
        (user.email + str(user.date_joined)).encode()
    ).decode()


def get_auth_url(email, secret, issuer='ProjectName'):
    """
    ���ɏ����Ă���URL�t�H�[�}�b�g�Őݒ肷��K�v������B
    �ŏ��́uisr�v�uuid�v�́AGoogle�F�؃V�X�e���̃A�v����ɂ��\������邩��A�v���W�F�N�g���ƃ��[���A�h���X��˂����ނ̂�����Ǝv���B
    """
    url_template = 'otpauth://totp/{isr}:{uid}?secret={secret}&issuer={isr}'
    return url_template.format(
        uid=email,
        secret=secret,
        isr=issuer)


def get_image_b64(url):
    qr = qrcode.make(url)
    img = BytesIO()
    qr.save(img)
    return base64.b64encode(img.getvalue()).decode()


def get_token(user):
    return str(onetimepass.get_totp(get_secret(user)))
