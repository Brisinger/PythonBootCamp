myList = [1, 2, 3, 4, 5]
isexhauted = False
try:
    for item in myList:
        # continue
        print(item)
        if (item==5):
            break
        # raise Exception
    else:
        isexhauted = True
        print("Loop exhauted successfully")
except Exception as e:
   print(f"Loop exited with exception failure {e}")
if not(isexhauted):
    print("\nWe have exited the for loop without exhausting it completely\n")