def whatday(num):
    w = ["Wrong, please enter a number between 1 and 7", 
         "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return w[num] if num in range(8) else w[0]
