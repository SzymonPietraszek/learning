def knapsack_value(
    volume_and_values: list[tuple[int, int]], chosen_objects: list[int]
) -> int:
    value = 0
    for chosen_object in chosen_objects:
        value += volume_and_values[chosen_object][1]
    return value


def pack_knapsack(
    max_knapsack_volume: int, volume_and_values: list[tuple[int, int]]
) -> list[int]:
    best_knapsack = [[]]
    best_knapsack_value = 0
    for knapsack_volume in range(1, max_knapsack_volume + 1):
        best_knapsack.append(best_knapsack[-1])
        for idx, volume_and_value in enumerate(volume_and_values):
            volume, value = volume_and_value
            if volume > knapsack_volume:
                continue

            smaller_knapsack = best_knapsack[knapsack_volume - volume]
            if idx in smaller_knapsack:
                continue

            new_knapsack_value = value + knapsack_value(
                volume_and_values, smaller_knapsack
            )
            if new_knapsack_value > best_knapsack_value:
                best_knapsack[knapsack_volume] = best_knapsack[
                    knapsack_volume - volume
                ] + [idx]
                best_knapsack_value = new_knapsack_value
    return best_knapsack[-1]


objs = [(2, 300), (1, 200), (5, 400), (3, 500)]
best = pack_knapsack(10, objs)
print(best, knapsack_value(objs, best))
