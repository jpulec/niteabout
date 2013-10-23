from django.forms.widgets import Input

class RangeInput(Input):
    input_type = 'range'

class FeatureInput(RangeInput):
    def __init__(self, *args, **kwargs):
        super(FeatureInput, self).__init__(*args, **kwargs)
        self.attrs.update({
            'step': 1,
            'min': -5,
            'max': 5,})
