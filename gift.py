from two_sum import two_sum

def find_gift_pair(prices, budget):
    result = two_sum(prices, budget)
    if result == [-1]:
        return -1
    return result


print("Подарунковий набір")
p = input("Ціни: ")
p = [int(x) for x in p.split(",")]
b = int(input("Бюджет: "))
print("Відповідь:", find_gift_pair(p, b))