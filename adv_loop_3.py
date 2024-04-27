#Write your function here
def over_nine_thousand(lst):
    sum = 0
    for number in lst:
        sum += number
        if sum > 9000:
                break # break must be in right indentation
    return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([123,8000,900,120,5000]))