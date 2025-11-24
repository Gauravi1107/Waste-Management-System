SORTING_BINS = { "Plastic": 1, "Paper": 2, "Metal": 3,"Glass": 4, "Compost": 5, "Unknown": 0}

def classify_and_sort_item(item_description):

    item = item_description.lower()

    print(f"\n--- Analyzing item: **{item_description}** ---")

    if "bottle" in item or "red" in item or "crinkly" in item:
        classification = "Plastic"
   
    elif "box" in item or "cardboard" in item or "newspaper" in item:
        classification = "Paper"
    
    elif "can" in item or "foil" in item or "shiny" in item:
        classification = "Metal"
    
    elif "jar" in item or "transparent" in item or "green" in item:
        classification = "Glass"
   
    elif "peel" in item or "food" in item:
        classification = "Compost"
   
    else:
        classification = "Unknown"

    bin_number = SORTING_BINS.get(classification, SORTING_BINS["Unknown"])

    if bin_number == 0:
        print(f"🤖 Action: **REJECT** (Bin {bin_number})")
        print("Note: Item cannot be clearly identified. Sending to general waste or further inspection.")
    else:
        print(f"✅ Classified as: **{classification}**")
        print(f"🤖 Action: **MOVE** item to Sorting Bin {bin_number}.")
        
    print("-" * 30)

n=int(input("Enter the number of items to be added: "))
items_list=[]
for i in range(0,n):
    item=input("Enter the item to be added: ")
    items_list.append(item)
print("The list of items is: ", items_list)
for things in items_list:
    classify_and_sort_item(things)
    