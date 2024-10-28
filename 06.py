def print_result(algo, result, total_cost, total_calories):
    print(f"{algo} алгоритм - обрані страви:")
    for item, data in result.items():
        print(f"{item}: Вартість = {data['cost']}, Калорійність = {data['calories']}")
    print(f"Загальна вартість: {total_cost}")
    print(f"Загальна калорійність: {total_calories}\n")


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = {}
    total_cost = 0
    total_calories = 0
    
    for item, data in sorted_items:
        cost = data['cost']
        calories = data['calories']
        
        if total_cost + cost <= budget:
            selected_items[item] = data
            total_cost += cost
            total_calories += calories
    
    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    item_selection = [{} for _ in range(budget + 1)]

    for item, data in items.items():
        cost = data['cost']
        calories = data['calories']
        
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget] < dp[current_budget - cost] + calories:
                dp[current_budget] = dp[current_budget - cost] + calories
                item_selection[current_budget] = item_selection[current_budget - cost].copy()
                item_selection[current_budget][item] = data

    selected_items = item_selection[budget]
    total_calories = dp[budget]
    total_cost = sum(item['cost'] for item in selected_items.values())
    
    return selected_items, total_cost, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

result, total_cost, total_calories = greedy_algorithm(items, budget)
print_result("Жадібний", result, total_cost, total_calories)

result, total_cost, total_calories = dynamic_programming(items, budget)
print_result("Динамічний", result, total_cost, total_calories)