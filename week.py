from datetime import date

class Week():
    # Omit product name as it is consistent accross the whole dataset
    def __init__(self,
                 location: str,
                 date: date,
                 gross_retail_sales: float,
                 net_retail_sales: float,
                 num_stores_selling: int,
                 volume_sales: int,
                 unit_rate_of_sale: int,
                 unit_price: float,
                 num_weeks_sold: int,
                 closing_stock: int) -> None:
        self.location = location
        self.date = date
        self.gross_retail_sales = gross_retail_sales
        self.net_retail_sales = net_retail_sales
        self.num_stores_selling = num_stores_selling
        self.volume_sales = volume_sales
        self.unit_rate_of_sale = unit_rate_of_sale
        self.unit_price = unit_price
        self.num_weeks_sold = num_weeks_sold
        self.closing_stock = closing_stock

    def get_field(self, field: str) -> str | date | float | int:
        match field:
            case 'location': return self.location
            case 'date': return self.date
            case 'gross_retail_sales': return self.gross_retail_sales
            case 'net_retail_sales': return self.net_retail_sales
            case 'num_stores_selling': return self.num_stores_selling
            case 'volume_sales': return self.volume_sales
            case 'unit_rate_of_sale': return self.unit_rate_of_sale
            case 'unit_price': return self.unit_price
            case 'num_weeks_sold': return self.num_weeks_sold
            case 'closing_stock': return self.closing_stock
            case _ : raise Exception(f"Field {field} not found")
            

    def __str__(self) -> str:
        return f"Week_Data({self.location}, {self.date}, £{self.gross_retail_sales}, £{self.net_retail_sales}, {self.num_stores_selling}, {self.volume_sales}, {self.unit_rate_of_sale}, £{self.unit_price}, {self.num_weeks_sold}, {self.closing_stock})"
