from resources.messages import Messages

def test_check_login_failed(github_ui_client, fake_user):
    github_ui_client.login(fake_user)

    assert github_ui_client.get_validation_error() == Messages.InvalidCredentials
