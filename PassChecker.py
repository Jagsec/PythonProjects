#!/usr/bin/python

import sys, getopt

def checker(password):
    lowercaseCounter = 0
    uppercaseCounter = 0
    numberCounter = 0
    specialCounter = 0
    for letter in password:
        if letter.islower():
            lowercaseCounter += 1
        elif letter.isupper():
            uppercaseCounter += 1
        elif letter.isnumeric():
            numberCounter += 1
        else:
            specialCounter += 1
    return lowercaseCounter, uppercaseCounter, numberCounter, specialCounter

def securityEvaluation(lowercaseCounter, uppercaseCounter, numberCounter, specialCounter, password):
    securityLevel = 0
    securityText = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong", "Optimal"]
    if lowercaseCounter > 0:
        securityLevel += 1
    if uppercaseCounter > 0:
        securityLevel += 1
    if numberCounter > 0:
        securityLevel += 1
    if specialCounter > 0:
        securityLevel += 1
    if len(password) > 10:
        securityLevel += 1
    return securityText[securityLevel]

def main(argv):
    input_file = ""
    output_file = ""
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["input_file=", "output_file="])
    except getopt.GetoptError:
        print("python PassChecker.py -i <input_file> -o <output_file>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("python PassChecker.py -i <input_file> -o <output_file>")
        elif opt in ("-i", "--input_file"):
            input_file = arg
        elif opt in ("-o", "--output_file"):
            output_file = arg
    if input_file != "":
        with open(input_file, "r") as file_object:
            passwords = file_object.readlines()
        for password in passwords:
            password = password.rstrip()
            lwcC, upcC, numC, spC = checker(password)
            securityScore = securityEvaluation(lwcC, upcC, numC, spC, password)
            with open(output_file, "a") as file_object:
                file_object.write(f"{password}: {securityScore}\n")
        print(f"Checked passwords in {output_file}")

if __name__ == "__main__":
    main(sys.argv[1:])