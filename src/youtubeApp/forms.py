from django import forms
from .models import Channel, VideoDetail

class ChannelForm(forms.ModelForm):
    class Meta:
        model=Channel
        fields=('name','category',)
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'enter your channel name','class':'border rounded w-full py-2 px-4 outline-none focus:shadow-outline'}),
            'category':forms.Select(attrs={'class':'border rounded w-full py-2 px-4 outline-none focus:shadow-outline'})
        }

class EditChannelForm(forms.ModelForm):
    class Meta:
        model=Channel
        fields=('name','channel_art','channel_icon','description')
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'enter your channel name','class':'border mb-2 rounded w-full py-2 px-4 outline-none focus:shadow-outline'}),
            'channel_art':forms.FileInput(attrs={'class':'border-0  mb-4 outline-none'}),
            'channel_icon':forms.FileInput(attrs={'class':'border-0  mb-4 outline-none'}),
            'description':forms.Textarea(attrs={'class':'border rounded w-full py-2 px-4 outline-none focus:shadow-outline'})
        }

class VideoDataForm(forms.ModelForm):
    class Meta:
        model=VideoDetail
        fields=('title','description','visibility','thumbnail')
        widgets={
            'title':forms.TextInput(attrs={'class':'shadow appearance-none mb-4 border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'description':forms.Textarea(attrs={'class':'shadow appearance-none mb-4 border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'visibility':forms.Select(attrs={'class':'box-border border py-2 border-gray-400 w-full focus:outline-none'}),
            'thumbnail':forms.ClearableFileInput(attrs={'class':'border-0  mb-4 outline-none'}),
        }

