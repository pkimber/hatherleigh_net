# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
    get_user_web,
    user_contractor,
)

from pump.models import (
    get_page_home,
    get_section_body,
)
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
from login.tests.scenario import (
    default_scenario_login,
    get_user_staff,
    get_user_web,
    user_contractor,
)


class TestStory(TestCase):

    def setUp(self):
        default_scenario_login()
        user_contractor()
        default_scenario_pump()

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
        make_story(
            make_story_block(get_page_home(), get_section_body()),
            order=1,
            name='Pat',
            email='code@pkimber.net',
            site=get_site_hatherleigh(),
            title='Alpha Male',
            description='completed their 300 mile paddle',
        )

    def test_create_trust(self):
        make_story(
            make_story_block(get_page_home(), get_section_body()),
            order=1,
            user=get_user_staff(),
            site=get_site_hatherleigh(),
            title='10 Pub Barrel Pull Success',
            description='10 Pub Pull on Saturday',
        )

    def test_create_no_user_or_name(self):
        self.assertRaises(
            ValueError,
            make_story,
            make_story_block(get_page_home(), get_section_body()),
            order=1,
            site=get_site_hatherleigh(),
            title='Alpha Male',
            description='completed their 300 mile paddle',
        )

    def test_published(self):
        story = get_story_craft_fair()
        story.set_published(get_user_staff())
        story.save()
        self.assertTrue(get_story_craft_fair().is_published)

    def test_published_not(self):
        story = get_story_craft_fair()
        self.assertFalse(get_story_craft_fair().is_published)

    def test_removed(self):
        story = get_story_craft_fair()
        story.set_removed(get_user_staff())
        story.save()
        self.assertTrue(get_story_craft_fair().is_removed)

    def test_removed_not(self):
        story = get_story_craft_fair()
        self.assertFalse(get_story_craft_fair().is_removed)
