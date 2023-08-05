#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db.models.signals import class_prepared
from importlib import import_module

from otree.db import models
from otree.models.session import Session
from otree.models.participant import Participant

# NOTE: this imports the following submodules and then subclasses several
# classes importing is done via import_module rather than an ordinary import.
# The only reason for this is to hide the base classes from IDEs like PyCharm,
# so that those members/attributes don't show up in autocomplete,
# including all the built-in django model fields that an ordinary oTree
# programmer will never need or want. if this was a conventional Django
# project I wouldn't do it this way, but because oTree is aimed at newcomers
# who may need more assistance from their IDE, I want to try this approach out.
# this module is also a form of documentation of the public API.

subsession_module = import_module('otree.models.subsession')
group_module = import_module('otree.models.group')
player_module = import_module('otree.models.player')
session_module = import_module('otree.models.session')


def ensure_required_fields(sender, **kwargs):
    """
    Some models need to hook up some dynamically created fields. They can be
    created on the fly or might be defined by the user in the app directly.

    We use this signal handler to ensure that these fields exist and are
    created on demand.
    """
    if hasattr(sender, '_ensure_required_fields'):
        sender._ensure_required_fields()

class_prepared.connect(ensure_required_fields)


class BaseSubsession(subsession_module.BaseSubsession):

    class Meta:
        abstract = True
        ordering = ['pk']

    session = models.ForeignKey(
        Session, related_name='%(app_label)s_%(class)s', null=True)

    round_number = models.PositiveIntegerField(
        db_index=True,
        doc='''If this subsession is repeated (i.e. has multiple rounds), this
        field stores the position (index) of this subsession, among subsessions
        in the same app.

        For example, if a session consists of the subsessions:

            [app1, app2, app1, app1, app3]

        Then the round numbers of these subsessions would be:

            [1, 1, 2, 3, 1]

        '''
    )

    def get_groups(self):
        return super(BaseSubsession, self).get_groups()

    def set_groups(self, groups_list):
        return super(BaseSubsession, self).set_groups(groups_list)

    def get_group_matrix(self):
        return super(BaseSubsession, self).get_group_matrix()

    def set_group_matrix(self, group_matrix):
        return super(BaseSubsession, self).set_group_matrix(group_matrix)

    def get_players(self):
        return super(BaseSubsession, self).get_players()

    @property
    def app_name(self):
        return self._meta.app_config.name

    def in_previous_rounds(self):
        return super(BaseSubsession, self).in_previous_rounds()

    def in_all_rounds(self):
        return super(BaseSubsession, self).in_all_rounds()

    def before_session_starts(self):
        return super(BaseSubsession, self).before_session_starts()

    def in_round(self, round_number):
        return super(BaseSubsession, self).in_round(round_number)

    def in_rounds(self, first, last):
        return super(BaseSubsession, self).in_rounds(first, last)

    def group_like_round(self, round_number):
        return super(BaseSubsession, self).group_like_round(round_number)

    def group_randomly(self, fixed_id_in_group=False):
        return super(BaseSubsession, self).group_randomly(fixed_id_in_group)


class BaseGroup(group_module.BaseGroup):

    class Meta:
        abstract = True
        ordering = ['pk']

    session = models.ForeignKey(
        Session, related_name='%(app_label)s_%(class)s'
    )

    subsession = None

    round_number = models.PositiveIntegerField(db_index=True)

    def set_players(self, players_list):
        return super(BaseGroup, self).set_players(players_list)

    def get_players(self):
        return super(BaseGroup, self).get_players()

    def get_player_by_role(self, role):
        return super(BaseGroup, self).get_player_by_role(role)

    def get_player_by_id(self, id_in_group):
        return super(BaseGroup, self).get_player_by_id(id_in_group)

    def in_previous_rounds(self):
        return super(BaseGroup, self).in_previous_rounds()

    def in_all_rounds(self):
        return super(BaseGroup, self).in_all_rounds()

    def in_round(self, round_number):
        return super(BaseGroup, self).in_round(round_number)

    def in_rounds(self, first, last):
        return super(BaseGroup, self).in_rounds(first, last)


class BasePlayer(player_module.BasePlayer):

    class Meta:
        abstract = True
        ordering = ['pk']

    id_in_group = models.PositiveIntegerField(
        null=True,
        db_index=True,
        doc=("Index starting from 1. In multiplayer games, "
             "indicates whether this is player 1, player 2, etc.")
    )

    payoff = models.CurrencyField(
        null=True,
        doc="""The payoff the player made in this subsession""",
    )

    participant = models.ForeignKey(
        Participant, related_name='%(app_label)s_%(class)s'
    )

    session = models.ForeignKey(
        Session, related_name='%(app_label)s_%(class)s'
    )

    group = None
    subsession = None

    round_number = models.PositiveIntegerField(db_index=True)

    def in_previous_rounds(self):
        return super(BasePlayer, self).in_previous_rounds()

    def in_all_rounds(self):
        return super(BasePlayer, self).in_all_rounds()

    def get_others_in_group(self):
        return [p for p in self.group.get_players() if p != self]

    def get_others_in_subsession(self):
        return [p for p in self.subsession.get_players() if p != self]

    def role(self):
        return super(BasePlayer, self).role()

    def in_round(self, round_number):
        return super(BasePlayer, self).in_round(round_number)

    def in_rounds(self, first, last):
        return super(BasePlayer, self).in_rounds(first, last)
