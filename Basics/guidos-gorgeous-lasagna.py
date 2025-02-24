# Exercise Instructions

# You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook.

# Task 1 - Define an EXPECTED_BAKE_TIME constant that returns how many minutes the lasagna should bake in the oven. According to your cookbook, the Lasagna should be in the oven for 40 minutes.

EXPECTED_BAKE_TIME = 40

# Task 2 - Implement the bake_time_remaining() function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME.

def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time

# Task 3 - Implement the preparation_time_in_minutes(number_of_layers) function that takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.

def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * 2

# Task 4 - Implement the elapsed_time_in_minutes(number_of_layers, elapsed_bake_time) function that has two parameters: number_of_layers (the number of layers added to the lasagna) and elapsed_bake_time (the number of minutes the lasagna has been baking in the oven). This function should return the total number of minutes you've been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return (number_of_layers * 2) + elapsed_bake_time