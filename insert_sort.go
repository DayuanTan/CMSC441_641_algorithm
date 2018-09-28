package main

import (
	"fmt"
	"math/rand"
)

func main() {
	var data []int
	//s := rand.NewSource(time.Now().UnixNano())
	//r := rand.New(s)

	fmt.Print("Unsorted array is:")
	for i := 0; i < 10; i++ {
		data = append(data, rand.Intn(100))
	}
	fmt.Println(data[:])

	sortedData := insertSort(data)
	fmt.Print("Sorted array is:")
	fmt.Println(sortedData[:])
}

func insertSort(data []int) []int {
	var key int
	for j := 1; j < len(data); j++ {
		key = data[j]
		i := j - 1
		for i >= 0 && data[i] > key { // a very trick point here: "i>=0" must be at front, otherwise "out of range" like "data[-1]"". Since "for" is not "while" in python.
			data[i+1] = data[i]
			i--
		}
		data[i+1] = key
	}
	return data
}
