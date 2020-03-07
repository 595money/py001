from pm.dao.framework.Factory import Factory
from pm.dao.implement.EtoroDAOImpl import EtoroDAOImpl
from pm.dao.implement.PortfolioDAOImpl import PortfolioDAOImpl
from pm.dao.implement.FundDAOImpl import FundDAOImpl

class DAOFactory(Factory):
    products = {
        "etoro": EtoroDAOImpl,
        "portfolio": PortfolioDAOImpl,
        "fund": FundDAOImpl,
        "other": None
    }

    def create_product(self, product_name):
        return self.products[product_name]()

def main():
    p = DAOFactory().create_product('etoro')
    p.test()
if __name__ == '__main__':
    main()
    main()