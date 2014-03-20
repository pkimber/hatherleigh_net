# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import (
    date,
    time,
)
from dateutil.relativedelta import relativedelta

from django.contrib.sites.models import Site

from base.tests.model_maker import init_site
from block.models import (
    ModerateState,
    Page,
    Section,
)
from block.tests.model_maker import (
    make_page,
    make_section,
)
from block.tests.scenario import default_moderate_state
from login.tests.scenario import (
    get_user_staff,
    get_user_web,
)

from pump.models import (
    Event,
    get_page_home,
    get_section_body,
    PAGE_HOME,
    SECTION_BODY,
    Story,
)
from pump.tests.model_maker import (
    make_event,
    make_event_block,
    make_story,
    make_story_block,
)


def get_site_exbourne():
    return Site.objects.get(name='Exbourne')


def get_site_hatherleigh():
    return Site.objects.get(name='Hatherleigh')


def get_event_history():
    return Event.objects.get(title='History Society')


def get_event_microchip():
    return Event.objects.get(title='Free Microchipping for Dogs')


def get_event_temp():
    return Event.objects.get(title='Temp Title')


def get_event_temp_today():
    return Event.objects.get(title='Temp Title Today')


def get_story_craft_fair():
    return Story.objects.get(title='Craft Fair')


def get_story_market_fire():
    return Story.objects.get(title='Market Offices burnt down')


def get_story_market_planning():
    return Story.objects.get(title='The Market Planning has been Approved')


def get_story_mg_descend():
    return Story.objects.get(title='MGs descend on Hatherleigh')


def default_section(verbose=None):
    try:
        page = Page.objects.get(slug=PAGE_HOME)
    except Page.DoesNotExist:
        page = make_page('Home', 0)
        if verbose:
            print('created page: {}'.format(page))
    try:
        section_event = Section.objects.get(slug=SECTION_BODY)
    except Section.DoesNotExist:
        section_event = make_section('Body')
        if verbose:
            print('created section: {}'.format(section_event))


def default_site(verbose=None):
    init_site(1, 'Hatherleigh', 'hatherleigh.net')
    init_site(2, 'Exbourne', 'exbourne.net')
    init_site(3, 'Jacobstowe', 'jacobstowe.net')


def default_scenario_pump():
    default_section()
    default_moderate_state()
    default_site()
    # story
    make_story(
        block=make_story_block(get_page_home(), get_section_body()),
        order=1,
        user=get_user_staff(),
        site=get_site_hatherleigh(),
        title='MGs descend on Hatherleigh',
        description=(
            "The Taw and Torridge MG owners club came to Hatherleigh, on "
            "Tuesday, to join the crowds at Hatherleigh Market. They came "
            "to visit Martin at the Hatherleigh Fish Bar. Martin the owner "
            "of the bar also has two MGs."
        )
    )
    make_story(
        block=make_story_block(get_page_home(), get_section_body()),
        order=2,
        user=get_user_web(),
        site=get_site_hatherleigh(),
        title='Market Offices burnt down',
        description=(
            "The market offices burnt down last night. I am sure theories "
            "will abound around the town, but we will have to wait until the "
            "Police have done their bit, before we will know. The offices "
            "and files held within seam to have been totalled destroyed. "
            "Tomorrow's Market should go ahead although the auction will "
            "NOT take place, but the stallholders hopefully will be selling "
            "their wares"
        )
    )
    make_story(
        block=make_story_block(get_page_home(), get_section_body()),
        order=3,
        name='Pat',
        email='code@pkimber.net',
        site=get_site_exbourne(),
        title='Craft Fair',
        description=(
            "Over 200 entries were exhibited at the Hatherleigh Craft Show, "
            "at its launch in Hatherleigh Community Centre on Sunday 4th "
            "August. Judges had the difficult task of awarding rosettes for "
            "1st, 2nd & 3rd places in each of the 24 classes, ranging from "
            "knitting to metal work."
        )
    )
    story = make_story(
        block=make_story_block(get_page_home(), get_section_body()),
        order=4,
        name='Pat',
        email='test@pkimber.net',
        site=get_site_hatherleigh(),
        title='The Market Planning has been Approved',
        description=(
            "I had an eye opening experience, last week, that left me "
            "ashamed of our democracy. The paid planners of the council, "
            "recommended that the outline planning application for "
            "Hatherleigh Market be approved as presented by the paid "
            "consultants."
        )
    )
    story.created = date.today() + relativedelta(months=-1, day=7)
    story.set_published(get_user_staff())
    story.save()
    # event
    event_date = date.today() + relativedelta(days=8)
    make_event(
        block=make_event_block(get_page_home(), get_section_body()),
        order=1,
        user=get_user_web(),
        site=get_site_exbourne(),
        title='Free Microchipping for Dogs',
        event_date=event_date,
        event_time=time(19, 30),
        description=(
            "Free Microchipping The law is changing! As from the 6th April "
            "2016 you must have your dog microchipped - please visit us at "
            "At The Burrow Cafe, Exbourne on Friday 7th February, between "
            "10am - 12noon, from the Dogs Trust & West Devon Borough Council "
            "Customer Service Advisor to help with all your council and many "
            "public service enquiries Everyone Welcome"
        )
    )
    event_date = date.today() + relativedelta(days=4)
    make_event(
        block=make_event_block(get_page_home(), get_section_body()),
        order=2,
        name='Pat',
        email='code@pkimber.net',
        site=get_site_exbourne(),
        title='History Society',
        event_date=event_date,
        event_time=time(19, 30),
        description=(
            "On Monday February 10th at 7:30pm in Old Schools Dr. Janet Few "
            "will be giving an illustrated talk entitled ‘Farm, Fish, Faith "
            "and Family’. As usual all are welcome (non-members £2) The "
            "History Society is currently investigating Hatherleigh’s "
            "prehistoric history and is keen to hear of any finds relating "
            "to this period in particular worked flints such as the one "
            "recently found by a pupil at the School."
        )
    )
    event_date = date.today()
    make_event(
        block=make_event_block(get_page_home(), get_section_body()),
        order=3,
        name='Pat',
        email='code@pkimber.net',
        site=get_site_hatherleigh(),
        title='Temp Title Today',
        event_date=event_date,
        event_time=time(19, 30),
        description=(
            "Temp Description for Today"
        )
    )
    event_date = date.today() + relativedelta(days=-5)
    make_event(
        block=make_event_block(get_page_home(), get_section_body()),
        order=4,
        name='Pat',
        email='code@pkimber.net',
        site=get_site_hatherleigh(),
        title='Temp Title',
        event_date=event_date,
        event_time=time(19, 30),
        description=(
            "Temp Description"
        )
    )
