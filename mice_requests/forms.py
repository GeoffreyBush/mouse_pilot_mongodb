from django import forms
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe

from main.constants import EARMARK_CHOICES_PAIRED
from mice_repository.models import Mouse
from mice_requests.models import Request


# Custom widget will allow displaying graphical representation of selected mice in the future
class ReadOnlyMiceField(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = []
        rendered_inputs = []
        for i, val in enumerate(value):
            input_id = f"id_{name}_{i}"
            rendered_inputs.append(
                f'<input type="hidden" name="{name}" value="{val}" id="{input_id}">'
            )
            rendered_inputs.append(f"<p>{val}</p>")
        return mark_safe("\n".join(rendered_inputs))

    def value_from_datadict(self, data, files, name):
        if hasattr(data, "getlist"):
            return data.getlist(name)
        else:
            value = data.get(name, [])
            if isinstance(value, str):
                return [value]
            else:
                return [force_str(value) for value in data.get(name, [])]


class RequestForm(forms.ModelForm):

    task_type = forms.ChoiceField(
        choices=Request.TASK_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    mice = forms.ModelMultipleChoiceField(
        queryset=Mouse.objects.all(),
        widget=ReadOnlyMiceField,
    )

    # Should be able to initialise a form when no mice are selected from MouseSelectionForm

    def clean(self):
        cleaned_data = super().clean()
        task_type = cleaned_data.get("task_type")
        mice = cleaned_data.get("mice")

        errors = {}
        if not mice or len(mice) == 0:
            raise forms.ValidationError("You must select at least one mouse.")
        else:
            mice_errors = []
            if task_type == "Cull":
                for mouse in mice:
                    if mouse.is_culled():
                        mice_errors.append(f"Mouse {mouse} has already been culled.")
                    elif Request.objects.filter(task_type="Cull", mice=mouse).exists():
                        mice_errors.append(f"Mouse {mouse} already has a cull request.")

            elif task_type == "Clip":
                for mouse in mice:
                    if mouse.is_genotyped():
                        mice_errors.append(f"Mouse {mouse} has already been clipped.")
                    elif Request.objects.filter(task_type="Clip", mice=mouse).exists():
                        mice_errors.append(f"Mouse {mouse} already has a clip request.")

            if mice_errors:
                errors["mice"] = mice_errors

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data

    class Meta:
        model = Request
        fields = ["mice", "task_type"]


class ClipForm(forms.Form):
    earmark = forms.ChoiceField(
        label="Earmark results",
        choices=EARMARK_CHOICES_PAIRED[1:],
        widget=forms.Select(attrs={"class": "form-select"}),
    )


class CullForm(forms.Form):
    culled_date = forms.DateField(
        label="Date culled on:",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    )
    culled = forms.BooleanField(
        label="These mice have been culled",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        required=True,
    )
