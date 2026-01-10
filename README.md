#☕ Coffee Machine Maker (Python)

This project is a simple console-based coffee machine simulator written in Python. It lets a user order coffee, insert coins, checks ingredient availability, and prepares the drink with sound effects.

📌 Features

Menu with three drinks:

Espresso

Latte

Cappuccino

Checks if enough ingredients are available before making coffee

Accepts Indian coin inputs (₹1, ₹2, ₹5, ₹10)

Calculates total payment and returns change

Updates machine resources after each order

Adds sugar preference (0–3 spoons)

Plays a coffee brewing sound

Displays machine report (resources and profit)

Option to turn off the machine

🧠 How the Code Works
1. Menu and Resources

menu dictionary stores drink ingredients and cost.

resources dictionary keeps track of available water, milk, and coffee.

profit stores total money earned.

2. Resource Check
check_esources_sufficient()


Checks if the machine has enough ingredients to prepare the selected drink.

3. Coin Processing
process_coin()


Takes user input for different coins and calculates the total amount inserted.

4. Making Coffee
make_coffee()


Deducts ingredients from resources

Simulates brewing using time.sleep()

Plays a brewing sound using playsound

Serves coffee with selected sugar level

5. Main Program Loop

Runs continuously until the user types off

Options available:

Order coffee

View report

Turn off machine

▶️ How to Run the Project
Requirements

Python 3

playsound module

Install dependency:

pip install playsound

Run the Program
python project 7(coffee maker).py


Make sure the audio file brewing-coffee-56459.mp3 is in the same folder.

📊 Sample Commands

espresso, latte, cappuccino → Order coffee

report → View resources and profit

off → Shut down machine

🚀 Future Improvements

Input validation for coins and sugar

Graphical interface (GUI)

Online payment support

More drink options
