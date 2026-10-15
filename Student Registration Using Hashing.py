size = int(input("Enter the size of the hash table: "))
hash_table = [None] * size

while True:
    print("\n--- Student Registration System ---")
    print("1. Insert Student Record")
    print("2. Search Student by Roll Number")
    print("3. Delete Student Record")
    print("4. Display Hash Table")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        roll = int(input("Enter student roll number (Key): "))
        name = input("Enter student name (Value): ")

        index = roll % size
        start_index = index
        inserted = False

        while True:
            if hash_table[index] is None or hash_table[index] == "DELETED":
                hash_table[index] = (roll, name)
                print(f"Record inserted successfully at index {index}")
                inserted = True
                break

            index = (index + 1) % size

            if index == start_index:
                break

        if not inserted:
            print("Hash table is full. Cannot insert record.")

    elif choice == "2":
        roll = int(input("Enter roll number to search: "))
        index = roll % size
        start_index = index
        found = False

        while hash_table[index] is not None:
            if hash_table[index] != "DELETED" and hash_table[index][0] == roll:
                print(f"Student found at index {index}")
                print("Roll Number:", hash_table[index][0])
                print("Name:", hash_table[index][1])
                found = True
                break

            index = (index + 1) % size

            if index == start_index:
                break

        if not found:
            print("Student record not found.")

    elif choice == "3":
        roll = int(input("Enter roll number to delete: "))
        index = roll % size
        start_index = index
        deleted = False

        while hash_table[index] is not None:
            if hash_table[index] != "DELETED" and hash_table[index][0] == roll:
                hash_table[index] = "DELETED"
                print("Record deleted successfully.")
                deleted = True
                break

            index = (index + 1) % size

            if index == start_index:
                break

        if not deleted:
            print("Record not found to delete.")

    elif choice == "4":
        print("\nHash Table:")
        for i in range(size):
            print(f"Index {i}: {hash_table[i]}")

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Please choose between 1 and 5.")
