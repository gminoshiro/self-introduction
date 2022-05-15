# ↓過去のもの(一応残してる)
#from django.http import HttpResponse
#from django.views.generic import TemplateView

from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ContactForm
from .models import Profile, Work1, Experience, Education, Software, Technical
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap


class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]
        work_data = Work1.objects.order_by("-id")
        return render(request, 'mino/index.html', {
            'profile_data': profile_data,
            'work_data': work_data,
        })


class DetailView(View):
    def get(self, request, *args, **kwargs):
        work_data = Work1.objects.get(id=self.kwargs['pk'])
        return render(request, 'mino/detail.html', {
            'work_data': work_data
        })


class AboutView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        experience_data = Experience.objects.order_by('-id')
        education_data = Education.objects.order_by('-id')
        software_data = Software.objects.order_by('-id')
        technical_data = Technical.objects.order_by('-id')
        return render(request, 'mino/about.html', {
            'profile_data': profile_data,
            'experience_data': experience_data,
            'education_data': education_data,
            'software_data': software_data,
            'technical_data': technical_data,
        })


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        return render(request, 'mino/contact.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'お問い合わせありがとうございます。'
            contact = textwrap.dedent('''
                ※このメールはシステムからの自動返信です。

                {name} 様

                お問い合せありがとうございました。
                以下の内容でお問い合わせを受け付けいたしました。
                内容を確認させていただき、ご返信いたしますので、少々お待ちください。

                -------------------
                ■お名前
                {name}

                ■メールアドレス
                {email}

                ■メッセージ
                {message}
                -------------------

                ''').format(
                name=name,
                email=email,
                message=message
            )
            to_list = [email]
            bcc_list = [settings.EMAIL_HOST_USER]

            try:
                message = EmailMessage(subject=subject, body=contact, to=to_list, bcc=bcc_list)
                message.send()

            except BadHeaderError:
                return HttpResponse('無効なヘッダが検出されました。')

            return redirect('thanks')

        return render(request, 'mino/contact.html', {
            'form': form
        })


class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mino/thanks.html')


# ↓過去のもの(一応残してる)
# def index(request):
#    return HttpResponse("HttpResponse")

# class IndexView(TemplateView):
#    template_name = "mino/index.html"

# class AboutView(TemplateView):
#    template_name = "mino/about.html"

# def  portfoliofunc(request):
#    responseobject =  HttpResponse('まだありません。')
#    return responseobject

# class BlogView(TemplateView):
#    template_name = "mino/blog.html"

# def  contactfunc(request):
#    responseobject =  HttpResponse('まだできません')
#    return responseobject
