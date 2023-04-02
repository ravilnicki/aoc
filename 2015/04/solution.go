package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
	"strings"
)

func MineAdventCoin(secret []byte, num_zeros int, start int64) int64 {
	i := start
	for {
		hash := md5.Sum(strconv.AppendInt(secret, i, 10))
		encoded := hex.EncodeToString(hash[:])
		if strings.HasPrefix(encoded, strings.Repeat("0", num_zeros)) {
			return i
		}
		i++
	}
}

func main() {
	var secret []byte
	fmt.Scanln(&secret)
	p1 := MineAdventCoin(secret, 5, 1)
	p2 := MineAdventCoin(secret, 6, p1)
	fmt.Println("Part One:", p1)
	fmt.Println("Part Two:", p2)
}
