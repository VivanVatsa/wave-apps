class Configuration:
    """
    App Configurations
    """

    def __init__(self):
        self.title = "Shopping Cart Recommendations"
        self.subtitle = "Recommendations based on shopping cart items"
        self.icon = "ShoppingCartSolid"
        self.icon_color = "$yellow"

        self.rule_set = 'data/instacart_market_basket_model.csv'
        self.product_mappings = 'data/instacart_products.csv'

        self.boxes = {
            'header': '1 1 12 1',
            'cart': '1 2 6 5',
            'suggestions': '1 7 6 4',
            'trending': '7 2 6 9',
        }


config = Configuration()
