def read_data(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            country, area, population = line.strip().split(',')
            data.append({
                'country': country.strip(),
                'area': float(area.strip()),
                'population': int(population.strip())
            })
    return data

def sort_by_area(data):
    return sorted(data, key=lambda x: x['area'], reverse=True)

def sort_by_population(data):
    return sorted(data, key=lambda x: x['population'], reverse=True)