#Christopher Savage
import csv
from typing import List, Tuple, Dict

def load_life_expectancy_data(filename: str) -> List[List[str]]:
    """
    Load the life expectancy data from a CSV file.
    
    Args:
        filename (str): Path to the CSV file
    
    Returns:
        List[List[str]]: A list of lists containing the CSV data
    """
    life_expectancy_data = []
    
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            # Skip the header line
            next(csv_reader)
            
            # Read and process each line
            for row in csv_reader:
                life_expectancy_data.append(row)
        
        return life_expectancy_data
    
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def find_overall_extreme_life_expectancies(data: List[List[str]]) -> Tuple[float, str, int, float, str, int]:
    """
    Find the lowest and highest life expectancy values in the entire dataset.
    
    Args:
        data (List[List[str]]): List of lists containing life expectancy data
    
    Returns:
        Tuple containing (lowest_value, lowest_country, lowest_year, 
                          highest_value, highest_country, highest_year)
    """
    lowest_life_expectancy = float('inf')
    highest_life_expectancy = float('-inf')
    lowest_country = ""
    highest_country = ""
    lowest_year = 0
    highest_year = 0

    for row in data:
        try:
            # Ensure row has enough elements
            if len(row) >= 4:
                # Parse life expectancy and year
                life_expectancy = float(row[3])
                year = int(row[2])
                country = row[0]
                
                # Update lowest life expectancy
                if life_expectancy < lowest_life_expectancy:
                    lowest_life_expectancy = life_expectancy
                    lowest_country = country
                    lowest_year = year
                
                # Update highest life expectancy
                if life_expectancy > highest_life_expectancy:
                    highest_life_expectancy = life_expectancy
                    highest_country = country
                    highest_year = year
        
        except (ValueError, IndexError):
            # Skip rows with invalid data
            continue
    
    return (lowest_life_expectancy, lowest_country, lowest_year, 
            highest_life_expectancy, highest_country, highest_year)

def analyze_year(data: List[List[str]], target_year: int) -> Tuple[float, float, str, float, str]:
    """
    Analyze life expectancy for a specific year.
    
    Args:
        data (List[List[str]]): List of lists containing life expectancy data
        target_year (int): Year to analyze
    
    Returns:
        Tuple containing (average_life_expectancy, max_life_expectancy, 
                          max_country, min_life_expectancy, min_country)
    """
    year_data = []
    
    for row in data:
        try:
            # Ensure row has enough elements
            if len(row) >= 4:
                # Parse year and life expectancy
                year = int(row[2])
                if year == target_year:
                    life_expectancy = float(row[3])
                    country = row[0]
                    year_data.append((life_expectancy, country))
        
        except (ValueError, IndexError):
            # Skip rows with invalid data
            continue
    
    if not year_data:
        return 0, 0, "", 0, ""
    
    # Calculate average
    average_life_expectancy = sum(le for le, _ in year_data) / len(year_data)
    
    # Find max and min
    max_life_expectancy = max(year_data, key=lambda x: x[0])
    min_life_expectancy = min(year_data, key=lambda x: x[0])
    
    return (average_life_expectancy, 
            max_life_expectancy[0], max_life_expectancy[1],
            min_life_expectancy[0], min_life_expectancy[1])

def analyze_country(data: List[List[str]], target_country: str) -> Tuple[float, float, float, int, int]:
    """
    Analyze life expectancy for a specific country.
    
    Args:
        data (List[List[str]]): List of lists containing life expectancy data
        target_country (str): Country to analyze
    
    Returns:
        Tuple containing (min_life_expectancy, max_life_expectancy, 
                          avg_life_expectancy, min_year, max_year)
    """
    country_data = []
    
    for row in data:
        try:
            # Ensure row has enough elements
            if len(row) >= 4:
                # Parse country and life expectancy
                country = row[0]
                if country.lower() == target_country.lower():
                    year = int(row[2])
                    life_expectancy = float(row[3])
                    country_data.append((life_expectancy, year))
        
        except (ValueError, IndexError):
            # Skip rows with invalid data
            continue
    
    if not country_data:
        return 0, 0, 0, 0, 0
    
    # Find min and max life expectancy
    min_life_expectancy = min(country_data, key=lambda x: x[0])
    max_life_expectancy = max(country_data, key=lambda x: x[0])
    
    # Calculate average
    avg_life_expectancy = sum(le for le, _ in country_data) / len(country_data)
    
    return (min_life_expectancy[0], max_life_expectancy[0], 
            avg_life_expectancy, min_life_expectancy[1], max_life_expectancy[1])

