from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from login.tests.scenario import (
    default_scenario_login,
    user_contractor,
)

from pump.models import Event
from pump.tests.scenario import (
    default_scenario_pump,
    get_area_hatherleigh,
    get_event_history,
    get_event_microchip,
)


class TestEventViewPerm(PermTestCase):

    def setUp(self):
        default_scenario_login()
        user_contractor()
        default_scenario_pump()

    def test_create_anon(self):
        self.assert_any(reverse('pump.event.create.anon'))

    def test_create_anon_post(self):
        url = reverse('pump.event.create.anon')
        data = dict(
            name='Patrick',
            email='code@pkimber.net',
            area=get_area_hatherleigh().pk,
            title='Jazz Night',
            event_date='06/02/2014',
            event_time='18:45',
            description='Our next fund raising event...',
            captcha_0='testing',
            captcha_1='PASSED',
        )
        response = self.client.post(url, data)
        print response
        self.assertEqual(response.status_code, 302)
        Event.objects.get(name='Patrick')

    def test_create_trust_perm(self):
        self.assert_logged_in(reverse('pump.event.create.trust'))

    def test_detail_perm(self):
        """the 'assert_logged_in' method uses the 'web' user"""
        event = get_event_microchip()
        self.assert_logged_in(
            reverse('pump.event.detail', kwargs={'pk': event.pk})
        )

    def test_list_perm(self):
        self.assert_logged_in(reverse('pump.event.list'))

    def test_publish_perm(self):
        event = get_event_history()
        self.assert_logged_in(
            reverse('pump.event.publish', kwargs={'pk': event.pk})
        )

    def test_remove_perm(self):
        event = get_event_history()
        self.assert_logged_in(
            reverse('pump.event.remove', kwargs={'pk': event.pk})
        )

    def test_update_perm(self):
        event = get_event_microchip()
        self.assert_logged_in(
            reverse('pump.event.update', kwargs={'pk': event.pk})
        )
