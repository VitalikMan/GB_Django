from random import choices
from django import forms


class GameCoin(forms.Form):
    game = forms.ChoiceField(choices=(('coin', 'Монетка'), ('kub', 'Кубик'), ('numbers', 'Случайное число')))
    size = forms.IntegerField(min_value=1, max_value=64)
