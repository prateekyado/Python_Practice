#logical opertor = evaluate many condition (or, and, not)
#and = both condition should be true
# or = atleast one condition mustbe true
# not= inverts the condition

temp=30
is_raining=False

if temp>35 or temp<0 or is_raining:
    print("Outdoor event Canceled")
else:
    print("not canceled")