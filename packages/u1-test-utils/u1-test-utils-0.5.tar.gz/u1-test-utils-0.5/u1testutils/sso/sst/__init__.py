# Copyright 2012, 2013 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License version 3, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging

import sst.actions

from u1testutils.sso import mail
from u1testutils.sso.sst import pages


logger = logging.getLogger('User test')


def create_new_account(user, is_site_recognized=True):
    """Create a new account on Ubuntu Single Sign On.

    The browser must be on the Log in page.
    If the account creation succeeds, the browser will be back on the site
    that requested the log in.

    Keyword arguments:
    user -- The user object with the information for the new account.
        It must have the full_name, email and password attributes.
    is_site_recognized -- Boolean indicating if the site that requested the
        log in is recognized. If it is not recognized, all the user available
        information will be send to it. Default is True.

    """
    log_in = pages.UnifiedLogInCreateAccountFromRedirect()
    create_account = log_in.go_to_create_new_account()
    create_account.create_ubuntu_sso_account(user)

    if not is_site_recognized:
        site_not_recognized = pages.SiteNotRecognized()
        site_not_recognized.make_all_information_available_to_website()
        site_not_recognized.yes_sign_me_in()
    else:
        _assert_site_not_recognized_page_not_opened()


def _assert_site_not_recognized_page_not_opened():
    try:
        sst.actions.fails(pages.SiteNotRecognized)
    except AssertionError:
        suggestion = (
            'Please check that you are accessing SSO from a server that is '
            'trusted. Otherwise, the unexpected Site Not Recognized page will '
            'be opened.')
        logger.error(suggestion)
        raise


def validate_user_email(user):
    """Validate user's email address.

    The user must be logged in and received the verification email
    (for example, right after registration).
    If the this succeeds, the browser will be redirected to user's
    account page.

    Keyword arguments:
    user -- The user object with the information for the log in.
        It must have the email and full_name attributes.

    """
    vlink = mail.get_verification_link_for_address(user.email)
    sst.actions.go_to(vlink)
    validate_email = pages.CompleteEmailAddressValidation()
    validate_email.confirm()


def sign_in(user=None, is_site_recognized=True):
    """Log in with an Ubuntu Single Sign On account.

    The browser must be on the Log in page.
    If the log in succeeds, the browser will be back on the site that
    requested the log in.

    Keyword arguments:
    user -- The user object with the information for the log in.
        It must have the email and password attributes.
        If its value is None, it means that the user has already started a
        session on Ubuntu Single Sign On and it's not necessary to enter the
        credentials again. Default is None.
    is_site_recognized -- Boolean indicating if the site that requested the
        log in is recognized. If it is not recognized, all the user available
        information will be send to it. Default is True.

    """
    if is_site_recognized:
        if user is not None:
            log_in = pages.LogInFromRedirect()
            log_in.log_in_to_site_recognized(user)
        else:
            # User is already signed in so SSO will just redirect back to the
            # main site.
            pass
        _assert_site_not_recognized_page_not_opened()
    else:
        if user is not None:
            log_in = pages.LogInFromRedirect()
            site_not_recognized = log_in.log_in_to_site_not_recognized(user)
        else:
            # User is already signed in so SSO will just show the site not
            # recognized page.
            site_not_recognized = pages.SiteNotRecognized()
        site_not_recognized.make_all_information_available_to_website()
        site_not_recognized.yes_sign_me_in()


def log_out():
    """Log out from the Ubuntu Single Sign On site.

    The browser must be on the Single Sign On site, and the user must have the
    session started there.

    If the log out succeeds, the browser will be on the Ubuntu Single Sign On
    logout page.

    """
    your_account = pages.YourAccount()
    return your_account.subheader.log_out()
