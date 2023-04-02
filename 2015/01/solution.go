package main

import (
	"fmt"
)

func main() {
	var line string
	var floor, basement int
	fmt.Scanln(&line)
	for i, ch := range line {
		if ch == '(' {
			floor++
		} else {
			floor--
			if basement == 0 && floor == -1 {
				basement = i + 1
			}
		}
	}
	fmt.Println("Part One:", floor)
	fmt.Println("Part Two:", basement)
}