def find_largest_life_expectancy_drop(data: List[List[str]]) -> Tuple[str, int, float, float]:
    """
    Find the country with the largest drop in life expectancy from one year to the next.
    
    Args:
        data (List[List[str]]): List of lists containing life expectancy data
    
    Returns:
        Tuple containing (country, year, previous_life_expectancy, dropped_life_expectancy)
    """
    # Group data by country and sort by year
    country_data = {}
    for row in data:
        try:
            country = row[0]
            year = int(row[2])
            life_expectancy = float(row[3])
            
            if country not in country_data:
                country_data[country] = []
            
            country_data[country].append((year, life_expectancy))
        except (ValueError, IndexError):
            continue
    
    # Track largest drop
    largest_drop = 0
    largest_drop_country = ""
    largest_drop_year = 0
    largest_drop_previous = 0
    largest_drop_current = 0
    
    # Check each country's life expectancy year by year
    for country, yearly_data in country_data.items():
        # Sort data by year
        yearly_data.sort(key=lambda x: x[0])
        
        # Check for largest drop
        for i in range(1, len(yearly_data)):
            drop = yearly_data[i-1][1] - yearly_data[i][1]
            
            if drop > largest_drop:
                largest_drop = drop
                largest_drop_country = country
                largest_drop_year = yearly_data[i][0]
                largest_drop_previous = yearly_data[i-1][1]
                largest_drop_current = yearly_data[i][1]
    
    return (largest_drop_country, largest_drop_year, 
            largest_drop_previous, largest_drop_current)

def main():
    # File path for the life expectancy dataset
    filename = 'life-expectancy.csv'
    
    # Load the data
    life_expectancy_data = load_life_expectancy_data(filename)
    
    if not life_expectancy_data:
        print("No data could be loaded. Exiting.")
        return
    
    # Find overall extreme life expectancies
    (lowest_value, lowest_country, lowest_year, 
     highest_value, highest_country, highest_year) = find_overall_extreme_life_expectancies(life_expectancy_data)
    
    # Print overall extreme life expectancies
    print("\n--- Overall Life Expectancy Analysis ---")
    print(f"Overall lowest life expectancy: {lowest_value:.3f} years")
    print(f"   Country: {lowest_country}")
    print(f"   Year: {lowest_year}")
    print(f"Overall highest life expectancy: {highest_value:.3f} years")
    print(f"   Country: {highest_country}")
    print(f"   Year: {highest_year}")
    
    # Interactive menu
    while True:
        print("\n Life expectancy database")
        print("1. Analyze a specific year")
        print("2. Analyze a specific country")
        print("3. Find largest life expectancy drop")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            # Year analysis
            try:
                year = int(input("Enter the year of interest: "))
                
                # Analyze the specific year
                (avg_life_exp, max_life_exp, max_country, 
                 min_life_exp, min_country) = analyze_year(life_expectancy_data, year)
                
                print(f"\nFor the year {year}:")
                print(f"Average life expectancy: {avg_life_exp:.3f} years")
                print(f"Highest life expectancy: {max_life_exp:.3f} years in {max_country}")
                print(f"Lowest life expectancy: {min_life_exp:.3f} years in {min_country}")
            
            except ValueError:
                print("Invalid year. Please enter a valid number.")
        
        elif choice == '2':
            # Country analysis
            country = input("Enter the country name: ").strip()
            
            # Analyze the specific country
            (min_life_exp, max_life_exp, avg_life_exp, 
             min_year, max_year) = analyze_country(life_expectancy_data, country)
            
            if min_life_exp > 0:
                print(f"\nLife Expectancy Analysis for {country}:")
                print(f"Minimum life expectancy: {min_life_exp:.3f} years (in {min_year})")
                print(f"Maximum life expectancy: {max_life_exp:.3f} years (in {max_year})")
                print(f"Average life expectancy: {avg_life_exp:.3f} years")
            else:
                print(f"No data found for {country}.")
        
        elif choice == '3':
            # Largest life expectancy drop
            (drop_country, drop_year, prev_life_exp, 
             curr_life_exp) = find_largest_life_expectancy_drop(life_expectancy_data)
            
            print("\nLargest Life Expectancy Drop:")
            print(f"Country: {drop_country}")
            print(f"Year: {drop_year}")
            print(f"Previous year life expectancy: {prev_life_exp:.3f} years")
            print(f"Latest year life expectancy: {curr_life_exp:.3f} years")
            print(f"Drop: {prev_life_exp - curr_life_exp:.3f} years")
        
        elif choice == '4':
            print("Thank you for using the Life Expectancy Data Explorer!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()