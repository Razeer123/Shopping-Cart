# Shopping Cart 🤑

Shopping Cart is a simple project written in Python. It was created as a take-home assignment 
for the [Mongo DB](https://www.mongodb.com) company. The project's goal was to create a receipt printing system
for an online shopping cart.

## Example output 🥳
A receipt is printed as a formatted table. Minimal width of particular values is calculated using keys of items in the 
database.
```
------------ RECEIPT ------------
Name             Quantity         Price           
Apple            2                €1.0            
Banana           4                €2.0            
Total: €10.00
```

## Usage 👨‍💻
To use the program, it's necessary to populate the database of products located in `pricer.py`, create an
instance of a shopping cart, and add a product. The minimal working code is visible below.
```
sc = ShoppingCartConcreteCreator().operation()
sc.add_item("Apple", 2)
sc.print_receipt()
```
**User can decide about the order of columns**. To do that, an optional parameter was added to the 
`ShoppingCartConcreteCreator().operation()`. This factory method can take a list of three values from the `Order` 
enum. The columns are then generated accordingly. For example, running the code:
```
sc = ShoppingCartConcreteCreator().operation([Order.NAME, Order.PRICE, Order.QUANTITY])
sc.add_item("Apple", 2)
sc.add_item("Banana", 4)
sc.print_receipt()
```
will generate the following output:
```
------------ RECEIPT ------------
Name             Price            Quantity        
Apple            €1.0             2               
Banana           €2.0             4               
Total: €10.00
```
In case of no parameter provided or wrong values put inside the list, program will use the default order:
`default_order = ['Name', 'Quantity', 'Price']`.

## Testing 💡
Six different tests were placed in the `tests.py` file. They check the whole process of generating a receipt. They were
changed so that they don't require modifications when the different database is used; test values are updated accordingly.
It was assumed that the input would be tested without whitespace characters, as the number of those characters
can change according to the database. There is just no point in hardcoding them. 

## Improvement ideas 🤔

If more time were allowed for the project, I would create a simple console that would enable the user to add new
items to the database. I would also probably store the database in a better way than currently.