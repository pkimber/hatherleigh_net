# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.test import TestCase

from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
    get_user_web,
    user_contractor,
)

from pump.models import get_home_body
from pump.tests.model_maker import (
    make_story,
    make_story_block,
)
from pump.tests.scenario import (
    default_scenario_pump,
    get_site_hatherleigh,
    get_story_craft_fair,
    get_story_market_fire,
)


class TestStory(TestCase):

    def setUp(self):
        default_scenario_login()
        user_contractor()
        default_scenario_pump()

    def _create_anon(self):
        return make_story(
            make_story_block(get_home_body()),
            get_site_hatherleigh(),
            order=1,
            story_date=datetime.now(),
            name='Pat',
            email='code@pkimber.net',
            title='Alpha Male',
            description='completed their 300 mile paddle',
        )

    def _create_trust(self):
        return make_story(
            make_story_block(get_home_body()),
            get_site_hatherleigh(),
            order=1,
            story_date=datetime.now(),
            user=get_user_staff(),
            title='10 Pub Barrel Pull Success',
            description='10 Pub Pull on Saturday',
        )

    def test_can_edit(self):
        """
        A story can be edited by the person who created it (or a member of
        staff).
        """
        story = get_story_market_fire()
        self.assertTrue(story.user_can_edit(get_user_web()))

    def test_can_edit_not(self):
        """
        A story can only be edited by the person who created it (or a member
        of staff).  The craft fair story was created by an anonymous user.
        """
        story = get_story_craft_fair()
        self.assertFalse(story.user_can_edit(get_user_web()))


    def test_create_anon(self):
        self._create_anon()

    def test_create_trust(self):
        self._create_trust()

    def test_create_no_user_or_name(self):
        self.assertRaises(
            ValueError,
            make_story,
            make_story_block(get_home_body()),
            order=1,
            story_date=datetime.now(),
            site=get_site_hatherleigh(),
            title='Alpha Male',
            description='completed their 300 mile paddle',
        )

    def test_is_trusted(self):
        story = self._create_trust()
        self.assertTrue(story.is_trusted)

    def test_is_trusted_not(self):
        story = self._create_anon()
        self.assertFalse(story.is_trusted)

    def test_truncated(self):
        story = self._create_trust()
        story.truncated()
