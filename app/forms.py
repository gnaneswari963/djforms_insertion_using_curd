from django import forms

g=[['male','male'],['female','female']]
c=[['python','python'],['sql','sql'],['web technology','web technology']]

class NameForm(forms.Form):
    Sname=forms.CharField()
    Sprincipal=forms.CharField()
    Slocation=forms.CharField()

class StudentForm(forms.Form):
    sname=forms.CharField()
    sage=forms.IntegerField()
    sgender=forms.ChoiceField(choices=g)
    #sgender=forms.CharField(choices=g,widget=forms.RadioSelect)
    
    scourse=forms.MultipleChoiceField(choices=c)
    #scourse=forms.CharField(choices=c,widget=forms.CheckboxSelectMultiple)
    saddress=forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':10}))
    spassword=forms.CharField(widget=forms.PasswordInput)

    