def calc_avg(numbers: list[float]):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def fmt_fio(parts: list[str], capitalize: bool = True):
    fio = " ".join(parts)
    
    if capitalize:
        return fio.title()
    
    return fio


def filter_scores(data_dict: dict[str, float], min_value: float):
  
    result = {}
    
    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value
    
    return result

if __name__ == "__main__":
    print(" Функция calc_avg")
    print(calc_avg([10, 20, 30, 40]))  
    print(calc_avg([5, 15, 25]))      
    print(calc_avg([]))               
    
    print("\n Функция fmt_fio")
    print(fmt_fio(['иванов', 'иван', 'сергеевич']))
    print(fmt_fio(['сидорова', 'анна', 'валерьевна'], capitalize=False))
    print(fmt_fio(['петров', 'петр', 'петрович'], capitalize=True))
    
    print("\n Функция filter_scores")
    scores = {"math": 95, "history": 78, "english": 88, "art": 92}
    print(filter_scores(scores, 90))   
    print(filter_scores(scores, 80))   
    print(filter_scores(scores, 100))  