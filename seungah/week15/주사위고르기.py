from itertools import combinations, product

def solution(dice):
    n = len(dice)  
    half = n // 2  
    
    a_combinations = list(combinations(range(n), half))
    
    max_wins = -1
    best_combination = None
    
    for a_comb in a_combinations:
        b_comb = [i for i in range(n) if i not in a_comb]

        wins, draws, losses = 0, 0, 0
        
        for a_roll in product(*(dice[i] for i in a_comb)):
            for b_roll in product(*(dice[i] for i in b_comb)):
                a_sum = sum(a_roll)
                b_sum = sum(b_roll)
                
                if a_sum > b_sum:
                    wins += 1
                elif a_sum == b_sum:
                    draws += 1
                else:
                    losses += 1
        
        if wins > max_wins:
            max_wins = wins
            best_combination = a_comb
    
    
    return sorted([i + 1 for i in best_combination])







from itertools import combinations, product
from collections import Counter


def calculate_histogram(dice_comb):
    """
    주사위 조합에 대해 가능한 모든 합계의 빈도를 계산하는 함수.
    """
    histogram = Counter()
    
    
    for roll in product(*dice_comb):
        histogram[sum(roll)] += 1
    
    return histogram

def solution(dice):
    n = len(dice) 
    half = n // 2 
    
    a_combinations = list(combinations(range(n), half))
    
    max_wins = -1
    best_combination = None
    
    for a_comb in a_combinations:
        b_comb = [i for i in range(n) if i not in a_comb]
        
        a_histogram = calculate_histogram([dice[i] for i in a_comb])
        b_histogram = calculate_histogram([dice[i] for i in b_comb])
        
        wins = 0
        
        for a_sum, a_freq in a_histogram.items():
            for b_sum, b_freq in b_histogram.items():
                if a_sum > b_sum:
                    wins += a_freq * b_freq
        
        if wins > max_wins:
            max_wins = wins
            best_combination = a_comb
    
    return sorted([i + 1 for i in best_combination])
