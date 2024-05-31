package errors

import (
	"fmt"
	"log"
	"os"
	"runtime/debug"
)

var head string = "\n\nAnswer from byogram: "

func AssertTest(compared, comparedfunc, comparator, comparatorfunc string) (err error) {
	body := "\n\nAnswer from fmtogram: The data doesn't match. The original passed value in %s (%s) is different from the final %s (%s)"
	err = fmt.Errorf(fmt.Sprintf(body, comparedfunc, compared, comparatorfunc, comparator))
	return err
}

func JustError() (err error) {
	body := "\n\nAnswer from fmtogram: the length of the passed arrays does not match"
	err = fmt.Errorf(body)
	return err
}

func UpdatesMisstakes(part string) (err error) {
	body := fmt.Sprintf(head, part)
	err = fmt.Errorf(body)

	return err
}

func MadeMisstake(err error) {
	log.Println("You have a misstake:", err)
	debug.PrintStack()
}

func MakeIntestines() {
	if r := recover(); r != nil {
		fmt.Println("Recovered from log.Fatal:", r)
		debug.PrintStack()
		os.Exit(1)
	}
}
