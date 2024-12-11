def get_stones():
    with open('input.txt') as f:
        return [int(x.strip()) for x in f.readline().split(' ')]

score_cache = {}

def score(number, blinks_remaining):
    if blinks_remaining == 0:
        return 1

    if (number, blinks_remaining) in score_cache:
        return score_cache[(number, blinks_remaining)]

    if number == 0:
        s = score(1, blinks_remaining - 1)
    else:
        number_string = str(number)
        len_number_string = len(number_string)
        if (len_number_string % 2) == 0:
            s = (score(int(number_string[:len_number_string // 2]), blinks_remaining - 1)
                 + score(int(number_string[len_number_string // 2:]), blinks_remaining - 1))
        else:
            s = score(number * 2024, blinks_remaining - 1)

    score_cache[(number, blinks_remaining)] = s
    return s

the_stones = get_stones()
stone_len = 0
for j in range(len(the_stones)):
    stone_len += score(the_stones[j], 75)
print("Total stones:", stone_len)