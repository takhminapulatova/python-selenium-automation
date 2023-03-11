from pages.base_page import Page


class SignIn(Page):

    def verify_sign_in_page(self):
        self.verify_url_contains_query('amazon.com/ap/signin')
