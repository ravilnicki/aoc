package main

import (
	"encoding/json"
	"fmt"
	"log"
)

func sumJSON(jsonObject interface{}, ignoreRed bool) float64 {
	var sum float64
	switch val := jsonObject.(type) {
	case map[string]interface{}:
		for _, v := range val {
			if ignoreRed && v == "red" {
				return 0
			}
			sum += sumJSON(v, ignoreRed)
		}
	case []interface{}:
		for _, v := range val {
			sum += sumJSON(v, ignoreRed)
		}
	case float64:
		sum += val
	}
	return sum
}

func main() {
	var jsonString []byte
	var jsonObject interface{}
	fmt.Scanln(&jsonString)
	if err := json.Unmarshal(jsonString, &jsonObject); err != nil {
		log.Fatal(err)
	}
	sum := int(sumJSON(jsonObject, false))
	fmt.Println("Part One:", sum)
	sum = int(sumJSON(jsonObject, true))
	fmt.Println("Part Two:", sum)
}
