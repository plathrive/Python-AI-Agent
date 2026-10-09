from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
result_1, result_2, result_3, result_4 = get_file_content("calculator", "main.py"), get_file_content("calculator", "pkg/calculator.py"), get_file_content("calculator", "/bin/cat"), get_file_content("calculator", "pkg/does_not_exist.py")
print(result)
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
print("\n")

print(result_1)
print(f"lorem.txt length: {len(result_1)}")
print(f"lorem.txt truncated: {'truncated' in result_1}")
print("\n")

print(result_2)
print(f"lorem.txt length: {len(result_2)}")
print(f"lorem.txt truncated: {'truncated' in result_2}")
print("\n")

print(result_3)
print(f"lorem.txt length: {len(result_3)}")
print(f"lorem.txt truncated: {'truncated' in result_3}")
print("\n")

print(result_4)
print(f"lorem.txt length: {len(result_4)}")
print(f"lorem.txt truncated: {'truncated' in result_4}")