def players_to_get_shot(T, test_cases):
    results = []
    for _ in range(T):
        N, K = test_cases[_][0], test_cases[_][1]
        heights = test_cases[_][2]
        
        min_players_shot = 0
        for height in reversed(heights): 
            if height >= K:
                min_players_shot += 1
            else:
                break  
        results.append(min_players_shot)
    
    return results

T = 3
test_cases = [
    (5, 170, [180, 160, 165, 175, 155]),
    (4, 160, [170, 180, 150, 155]),
    (6, 180, [185, 190, 170, 175, 165, 160])
]
results = players_to_get_shot(T, test_cases)
for result in results:
    print(result)