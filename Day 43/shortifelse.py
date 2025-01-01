A = int(input("Give A number: "))
B = int(input("Give B number: "))

print("A") if A > B else print("B") if B > A else print("A == B")

C = "negative" if A < 0 else "positive"

print(f"C => {C}")