package main

import (
	"fmt"
	"slices"
)

func knapsackValue(volumeAndValues [][]int, chosenObjects []int) int {
	ret := 0
	for _, chosenObject := range chosenObjects {
		ret += volumeAndValues[chosenObject][1]
	}
	return ret
}

func packKnapsack(maxKnapsackVolume int, volumeAndValues [][]int) []int {
	best := [][]int{{}}
	bestValue := 0

	for i := range maxKnapsackVolume {
		volume := i + 1
		fmt.Println("vol", volume)
		best = append(best, best[len(best)-1])

		for objectIdx, volumeAndValue := range volumeAndValues {
			objectVolume, value := volumeAndValue[0], volumeAndValue[1]
			if objectVolume > volume {
				continue
			}

			previousBest := best[volume-objectVolume]
			if slices.Contains(previousBest, objectIdx) {
				continue
			}

			newValue := knapsackValue(volumeAndValues, previousBest) + value
			if newValue > bestValue {
				best[volume] = append(previousBest, objectIdx)
				bestValue = newValue
			}
		}

	}
	return best[maxKnapsackVolume]
}

func main() {
	objs := [][]int{{2, 300}, {1, 200}, {5, 400}, {3, 500}}
	best := packKnapsack(10, objs)
	fmt.Println(best, knapsackValue(objs, best))
}
