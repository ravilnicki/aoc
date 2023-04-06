package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var grid1 [1000][1000]int
	var grid2 [1000][1000]int
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		fields := strings.Fields(line)
		var cmd, start, end string
		if len(fields) == 4 {
			cmd, start, _, end = fields[0], fields[1], fields[2], fields[3]
		} else {
			_, cmd, start, _, end = fields[0], fields[1], fields[2], fields[3], fields[4]
		}
		var r1, c1, r2, c2 int
		fmt.Sscanf(start, "%d,%d", &r1, &c1)
		fmt.Sscanf(end, "%d,%d", &r2, &c2)
		for r := r1; r <= r2; r++ {
			for c := c1; c <= c2; c++ {
				switch cmd {
				case "toggle":
					if grid1[r][c] == 1 {
						grid1[r][c] = 0
					} else {
						grid1[r][c] = 1
					}
					grid2[r][c] += 2
				case "on":
					grid1[r][c] = 1
					grid2[r][c] += 1
				case "off":
					grid1[r][c] = 0
					if grid2[r][c] > 0 {
						grid2[r][c] -= 1
					}
				}
			}
		}
	}
	p1, p2 := 0, 0
	for r := range grid1 {
		for c := range grid1[r] {
			p1 += grid1[r][c]
			p2 += grid2[r][c]
		}
	}
	fmt.Println("Part One:", p1)
	fmt.Println("Part Two:", p2)
}
