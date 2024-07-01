from check_mail import CheckMail

myMailChecker = CheckMail()
myMailChecker.isValidMailAddress("a@test.e")
def test_class_CheckMail():
    myMailChecker = CheckMail()
    assert isinstance(myMailChecker, CheckMail)

def test_class_CheckMail_no_input():
    myMailChecker = CheckMail()
    assert not myMailChecker.isValidMailAddress(None)
    address = ""
    assert not myMailChecker.isValidMailAddress(address)

def test_class_CheckMail_correct_input():
    myMailChecker = CheckMail()
    assert myMailChecker.isValidMailAddress("jonas@test.abc.de")

def test_class_CheckMail_check_for_ats():
    myMailChecker = CheckMail()
    assert not myMailChecker.isValidMailAddress("jonastest.de")
    assert not myMailChecker.isValidMailAddress("jon@s@test.de")

def test_class_CheckMail_check_text_before_at():
    myMailChecker = CheckMail()
    assert not myMailChecker.isValidMailAddress("@jonastest.de")
    assert myMailChecker.isValidMailAddress("a@test.de")

def test_class_CheckMail_check_for_dot():
    myMailChecker = CheckMail()
    assert not myMailChecker.isValidMailAddress("jonas@testde")
    assert not myMailChecker.isValidMailAddress("a@test.e")