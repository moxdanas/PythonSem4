comment = input("Enter comment: ")

if("make a lot of money" in comment.lower() or
   "buy now" in comment.lower() or
   "subscribe this" in comment.lower() or
   "click this" in comment.lower()):

    print("Spam detected!")

else:
    print("Not a spam")