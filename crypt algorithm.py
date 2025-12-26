from itertools import permutations

# -------------------------------------------------
# GENERAL SOLVER FUNCTION
# -------------------------------------------------

def solve_cryptarithm(words, result):
    letters = set(''.join(words) + result)
    letters = list(letters)

    if len(letters) > 10:
        print("Too many unique letters!")
        return

    first_letters = set(word[0] for word in words + [result])

    print(f"\nSolving: {' + '.join(words)} = {result}")
    print("-" * 40)

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading zero check
        if any(mapping[ch] == 0 for ch in first_letters):
            continue

        # Convert words to numbers
        word_values = []
        for word in words:
            num = int(''.join(str(mapping[ch]) for ch in word))
            word_values.append(num)

        result_value = int(''.join(str(mapping[ch]) for ch in result))

        if sum(word_values) == result_value:
            print("Solution Found:")
            for ch in sorted(mapping):
                print(f"  {ch} = {mapping[ch]}")
            print(f"\n  {' + '.join(map(str, word_values))} = {result_value}")
            print("-" * 40)
            return

    print("No solution found.")

# -------------------------------------------------
# EXAMPLE 1: TWO + TWO = FOUR
# -------------------------------------------------

solve_cryptarithm(
    words=["TWO", "TWO"],
    result="FOUR"
)

# -------------------------------------------------
# EXAMPLE 2: SEND + MORE = MONEY
# -------------------------------------------------

solve_cryptarithm(
    words=["SEND", "MORE"],
    result="MONEY"
)
