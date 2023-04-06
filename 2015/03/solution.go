package main

import (
	"fmt"
)

func nextPos(pos *[2]int, move rune) {
	switch move {
	case '^':
		pos[1]++
	case 'v':
		pos[1]--
	case '>':
		pos[0]++
	case '<':
		pos[0]--
	}
}

func main() {
	var line string
	var santa1Pos, santa2Pos, roboSantaPos [2]int
	year1 := make(map[[2]int]bool)
	year2 := make(map[[2]int]bool)
	fmt.Scanln(&line)
	year1[santa1Pos] = true
	year2[santa2Pos] = true
	for i, move := range line {
		nextPos(&santa1Pos, move)
		year1[santa1Pos] = true
		var pos *[2]int
		if i%2 == 0 {
			pos = &santa2Pos
		} else {
			pos = &roboSantaPos
		}
		nextPos(pos, move)
		year2[*pos] = true
	}
	fmt.Println("Part One:", len(year1))
	fmt.Println("Part Two:", len(year2))
}
