# Copyright 2013 Canonical Ltd.
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

import u1testutils.sst

from u1testutils.sst import log_action


logger = logging.getLogger('User test')


class LogIn(u1testutils.sst.Page):
    """Log in page of the Ubuntu Single Sign On website.

    This is a subclass of the PageWithAnonymousSubheader object to add
    methods for the actions available in this page.

    """

    url_path = '(/|/\+login)'
    is_url_path_regex = True
    qa_anchor = 'login'

    @log_action(logging.info)
    def _open_page(self):
        """Open the page.

        This overwrites the method from the base Page class in order to choose
        one of the possible URL paths to open the page.

        """
        sst.actions.go_to('/+login')
        return self

    @log_action(logging.info)
    def log_in_to_site_recognized(self, user=None):
        """Fill the log in form and continue to the site that requested it.

        Keyword arguments:
        user -- The user credentials. It must have the attributes email and
            password. If None is passed as the user, it means that the user
            has already started session on the identity provider and it's not
            necessary to enter the credentials again.

        """
        self._log_in(user)

    @log_action(logging.info)
    def log_in_to_site_not_recognized(self, user=None):
        """Fill the log in form and continue to the next step.

        As the site is not recognized, the next step is the page where the
        user can select the information that will be send to the site.

        Keyword arguments:
        user -- The user credentials. It must have the attributes email and
            password. If None is passed as the user, it means that the user
            has already started session on the identity provider and it's not
            necessary to enter the credentials again.

        """
        self._log_in(user)
        return SiteNotRecognized()

    def _log_in(self, user=None):
        if user is not None:
            sst.actions.wait_for(sst.actions.assert_title, 'Log in')
            self._fill_log_in_form(user.email, user.password)
            self._click_continue_button()
        else:
            # If None is passed as the user, it means that the user has
            # already started session on the identity provider and it's not
            # necessary to enter the credentials again.
            pass

    def _fill_log_in_form(self, email, password):
        email_field = sst.actions.get_element_by_css(
            '*[data-qa-id="login_form"] #id_email')
        sst.actions.write_textfield(email_field, email)
        password_field = sst.actions.get_element_by_css(
            '*[data-qa-id="login_form"] #id_password')
        sst.actions.write_textfield(password_field, password)

    def _click_continue_button(self):
        continue_button = sst.actions.get_element_by_css(
            '*[data-qa-id="login_button"]')
        sst.actions.click_button(continue_button)

    @log_action(logging.info)
    def go_to_create_new_account(self):
        """Go to the Create new account page."""
        self._click_create_new_account()
        return self._new_create_account_page()

    def _click_create_new_account(self):
        link = sst.actions.get_element_by_css(
            '*[data-qa-id="create_account_link"]')
        sst.actions.click_link(link)

    def _new_create_account_page(self):
        # override in children
        return CreateAccount()


class LogInFromRedirect(LogIn):

    url_path = '/.*/\+decide'
    is_url_path_regex = True

    @log_action(logging.info)
    def go_to_create_new_account(self):
        """Go to the Create new account page."""
        self._click_create_new_account()
        return CreateAccountFromRedirect()


class PageWithAnonymousSubheader(u1testutils.sst.Page):

    def __init__(self, open_page=False):
        super(PageWithAnonymousSubheader, self).__init__(open_page)
        self.subheader = _AnonymousSubheader()


class _AnonymousSubheader(object):

    @log_action(logging.info)
    def go_to_log_in_or_create_account(self):
        link = sst.actions.get_element_by_css('*[data-qa-id="login_link"]')
        sst.actions.click_link(link)
        return LogIn()


class CreateAccount(PageWithAnonymousSubheader):
    """Create account page of the Ubuntu Single Sign On website.

    This is a subclass of the PageWithAnonymousSubheader object to add
    methods for the actions available in this page.

    """

    url_path = '/+new_account'
    qa_anchor = 'new_account'

    @log_action(logging.info)
    def create_ubuntu_sso_account(self, user):
        """Fill the new account form and continue to the next step.

        Keyword arguments:
        user -- The user credentials. It must have the attributes email and
            password.

        """
        self._fill_new_account_form(user)
        self._click_continue()

    def _fill_new_account_form(self, user, password_confirmation=None):
        if password_confirmation is None:
            password_confirmation = user.password
        sst.actions.write_textfield('id_displayname', user.full_name)
        email_field = sst.actions.get_element_by_css(
            '*[data-qa-id="create_account_form"] #id_email')
        sst.actions.write_textfield(email_field, user.email)
        password_field = sst.actions.get_element_by_css(
            '*[data-qa-id="create_account_form"] #id_password')
        sst.actions.write_textfield(password_field, user.password)
        sst.actions.write_textfield(
            'id_passwordconfirm', password_confirmation)

        captcha_field = 'recaptcha_response_field'
        if sst.actions.exists_element(id=captcha_field):
            sst.actions.write_textfield(captcha_field, 'ignored')

        tos_field = 'id_accept_tos'
        if sst.actions.exists_element(id=tos_field):
            sst.actions.set_checkbox_value(tos_field, True)

    def _click_continue(self):
        continue_button = sst.actions.get_element_by_css(
            '*[data-qa-id="register_button"]')
        sst.actions.click_button(continue_button)


class CreateAccountFromRedirect(CreateAccount):

    url_path = '/.*/\+new_account'
    is_url_path_regex = True


class UnifiedLogInCreateAccount(LogIn, CreateAccount):
    """Log in or create account, unified experience."""

    url_path = LogIn.url_path
    is_url_path_regex = LogIn.is_url_path_regex
    qa_anchor = 'login'

    def _click_create_new_account(self):
        new_user_intention = sst.actions.get_element_by_css(
            '*[data-qa-id="user_intention_create"]')
        sst.actions.click_element(new_user_intention)

    def _new_create_account_page(self):
        return self


