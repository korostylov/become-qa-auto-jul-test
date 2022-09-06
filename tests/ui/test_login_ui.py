from providers.data.users_provider import UsersProvider


def test_check_login_failed(github_ui_client):
    user = UsersProvider.fake_user()

    github_ui_client.login(user['login'], user['password'])

    assert github_ui_client.login_page.is_login_error() is False

def test_check_navigate_to_forgot_page_from_login_page(github_ui_client):
    user = UsersProvider.fake_user()

    login_page = github_ui_client.login_page
    login_page.login(user['login'], user['password'])
    login_page.navigate()

    forgot_password_page = login_page.proceed_to_forgot_password_page()
    assert forgot_password_page.is_valid()
