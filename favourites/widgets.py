from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


# Inherits builtin class from Django, checkbox removes future product image
class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'favourites/custom_widget_templates/custom_clearable_file_input.html'
    )