class UnifiedLogInCreateAccountFromRedirect(UnifiedLogInCreateAccount):

    url_path = '/.*/\+decide'
    is_url_path_regex = True


class AccountCreationMailSent(PageWithAnonymousSubheader):
    """AccountCreation mail sent page of the Ubuntu Single Sign On website.

    This is a subclass of the PageWithAnonymousSubheader object to add methods
    for the actions available in this page.

    """

    url_path = '/+new_account'
    qa_anchor = 'new_account'

    @log_action(logging.info)
    def confirm_email_to_site_recognized(self, confirmation_code):
        """Confirm email and continue to the site that requested the log in.

        Keyword arguments:
        confirmation_code -- The confirmation code sent to the user email
            address.

        """
        self._confirm_email(confirmation_code)

    @log_action(logging.info)
    def confirm_email_to_site_not_recognized(self, confirmation_code):
        """Enter the confirmation code and continue to the next step.

        As the site is not recognized, the next step is the page where the
        user can select the information that will be send to the site.

        Keyword arguments:
        confirmation_code -- The confirmation code sent to the user email
            address.

        """
        self._confirm_email(confirmation_code)
        return SiteNotRecognized()

    def _confirm_email(self, confirmation_code):
        self._enter_confirmation_code(confirmation_code)
        self._click_continue_button()

    def _enter_confirmation_code(self, confirmation_code):
        confirmation_code_text_field = sst.actions.get_element(
            name='confirmation_code')
        sst.actions.write_textfield(confirmation_code_text_field,
                                    confirmation_code)

    def _click_continue_button(self):
        continue_button = sst.actions.get_element_by_css(
            '*[data-qa-id="complete_account_creation"]')
        sst.actions.click_button(continue_button)


class PageWithUserSubheader(u1testutils.sst.Page):

    def __init__(self, open_page=False):
        # Some pages will need to take the user name from the subheader in
        # order to assert that they are open. We need the subheader before
        # that check.
        self.subheader = UserSubheader()
        super(PageWithUserSubheader, self).__init__(open_page)


class UserSubheader(object):

    @log_action(logging.info)
    def log_out(self):
        """Log out from the web site."""
        link = sst.actions.get_element_by_css('*[data-qa-id="logout_link"]')
        sst.actions.click_link(link)
        return YouHaveBeenLoggedOut()

    def get_user_name(self):
        return sst.actions.get_element_by_css('*[data-qa-id="user_name"]').text


class CompleteEmailValidation(PageWithUserSubheader):
    """Complete email address validation page.

    This is a subclass of the Page object. It adds methods for the actions
    available in this page.

    """

    url_path = '/token/.+/\+newemail/.+@.+'
    is_url_path_regex = True
    qa_anchor = 'confirm_email'

    def __init__(self, open_page=False):
        super(CompleteEmailValidation, self).__init__(open_page)

    def _click_continue_button(self):
        continue_button = sst.actions.get_element_by_css(
            '*[data-qa-id="confirm_email_validation"]')
        sst.actions.click_button(continue_button)

    def _click_cancel(self):
        cancel_link = sst.actions.get_element_by_css(
            '*[data-qa-id="cancel_email_validation"]')
        sst.actions.click_link(cancel_link)

    @log_action(logging.info)
    def confirm(self):
        self._click_continue_button()
        return YourAccount()

    @log_action(logging.info)
    def cancel(self):
        return YourAccount()


class SiteNotRecognized(u1testutils.sst.Page):
    """Site not Recognized page of the Ubuntu Single Sign On website.

    This is a subclass of the Page object. It overrides the assert_title
    method to check only the first part of the title, and adds methods for the
    actions available in this page.

    """

    url_path = '/.+/\+decide'
    is_url_path_regex = True
    qa_anchor = 'decide'

    def assert_title(self):
        """Assert that the page is open.

        We use a regular expression because the title has the URL of the site
        that requested the log in plus some tokens, and we don't need to check
        that.

        """
        sst.actions.assert_title_contains(self.title, regex=True)

    @log_action(logging.info)
    def make_all_information_available_to_website(self):
        """Select all the user available information.

        This information will be send to the site that requested the log in.

        """
        information_checkboxes = self._get_information_checkboxes()
        for checkbox in information_checkboxes:
            if checkbox.is_displayed():
                sst.actions.set_checkbox_value(checkbox, True)
        return self

    def _get_information_checkboxes(self):
        return sst.actions.wait_for(
            sst.actions.get_elements_by_css,
            '*[data-qa-id="info-items"] input[type="checkbox"]')

    @log_action(logging.info)
    def yes_sign_me_in(self):
        """Accept to sign in to the site not recognized and go back to it."""
        sign_me_in_button = sst.actions.get_element_by_css(
            '*[data-qa-id="rp_confirm_login"]')
        sst.actions.click_button(sign_me_in_button)


class YourAccount(PageWithUserSubheader):
    """Your account page of the Ubuntu Single Sign On website.

    This is a subclass of the Page object. It extends the constructor to
    to receive the user name, and adds methods for the actions available in
    this page.

    Instance variables:
    title -- The title of the page. It's build when the page is instantiated
        using the user name.

    """

    url_path = '/'
    qa_anchor = 'edit_account'

    def __init__(self, open_page=False):
        super(YourAccount, self).__init__(open_page)


class YouHaveBeenLoggedOut(PageWithAnonymousSubheader):
    """Your account page of the Ubuntu Single Sign On website."""

    url_path = '/+logout'
    qa_anchor = 'logout'
