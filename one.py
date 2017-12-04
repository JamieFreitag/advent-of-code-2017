def captcha(input):
    total = 0
    for i in range(len(input)-1):
        if input[i] == input [i+1]:
            total = total + int(input[i])
    if input[len(input)-1] == input[0]:
            total = total + int(input[len(input)-1])
    print total

def circle_item(string, og_index):
    circle_index = ((len(string)/2) + og_index) % len(string)
    return string[circle_index]

def captcha2(input):
    total = 0
    for i in range(len(input)):
        if input[i] == circle_item(input, i):
            total = total + int(input[i])
    print total

digits = raw_input('Input digits -->      ')
captcha2(digits)