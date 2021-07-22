from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:   # 외적인 정보(가로세로 너비, 어디서 찍었는지, 언제 찍었는지 등등..)
        model = Profile
        fields = ['image', 'nickname', 'message']   # 'user' 정보는 서버단에서 처리하는 정보