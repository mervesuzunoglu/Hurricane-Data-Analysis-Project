# Hurricane Data Analysis
# This script contains functions to analyze the data of 34 strongest Atlantic hurricanes.
# Each function performs a specific task related to organizing, analyzing, and categorizing hurricane data.

# Hurricane data
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# Function 1: Update Damages
def convert_damages(damage_list):
    """Convert damages into numerical values, keeping 'Damages not recorded' intact."""
    updated_damages = []
    for damage in damage_list:
        if damage == "Damages not recorded":
            updated_damages.append(damage)
        elif 'M' in damage:
            updated_damages.append(float(damage[:-1]) * 1e6)
        elif 'B' in damage:
            updated_damages.append(float(damage[:-1]) * 1e9)
    return updated_damages

# Function 2: Create hurricane dictionary
def create_hurricane_dict(names, months, years, max_winds, areas, damages, deaths):
    """Create a dictionary of hurricanes with the hurricane name as the key and all details as values."""
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_winds[i],
            "Areas Affected": areas[i],
            "Damage": damages[i],
            "Deaths": deaths[i]
        }
    return hurricanes

# Function 3: Organize hurricanes by year
def hurricanes_by_year(hurricane_dict):
    """Organize hurricanes into a dictionary by the year they occurred."""
    hurricanes_year = {}
    for cane in hurricane_dict.values():
        year = cane["Year"]
        if year not in hurricanes_year:
            hurricanes_year[year] = []
        hurricanes_year[year].append(cane)
    return hurricanes_year

# Function 4: Count areas affected
def count_affected_areas(hurricane_dict):
    """Count the number of times each area was affected by a hurricane."""
    affected_count = {}
    for cane in hurricane_dict.values():
        for area in cane["Areas Affected"]:
            if area not in affected_count:
                affected_count[area] = 1
            else:
                affected_count[area] += 1
    return affected_count

# Function 5: Find area affected by the most hurricanes
def most_affected_area(affected_count):
    """Find the area affected by the most hurricanes."""
    max_area = ""
    max_count = 0
    for area, count in affected_count.items():
        if count > max_count:
            max_area = area
            max_count = count
    return max_area, max_count

# Function 6: Find the most deadly hurricane
def most_deadly_hurricane(hurricane_dict):
    """Find the hurricane that caused the most deaths."""
    max_mortality = 0
    deadliest_hurricane = ""
    for cane in hurricane_dict.values():
        if cane["Deaths"] > max_mortality:
            max_mortality = cane["Deaths"]
            deadliest_hurricane = cane["Name"]
    return deadliest_hurricane, max_mortality

# Function 7: Rate hurricanes by mortality
def rate_by_mortality(hurricane_dict):
    """Rate hurricanes by the number of deaths they caused."""
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000, 5: float('inf')}
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    
    # Iterate through each hurricane and categorize it based on mortality scale
    for cane in hurricane_dict.values():
        deaths = cane["Deaths"]
        for scale, upper_bound in mortality_scale.items():
            if deaths <= upper_bound:
                hurricanes_by_mortality[scale].append(cane)
                break
    return hurricanes_by_mortality

# Function 8: Find the hurricane that caused the greatest damage
def most_costly_hurricane(hurricane_dict):
    """Find the hurricane that caused the most damage."""
    max_damage = 0
    costly_hurricane = ""
    
    for cane in hurricane_dict.values():
        damage = cane["Damage"]
        if damage == "Damages not recorded":
            continue
        if damage > max_damage:
            max_damage = damage
            costly_hurricane = cane["Name"]
    return costly_hurricane, max_damage

# Function 9: Rate hurricanes by damage
def rate_by_damage(hurricane_dict):
    """Rate hurricanes by the damage they caused."""
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000, 5: float('inf')}
    hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    
    # Iterate through each hurricane and categorize it based on the damage scale
    for cane in hurricane_dict.values():
        damage = cane["Damage"]
        if damage == "Damages not recorded":
            hurricanes_by_damage[0].append(cane)  # If no damages recorded, put in category 0
        else:
            for scale, upper_bound in damage_scale.items():
                if damage <= upper_bound:
                    hurricanes_by_damage[scale].append(cane)
                    break
    return hurricanes_by_damage

# Function calls to test the script and display the results

# 1. Update damages
updated_damages = convert_damages(damages)
print(updated_damages)

# 2. Create hurricane dictionary
hurricanes = create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes)

# 3. Organize hurricanes by year
hurricanes_by_years = hurricanes_by_year(hurricanes)
print(hurricanes_by_years)

# 4. Count affected areas
affected_areas_count = count_affected_areas(hurricanes)
print(affected_areas_count)

# 5. Find the area most affected by hurricanes
most_affected = most_affected_area(affected_areas_count)
print(f"The area most affected by hurricanes is {most_affected[0]} with {most_affected[1]} occurrences.")

# 6. Find the most deadly hurricane
deadliest_hurricane = most_deadly_hurricane(hurricanes)
print(f"The most deadly hurricane is {deadliest_hurricane[0]} with {deadliest_hurricane[1]} deaths.")

# 7. Rate hurricanes by mortality
hurricanes_by_mortality = rate_by_mortality(hurricanes)
print(f"Hurricanes categorized by mortality ratings:\n{hurricanes_by_mortality}")

# 8. Find the most costly hurricane
most_costly = most_costly_hurricane(hurricanes)
print(f"The most costly hurricane is: {most_costly[0]} with damages amounting to ${most_costly[1]}.")

# 9. Rate hurricanes by damage
hurricanes_by_damage = rate_by_damage(hurricanes)
print(f"Hurricanes categorized by damage ratings:\n{hurricanes_by_damage}")
