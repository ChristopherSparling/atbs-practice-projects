inv = {'gold': 42, 'rope': 1}
dragon_loot = ['gold', 'gold', 'gold', 'dragon stone', 'sword', 'ruby']

def addToInventory (inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1
    print(inventory)

addToInventory(inv,dragon_loot)
print(inv) # Shows that the addition is done in place and inv is passed-by-reference

def displayInventory(inventory):
    print('Inventory')
    item_total = 0
    for key,value in inventory.items():
        print(str(value) + ' ' + key)
        item_total += value
    print('Total Items: ' + str(item_total))

displayInventory(inv)