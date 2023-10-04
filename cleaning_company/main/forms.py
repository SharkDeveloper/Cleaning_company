from .models import Order, Feedback
from django.forms import ModelForm, TextInput, Textarea , EmailInput, RadioSelect

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["name","email","subject","text"]
        widgets = {
            "name": TextInput(attrs={
                "name":"имя",
                "id":"input_content-comp-ll42rtmb2",
                "class":"KvoMHf has-custom-focus wixui-text-input__input",
                "type":"text",
                "placeholder":"Введите свое имя",
                "required":"",
                "aria-required":"true",
                "maxlength":"100",
                "value":""
            }),
            "email": EmailInput(attrs={
                "class": "KvoMHf has-custom-focus wixui-text-input__input",
                "placeholder":"Добавьте эл. почту"
            }),
            "subject": TextInput(attrs={
                "class": "KvoMHf has-custom-focus wixui-text-input__input",
                "placeholder":"Укажите тему"
            }),
            "text": Textarea(attrs={
                "id" : "textarea_comp-ll42rtmk2",
                "class" : "rEindN has-custom-focus wixui-text-box__input",
                "placeholder" : "Добавьте сообщение..."
            })
        }

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback 
        fields = ["name","surename","email","phone","review","recommendation","suggestion"]
        OPTIONS = (("да", "Да"), ("нет", "Нет"))
        widgets = {
            "name":TextInput(attrs={
                "name":"имя", 
                "id":"input_content-comp-ll42roqf1", 
                "class":"KvoMHf has-custom-focus wixui-text-input__input", 
                "type":"text", 
                "placeholder":"Имя", 
                "aria-required":"false", 
                "maxlength":"100", 
                "aria-label":"Имя",
                "value":""
            }),
            "surename":TextInput(attrs={
                "name":"фамилия", 
                "id":"input_content-comp-ll42roqm1",
                "class":"KvoMHf has-custom-focus wixui-text-input__input",
                "type":"text",
                "placeholder":"Фамилия",
                "aria-required":"false",
                "maxlength":"100",
                "aria-label":"Фамилия" 
            }),
            "email":EmailInput(attrs={
                "name":"email",
                "id":"input_content-comp-ll42roqj", 
                "class":"KvoMHf has-custom-focus wixui-text-input__input", 
                "type":"email", 
                "placeholder":"Эл. почта"
            }),
            "phone":TextInput(attrs={
                "name":"phone",
                "id":"input_content-comp-ll42roqp1",
                "class":"KvoMHf has-custom-focus wixui-text-input__input",
                "type":"tel",
                "placeholder":"Телефон", 
                "aria-required":"false", 
                "maxlength":"50", 
                "aria-label":"Телефон"
            }),
            "review":Textarea(attrs={
                "id":"textarea_comp-ll42roqs", 
                "class":"rEindN has-custom-focus wixui-text-box__input", 
                "placeholder":"Напишите отзыв здесь", 
                "aria-required":"false"
            }),
            #в review.html в возвращаемой кнопке ввел name="recommendation", без вставления формы
            "recommendation":RadioSelect(choices=OPTIONS,attrs={
                "class":"b33LKJ"
            }),
            "suggestion":Textarea(attrs={
                "id":"textarea_comp-ll42ror9", 
                "class":"rEindN has-custom-focus wixui-text-box__input", 
                "placeholder":"Хотите что-то добавить?", 
                "aria-required":"false"
            })
        }