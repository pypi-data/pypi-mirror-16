# coding=utf-8
u"""
LICENSE:
Copyright 2015,2016 Hermann Krumrey

This file is part of kudubot.

    kudubot makes use of various third-party python modules to serve
    information via online chat services.

    kudubot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    kudubot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with kudubot.  If not, see <http://www.gnu.org/licenses/>.
LICENSE
"""

# imports
from __future__ import absolute_import
import re

from kudubot.servicehandlers.Service import Service
from kudubot.connection.generic.Message import Message


class ServiceSelectorService(Service):
    u"""
    The ServiceSelectorService Class that extends the generic Service class.
    The service allows admin users to enable and disable services
    """

    identifier = u"service_selector"
    u"""
    The identifier for this service
    """

    protected = True
    u"""
    May not be disabled
    """

    help_description = {u"en": u"/service\tallows activation/deactivation of services (admin)\n"
                              u"/service activate <service|service-index>\tactivates a service\n"
                              u"/service deactivate <service|service-index>\tdeactivates a service\n",
                        u"de": u"/service\tErmöglicht das Aktivieren/Deaktivieren von einem Service (admin)\n"
                              u"/service an <service|service-index>\tAktiviert ein Service\n"
                              u"/service aus <service|service-index>\tDeaktiviert ein Service\n"}
    u"""
    Help description for this service.
    """

    activation_keywords = {u"activate": (u"en", u"activate"),
                           u"deactivate": (u"en", u"deactivate"),
                           u"an": (u"de", u"activate"),
                           u"aus": (u"de", u"deactivate")}
    u"""
    Keywords that trigger a plugin activation or deactivation
    """

    already_activated = {u"en": u"is already activated or does not exist.",
                         u"de": u"ist bereits aktiviert oder existiert nicht."}
    u"""
    Reply for when a plugin was already activated
    """

    already_deactivated = {u"en": u"is already deactivated or does not exist.",
                           u"de": u"ist bereits deaktiviert oder existiert nicht."}
    u"""
    Reply for when a plugin was already deactivated
    """

    service_activated = {u"en": u"has been activated.",
                         u"de": u"wurde aktiviert."}
    u"""
    Reply for when a plugin was activated
    """

    service_deactivated = {u"en": u"has been deactivated.",
                           u"de": u"wurde deaktiviert."}
    u"""
    Reply for when a plugin was deactivated
    """

    protected_service_warning = {u"en": u"can not be deactivated",
                                 u"de": u"kann nicht deaktiviert werden"}
    u"""
    Reply when an attempt at deactivating a protected service is done
    """

    unauthorized_warning = {u"en": u"Sorry, I can't let you do that.",
                            u"de": u"Sorry, das darfst du nicht."}
    u"""
    Reply for non-admins
    """

    def process_message(self, message):
        u"""
        Process a message according to the service's functionality

        :param message: the message to process
        :return: None
        """
        authenticated = self.connection.authenticator.is_from_admin(message)

        parsed = message.message_body.lower().split(u"/service ", 1)[1]
        mode, selected_service_identifier = parsed.split(u" ", 1)
        language = self.activation_keywords[mode][0]

        if authenticated:

            try:
                selected_service_identifier = \
                    self.connection.service_manager.all_services[int(selected_service_identifier) - 1].identifier
            except (IndexError, ValueError):
                pass

            selected_service_class = None
            for service in self.connection.service_manager.all_services:
                if service.identifier == selected_service_identifier:
                    selected_service_class = service

            is_active = False
            for service in self.connection.service_manager.active_services:
                if service.identifier == selected_service_identifier:
                    is_active = True

            if self.activation_keywords[mode][1] == u"activate":
                if is_active or selected_service_class is None:
                    reply = selected_service_identifier + u" " + self.already_activated[language]
                else:
                    self.connection.service_manager.active_services.append(selected_service_class)
                    reply = selected_service_identifier + u" " + self.service_activated[language]
            else:
                if selected_service_class is None \
                        or selected_service_class not in self.connection.service_manager.active_services:
                    reply = selected_service_identifier + u" " + self.already_deactivated[language]
                elif selected_service_class in self.connection.service_manager.protected_services:
                    reply = selected_service_identifier + u" " + self.protected_service_warning[language]
                else:
                    self.connection.service_manager.active_services.remove(selected_service_class)
                    reply = selected_service_identifier + u" " + self.service_deactivated[language]

        else:
            reply = self.unauthorized_warning[language]

        reply_message = self.generate_reply_message(message, u"Help", reply)
        self.send_text_message(reply_message)

    @staticmethod
    def regex_check(message):
        u"""
        Checks if the user input is valid for this service to continue

        :return: True if input is valid, False otherwise
        """
        regex = u"^/service ("

        first = True
        for key in ServiceSelectorService.activation_keywords:
            if first:
                regex += key
                first = False
            else:
                regex += u"|" + key

        regex += u") ([0-9]+|[a-zA-Z]+(( [a-zA-Z]+)+)?)$"

        return re.search(re.compile(regex), message.message_body.lower())
