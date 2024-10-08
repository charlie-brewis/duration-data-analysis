from week import Week
from dataset import Dataset


def get_all_public_methods(obj: object) -> list[str]:
    return [func for func in dir(obj) if callable(getattr(obj, func)) and not func.startswith("_Dataset__") and not func.startswith("__")]


def main() -> None:
    dataObj = Dataset('input/data.csv')

    print(get_all_public_methods(dataObj))
    
    print(f"Average volume sales across whole dataset: {dataObj.full_average_volume_sales()}")


    # dataObj.avg_field_per_location('volume_sales', True)
    # dataObj.avg_field_per_location('net_retail_sales', True)

if __name__ == '__main__':
    main()