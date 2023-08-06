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
import re
import urlparse

import sst.actions

from functools import wraps
from urllib2 import unquote


logger = logging.getLogger('User test')


def log_action(log_func):
    """Decorator to log the call of an action method."""

    def middle(f):

        @wraps(f)
        def inner(instance, *args, **kwargs):
            class_name = str(instance.__class__.__name__)
            docstring = f.__doc__
            if docstring:
                docstring = docstring.split('\n')[0].strip()
            else:
                docstring = f.__name__
            log_line = '%r: %r. Arguments %r. Keyword arguments: %r.'
            log_func(log_line, class_name, docstring, args, kwargs)
            return f(instance, *args, **kwargs)

        return inner

    return middle


class Page(object):
    """Base class for the page objects used in acceptance testing.

    Instance variables:
    title -- The title of the page.
    url_path -- The path of the page.
    is_url_path_regex -- If True, the url path will be considered as a regular
        expression.
    headings1 -- A list with the expected text of the h1 elements. If it's
        empty, the h1 elements will not be checked.
    headings2 -- A list with the expected text of the h2 elements. If it's
        empty, the h2 elements will not be checked.
    qa_anchor -- An string with the expected qa id

    """

    title = None
    url_path = None
    is_url_path_regex = False
    headings1 = []
    headings2 = []
    qa_anchor = ''

    def __init__(self, open_page=False):
        super(Page, self).__init__()
        if open_page:
            self._open_page()
        self.assert_page_is_open()

    @log_action(logging.info)
    def _open_page(self):
        """Open the page."""
        if self.is_url_path_regex:
            raise ValueError(
                "We can't open a page with a regular expression on the path.")
        else:
            assert self.url_path is not None
            sst.actions.go_to(self.url_path)
            return self

    def assert_page_is_open(self):
        """Assert that the page is open and that no oops are displayed."""
        try:
            assert not self._is_oops_displayed(), \
                'An oops error is displayed: {0}'.format(
                    self._get_oops_element().text)
            self.assert_url_path()

            # qa_anchor should take precedence
            # since checking for text should be
            # deprecated behaviour
            if self.qa_anchor:
                self.assert_qa_anchor()
            else:
                self.assert_title()
                if self.headings1:
                    self.assert_headings1()
                if self.headings2:
                    self.assert_headings2()
        except AssertionError:
            self._log_errors()
            raise

    def _is_oops_displayed(self):
        try:
            self._get_oops_element()
            return True
        except AssertionError:
            return False

    def _get_oops_element(self):
        # TODO this works for U1. Does it work the same for pay and SSO?
        oops_class = 'yui3-error-visible'
        return sst.actions.get_element(css_class=oops_class)

    def assert_title(self):
        """Assert the title of the page."""
        sst.actions.assert_title(self.title)

    def assert_url_path(self):
        """Assert the path of the page URL."""
        if not self.is_url_path_regex:
            sst.actions.assert_equal(
                self._get_current_url_path(), self.url_path)
        else:
            self._assert_url_path_match()

    def _assert_url_path_match(self):
        # Make sure that there are no more characters at the end of the path.
        url_path_regexp = self.url_path + '$'
        current_url_path = self._get_current_url_path()
        assert re.match(url_path_regexp, current_url_path), \
            "The current URL path {0} doesn't match {1}".format(
                current_url_path, url_path_regexp)

    def _get_current_url_path(self):
        current_url = sst.actions.get_current_url()
        return unquote(urlparse.urlparse(current_url).path)

    def assert_headings1(self):
        """Assert the h1 elements of the page."""
        self._assert_elements_text('h1', self.headings1)

    def _assert_elements_text(self, tag, expected_texts):
        elements_text = self._get_elements_text(tag)
        assert elements_text == expected_texts, \
            'Expected elements texts: {0}\n' \
            'Actual elements texts: {1}'.format(
                ', '.join(expected_texts), ', '.join(elements_text))

    def _get_elements_text(self, tag=None, css_class=None):
        return map(lambda x: x.text, sst.actions.get_elements(
            tag=tag, css_class=css_class))

    def assert_headings2(self):
        """Assert the h2 elements of the page."""
        self._assert_elements_text('h2', self.headings2)

    def assert_qa_anchor(self):
        """Assert the qa anchor."""
        sst.actions.assert_element(
            tag='html', **{'data-qa-id': self.qa_anchor})

    def _log_errors(self):
        if sst.actions.exists_element(css_class='error'):
            logger.error(
                ', '.join(self._get_elements_text(css_class='error')))


class StringHTMLPage(Page):
    """Fake page for testing, with the source in a string attribute."""

    def __init__(self, page_source, url_path, qa_anchor, open_page=False):
        # Do not call the super __init__ because it will assert that the page
        # is open. We will do that manually for the tests that require it.
        self.url_path = url_path
        self.page_source = page_source
        self.qa_anchor = qa_anchor
        self._make_temp_page()
        if open_page:
            self._open_page()

    def _make_temp_page(self):
        with open(self.url_path, 'w') as page_file:
            page_file.write(self.page_source)
