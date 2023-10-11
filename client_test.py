import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_ifPriceBEqualsZero(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771',
             'stock': 'ABC'},
            {'top_ask': {'price': 0.00, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0.00, 'size': 81}, 'id': '0.109974697771',
             'stock': 'DEF'}
        ]

        stockA, bid_priceA, ask_priceA, priceA = getDataPoint(quotes[0])
        stockB, bid_priceB, ask_priceB, priceB = getDataPoint(quotes[1])
        self.assertEqual(getRatio(priceA, priceB), None)

    def test_getRatio_ifPriceAEqualsZero(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 0.00, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0.00, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        stockA, bid_priceA, ask_priceA, priceA = getDataPoint(quotes[1])
        stockB, bid_priceB, ask_priceB, priceB = getDataPoint(quotes[0])
        self.assertEqual(getRatio(priceA, priceB), 0)


if __name__ == '__main__':
    unittest.main()
