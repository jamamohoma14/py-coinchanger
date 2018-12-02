penny = {'value': 1}
nickel = {'value': 5}
dime = {'value': 10}
quarter = {'value': 25}
dollar = {'value': 100}

class CoinChanger():



    def make_change(self, p):
        current_pouch = []
        coins = [dollar, quarter, dime, nickel, penny]

        for coin in coins:
            (p, current_pouch) = self.find_coins(coin, p, current_pouch)


        return current_pouch


    def find_coins(self, coin, amount_left, coin_list):
        if coin['value'] <= amount_left:
            while coin['value'] <= amount_left:
                coin_list.append(coin)
                amount_left -= coin['value']

        return (amount_left, coin_list)
