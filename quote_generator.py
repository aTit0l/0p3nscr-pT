Steps to follow:

Create a new file called quote_generator.py
Define a list of quotes that you want the script to choose from. You can do this by creating a variable called quotes and assigning a list of strings to it. For example:
css
Copy code
quotes = [    "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",    "The way to get started is to quit talking and begin doing. -Walt Disney",    "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt"]
Import the random module to choose a random quote from the list. You can do this by adding import random at the top of your file.
Create a variable called random_quote and assign a randomly chosen quote from the quotes list using the random.choice() function. For example:
arduino
Copy code
random_quote = random.choice(quotes)
Finally, print the random_quote variable to the console using the print() function. For example:
scss
Copy code
print(random_quote)
Save the file and push it to your GitHub repository.
Now, every time you run the quote_generator.py script, it will choose a random quote from your list and display it on the console. This is a simple and fun project that you can customize by adding your own quotes or modifying the script to display the quote in a different way.
