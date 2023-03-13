package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	line = strings.TrimSpace(line)
	floor, basement := 0, 0
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
