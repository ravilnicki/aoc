package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	paper, ribbon := 0, 0
	for scanner.Scan() {
		dims := make([]int, 3)
		fmt.Sscanf(scanner.Text(), "%dx%dx%d", &dims[0], &dims[1], &dims[2])
		sort.Ints(dims)
		w, l, h := dims[0], dims[1], dims[2]
		paper += 2*(w*l+l*h+w*h) + w*l
		ribbon += 2*(w+l) + w*l*h
	}
	fmt.Println("Part One:", paper)
	fmt.Println("Part Two:", ribbon)
}
