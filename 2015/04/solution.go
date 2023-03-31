package main

import (
	"bufio"
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	secret, _ := reader.ReadBytes('\n')
	var p1, p2, i int64 = 0, 0, 1
	for ; i < 10000000; i++ {
		hash := md5.Sum(strconv.AppendInt(secret, i, 10))
		if p1 == 0 {
			if strings.HasPrefix(hex.EncodeToString(hash[:]), "00000") {
				p1 = i
			}
		}
		if p2 == 0 {
			if strings.HasPrefix(hex.EncodeToString(hash[:]), "000000") {
				p2 = i
			}
		}
		if p1 != 0 && p2 != 0 {
			break
		}
	}
	fmt.Println("Part One:", p1)
	fmt.Println("Part Two:", p2)
}
