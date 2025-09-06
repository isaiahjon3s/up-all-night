import re

def main():
    year = int(input("Enter the year: "))
    if validate_year(year):
        print(iphone(year))
    else:
        print("Invalid year")
    
def validate_year(year):
    # Validates years from 2007 to 2025
    if re.match(r"^20(?:0[7-9]|1\d|2[0-5])$", str(year)):
        return True
    return False

def iphone(year:str):
    iphone_models = {
        "2007": "iPhone 1",
        "2008": "iPhone 3G", 
        "2009": "iPhone 3GS",
        "2010": "iPhone 4",
        "2011": "iPhone 4S",
        "2012": "iPhone 5",
        "2013": "iPhone 5S",
        "2014": "iPhone 6",
        "2015": "iPhone 6S",
        "2016": "iPhone 7",
        "2017": "iPhone 8",
        "2018": "iPhone X",
        "2019": "iPhone 11",
        "2020": "iPhone 12",
        "2021": "iPhone 13",
        "2022": "iPhone 14",
        "2023": "iPhone 15",
        "2024": "iPhone 16",
        "2025": "iPhone 17"
    }
    return iphone_models.get(str(year), "iPhone infinity")

if __name__ == "__main__":
    main()