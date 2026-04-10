def read_data(file_path):
    """Зчитує дані з файлу та повертає список словників."""
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
        """Сортує список країн за площею за спаданням (від найбільшої)."""
        return sorted(data, key=lambda x: x['area'], reverse=True)