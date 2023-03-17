package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	paper, ribbon := 0, 0
	for scanner.Scan() {
		dimensions := strings.Split(scanner.Text(), "x")
		sides := make([]int, len(dimensions))
		for i, s := range dimensions {
			n, _ := strconv.Atoi(s)
			sides[i] = n
		}
		sort.Ints(sides)
		w, l, h := sides[0], sides[1], sides[2]
		paper += 2*(w*l+l*h+w*h) + w*l
		ribbon += 2*(w+l) + w*l*h
	}
	fmt.Println("Part One:", paper)
	fmt.Println("Part Two:", ribbon)
}
