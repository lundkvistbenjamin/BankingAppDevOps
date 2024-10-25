import pytest
from bank_app import BankApp

@pytest.fixture
def app():
    """Fixture to create a new instance of BankApp before each test."""
    return BankApp()

def test_login_success(app):
    assert app.login('user1', 'pass1') == True
    assert app.login('user2', 'pass2') == True
    assert app.login('user3', 'pass3') == True

def test_login_failure(app):
    assert app.login('user1', 'wrongpass') == False
    assert app.login('unknown_user', 'pass1') == False

def test_get_balance_logged_in(app):
    app.login('user1', 'pass1')
    assert app.get_balance() == 1000

def test_get_balance_not_logged_in(app):
    with pytest.raises(Exception, match="No user logged in"):
        app.get_balance()

def test_get_account_number_logged_in(app):
    app.login('user1', 'pass1')
    assert app.get_account_number() == '111111'

def test_get_account_number_not_logged_in(app):
    with pytest.raises(Exception, match="No user logged in"):
        app.get_account_number()

def test_logout(app):
    app.login('user1', 'pass1')
    app.logout()
    assert app.current_user == None