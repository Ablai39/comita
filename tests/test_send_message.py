# coding=utf-8
import pytest

from pages.page import Page
from tests.base_test import BaseTest


class TestSearch(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = Page(self.driver, self.wait)
        self.page.go_to_test_page()

    def test_send_message(self, load_pages):
        self.page.login()
        self.page.send_message()
