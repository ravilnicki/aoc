package main

import (
	"fmt"
)

func lookAndSay(nums []int) []int {
	var new_nums []int
	start := 0
	for i := range nums {
		if nums[i] != nums[start] {
			new_nums = append(new_nums, i-start, nums[start])
			start = i
		}
	}
	new_nums = append(new_nums, len(nums)-start, nums[start])
	return new_nums
}

func main() {
	var number string
	fmt.Scanln(&number)
	digits := make([]int, len(number))
	for i, d := range number {
		digits[i] = int(d - '0')
	}
	for i := 0; i < 40; i++ {
		digits = lookAndSay(digits)
	}
	fmt.Println("Part One:", len(digits))
	for i := 0; i < 10; i++ {
		digits = lookAndSay(digits)
	}
	fmt.Println("Part Two:", len(digits))
}
