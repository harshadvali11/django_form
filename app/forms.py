from django import forms
g=[('MALE','male'),('FEMALE','female')]
c=[('python','python'),('django','django'),('sql','sql'),('webtech','webtech')]
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=5)
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)