from django.forms import IntegerField as FormIntegerField
from django.test import TestCase
from rest_framework.reverse import reverse as drf_reverse
from rest_framework.serializers import IntegerField as SerializerIntegerField

from . import factories
from .. import models


class TestSurveyField(TestCase):
    model = models.SurveyField
    factory = factories.SurveyFieldFactory

    @classmethod
    def setUpTestData(cls):
        cls.field = factories.SurveyFieldFactory.build(pk=1, field_type='number')

    def test_str(self):
        self.assertEqual(str(self.field), self.field.name)

    def test_key(self):
        self.assertEqual(self.field.key, 'question-1')

    def test_get_form_field(self):
        form_field = self.field.get_form_field()
        self.assertIsInstance(form_field, FormIntegerField)

    def test_get_serializer_field(self):
        form_field = self.field.get_serializer_field()
        self.assertIsInstance(form_field, SerializerIntegerField)


class TestSurveyFieldset(TestCase):
    model = models.SurveyFieldset
    factory = factories.SurveyFieldsetFactory

    def test_str(self):
        fieldset = self.factory.create()
        self.assertEqual(str(fieldset), fieldset.name)


class TestSurvey(TestCase):
    model = models.Survey
    factory = factories.SurveyFactory

    def test_str(self):
        survey = self.factory.create()
        self.assertEqual(str(survey), survey.name)

    def test_get_api_url(self):
        survey = self.factory.create()
        expected_url = drf_reverse('survey-form', kwargs={'pk': survey.pk})
        self.assertEqual(survey.get_api_url(), expected_url)


class TestUserResponse(TestCase):
    model = models.UserResponse
    factory = factories.UserResponseFactory

    def test_not_required(self):
        """
        This will throw an error if answers=[] is not allowed.

        Without accepting answers=[] on UserResponse, we can't have non-required
        questionnaire form fields.
        """
        self.factory.create(answers=[])

    def test_num_users(self):
        self.factory.create_batch(2, user_id='first_user')
        self.factory.create(user_id='second_user')
        self.assertEqual(self.model.objects.num_users(), 2)

    def test_latest_per_user(self):
        survey = factories.SurveyFactory.create()
        one, two = self.factory.create_batch(2, survey=survey)
        newer = self.factory.create(
            survey=survey,
            fieldset=one.fieldset,
            user_id=one.user_id,
        )
        self.factory.create()  # unrelated item since it has the wrong survey

        expected = {
            newer.user_id: {
                newer.fieldset.pk: newer.answers,
            },
            two.user_id: {
                two.fieldset.pk: two.answers,
            }
        }
        self.assertEqual(self.model.objects.latest_per_user(survey), expected)
