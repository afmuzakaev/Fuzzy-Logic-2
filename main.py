import math

# Fuzzy Logic Membership Functions
def poor(x):
    return max(0.0, 1.0 - x / 30.0)

def good(x):
    return max(0.0, min(x / 50.0, 1.0))

def excellent(x):
    return max(0.0, (x - 50.0) / 30.0)

# Fuzzy Logic Rule Evaluation
def apply_rule(input_temp, input_humidity):
    rule1 = min(poor(input_temp), poor(input_humidity))
    rule2 = min(excellent(input_temp), good(input_humidity))
    rule3 = min(good(input_temp), excellent(input_humidity))

    # Defuzzification (Centroid Method)
    numerator = rule1 * 10.0 + rule2 * 30.0 + rule3 * 70.0
    denominator = rule1 + rule2 + rule3

    if denominator != 0.0:
        return numerator / denominator

    return 0.0  # Default value

def main():
    temperature = float(input("Enter temperature (in Celsius): "))
    humidity = float(input("Enter humidity (0-100%): "))

    # Fuzzy Logic Inference and Control
    air_conditioning_power = apply_rule(temperature, humidity)

    print("Air Conditioning Power:", air_conditioning_power)

if __name__ == "__main__":
    main()
import math

# Fuzzy Logic Membership Functions
def poor(x):
    return max(0.0, 1.0 - x / 30.0)

def good(x):
    return max(0.0, min(x / 50.0, 1.0))

def excellent(x):
    return max(0.0, (x - 50.0) / 30.0)

# Fuzzy Logic Rule Evaluation
def apply_rule(input_temp, input_humidity):
    rule1 = min(poor(input_temp), poor(input_humidity))
    rule2 = min(excellent(input_temp), good(input_humidity))
    rule3 = min(good(input_temp), excellent(input_humidity))

    # Defuzzification (Centroid Method)
    numerator = rule1 * 10.0 + rule2 * 30.0 + rule3 * 70.0
    denominator = rule1 + rule2 + rule3

    if denominator != 0.0:
        return numerator / denominator

    return 0.0  # Default value

def main():
    temperature = float(input("Enter temperature (in Celsius): "))
    humidity = float(input("Enter humidity (0-100%): "))

    # Fuzzy Logic Inference and Control
    air_conditioning_power = apply_rule(temperature, humidity)

    print("Air Conditioning Power:", air_conditioning_power)

if __name__ == "__main__":
    main()
