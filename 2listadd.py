def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [98,23,1,4,5,8]
    print(listadd(list1, list2))

def listadd(list1, list2):
    list3 = []
    # Make copies to avoid modifying original lists
    list1_copy = list1.copy()
    list2_copy = list2.copy()
    
    # Get the length of the longer list
    max_length = max(len(list1), len(list2))
    
    # Pad shorter list with zeros if needed
    while len(list1_copy) < max_length:
        list1_copy.append(0)
    while len(list2_copy) < max_length:
        list2_copy.append(0)
        
    # Add corresponding elements
    for i in range(max_length):
        list3.append(list1_copy[i] + list2_copy[i])
            
    return list3


if __name__ == "__main__":
    main()