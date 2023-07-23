"""lists generation."""
# generator
def chunk_generator(data_range, chunk_size):
    data_list = list(data_range)
    for i in range(0, len(data_list), chunk_size):
        yield data_list[i:i + chunk_size]

# Example usage 1:
#var1=int(input("Enter the range data: "))
#var2=int(input("Enter the length  chunk: "))
#result = chunk_generator(range(var1), chunk_size=var2)

# Example usage 2:
result = chunk_generator(range(11), chunk_size=3)
for chunk in result:
    print(chunk)
print("result:", type(result))
