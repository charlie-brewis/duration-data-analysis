import csv
from datetime import date
from week import Week

class Dataset():
    def __init__(self, file_name: str) -> None:
        '''
        data:
            [
                Week_Data(
                    loc, 
                    date, 
                    gross_ret_sales, 
                    net_ret_sales, 
                    num_stores_selling, 
                    vol_sales, 
                    unit_rate_of_sale, 
                    unit_price, 
                    num_weeks_sold, 
                    closing_stock
                ),
            ]
        '''
        self.data = self.import_csv(file_name)
        self.data = self.sanitise(self.data)

    def import_csv(self, file_name: str) -> list[list[str]]:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            data = [week for week in reader]
        return data
    
    def display(self) -> None:
        for week in self.data:
            print(week)
    
    def sanitise(self, data: list[list[str]]) -> list[list[str]]:
        data.pop(0) # Remove header
        new_data = []
        for row in data:
            new_week = Week(
                location= row[1],
                date= self._convert_date(row[2]),
                gross_retail_sales= float(row[3].removeprefix('Â£')) if row[3] != '' else 0,
                net_retail_sales= float(row[4].removeprefix('Â£')) if row[3] != '' else 0,
                num_stores_selling= int(row[5]) if row[5] != '' else 0,
                volume_sales= int(row[6]) if row[6] != '' else 0,
                unit_rate_of_sale= int(row[7]) if row[7] != '' else 0,
                unit_price= float(row[8].removeprefix('Â£')) if row[8] != '' else 0,
                num_weeks_sold= int(row[9]) if row[9] != '' else 0,
                closing_stock= int(row[10]) if row[10] != '' else 0
            )
            new_data.append(new_week)
        return new_data

    def _convert_date(self, date_str: str) -> date:
        split_date = date_str.split(' ')
        year = int(split_date[3])
        month = self._convert_month(split_date[2])
        day = int(split_date[1])
        return date(year, month, day)

    def _convert_month(self, month: str) -> int:
        match month:
            case 'Jan': return 1
            case 'Feb': return 2
            case 'Mar': return 3
            case 'Apr': return 4
            case 'May': return 5
            case 'Jun': return 6
            case 'Jul': return 7
            case 'Aug': return 8
            case 'Sep': return 9
            case 'Oct': return 10
            case 'Nov': return 11
            case 'Dec': return 12



    def construct_location_dict(self) -> dict[str, list[Week]]:
        '''
        location_dict: 
            {
                'location1': [Week_Data, Week_Data, ...],
                'location2': [Week_Data, Week_Data, ...],
            }
        '''
        location_dict = {}
        for week in self.data:
            if week.location not in location_dict:
                location_dict[week.location] = []
            location_dict[week.location].append(week)
        return location_dict
    
    def avg_field_per_location(self, field: str, export_csv: bool = False) -> dict[str, float]:
        location_dict = self.construct_location_dict()
        average_field = {}
        for location, data in location_dict.items():
            # Calculate the total field for current location
            total_field = 0
            for week in data:
                total_field += week.getField(field)
            # Calculate the average field for current location
            average_field[location] = total_field / len(data)
        
        # Sort the dictionary by values in ascending order
        sorted_average_field = dict(sorted(average_field.items(), key=lambda x: x[1], reverse=True))
        
        if not export_csv:
            return sorted_average_field

        # Export the data to a csv file
        with open(f'average_{field}_per_location.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Location', f'Average {field}'])
            for location, avg in sorted_average_field.items():
                writer.writerow([location, avg])
        
        return sorted_average_field
    
    def full_average_volume_sales(self) -> int:
        total_vol_sales = 0
        for week in self.data:
            total_vol_sales += week.volume_sales
        return total_vol_sales / len(self.data)
    