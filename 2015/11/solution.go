package main

import "fmt"

const (
	minChar      = 97  // 'a'
	maxChar      = 122 // 'z'
	illegalChars = "iol"
)

func isIllegalChar(char byte) bool {
	for i := 0; i < len(illegalChars); i++ {
		if char == illegalChars[i] {
			return true
		}
	}
	return false
}

func next(password []byte) {
	for i := len(password) - 1; i >= 0; i-- {
		if password[i] == maxChar {
			password[i] = minChar
		} else {
			password[i]++
			if isIllegalChar(password[i]) {
				password[i]++
			}
			break
		}
	}
}

func isIncreasingStraight(password []byte) bool {
	for i := 0; i < len(password)-2; i++ {
		if password[i]+1 == password[i+1] && password[i+1]+1 == password[i+2] {
			return true
		}
	}
	return false
}

func isPair(password []byte) bool {
	pairCount := 0
	for i := 0; i < len(password)-1; i++ {
		if password[i] == password[i+1] {
			pairCount++
			i++
		}
	}
	return pairCount >= 2
}

func main() {
	var password []byte
	fmt.Scanln(&password)
	for !isIncreasingStraight(password) || !isPair(password) {
		next(password)
	}
	fmt.Println("Part One:", string(password))
	for {
		next(password)
		if isIncreasingStraight(password) && isPair(password) {
			break
		}
	}
	fmt.Println("Part Two:", string(password))
}
