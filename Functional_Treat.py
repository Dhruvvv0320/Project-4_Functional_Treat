print("Welcome to the Data Analyzer and Transformer Program")

dataArray = []
while True:
    print("\nMain Menu : ")
    print("1. Input Data.")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program.")
    choice = int(input("Enter your choice : "))

    match choice:
        case 1:
                         
            nums = [int(num) for num in input("\nEnter Data for a 1D array (seperated by spaces) : \n").split()]
            dataArray = nums

            print("Data has been stored successfully...\n")

        case 2:
            print("\nData Summary : ")
            print("- Total elements : ",len(dataArray))
            print("- Maximum Value : ",max(dataArray))
            print("- Minimum Value : ",min(dataArray))
            print("- Sum of all values : ",sum(dataArray))
            average = float(sum(dataArray) / len(dataArray))
            print(f"- Average value : {average:.2f}",)   
        case 3:
            num = int(input("\nEnter a number to calculate factorial : "))

            def factorial(n):
                '''
                This function calculates factorial of a given number using recursion if that number is equal or less than 1 then it simply returns 1.
                '''
                if n <= 1:
                    return 1
                
                return n * factorial(n-1)
            
            print(f"Factorial of {num} is : {factorial(num)}")
        case 4:
            num = int(input("\nEnter a threshold value to filter out data above this value : "))

            greater_than = lambda lst,n: [x for x in lst if x >= n]
            result = greater_than(dataArray,num)

            if result:
                print(f"Filtered Data (values >= {num}) : ")
                print(*result, sep=",")
            else:
                print(f"There is no values > {num}")
        case 5:
            while True:
                print("\nChoose sorting option :")
                print("1. Ascending")
                print("2. Descending")
                print("3. Back to main menu.")
                option = int(input("Enter your choice : "))

                match option:
                    case 1:
                        print("Sorted Data in Ascending Order : ")
                        dataArray.sort()
                        print(dataArray)
                    case 2:
                        print("Sorted Data in Descending Order : ")
                        dataArray.sort(reverse=True)
                        print(dataArray)
                    case 3:
                        break
                    case _:
                        print("Invalid option...")
        case 6:
            print("\nDataset Statistics : ")
            print("- Maximum Value : ",max(dataArray))
            print("- Minimum Value : ",min(dataArray))
            print("- Sum of all values : ",sum(dataArray))
            average = float(sum(dataArray) / len(dataArray))
            print(f"- Average value : {average:.2f}",)
        case 7:
            print("\nThank you for using The Data Analyzer and Transformer Program. Goodbye!")
            break
        case _:
            print("Invalid Choice...")