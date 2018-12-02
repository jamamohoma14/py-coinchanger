from coinchanger.coinchanger import CoinChanger
cc = CoinChanger()

penny = {
    "value": 1
}

nickel = {
    "value": 5
}

dime = {
    "value": 10
}

quarter = {
    "value": 25
}

dollar = {
    "value": 100
}

def test_one_penny():
    assert cc.make_change(1) == [penny]

def test_two_pennies():
    assert cc.make_change(2) == [penny, penny]

def test_six_cents():
    assert cc.make_change(6) ==[nickel, penny]

def test_seventeen_cents():
    assert cc.make_change(17) == [dime, nickel, penny, penny]

def test_fourty_nine_cents():
    assert cc.make_change(49) == [quarter, dime, dime, penny, penny, penny, penny]

def test_one_dollar_eightteen_cents():
    assert cc.make_change(118) == [dollar, dime, nickel, penny, penny, penny]


