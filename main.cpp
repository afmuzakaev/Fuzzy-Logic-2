#include <iostream>
#include <cmath>

// Fuzzy Logic Membership Functions
double poor(double x) {
    return std::max(0.0, 1.0 - x / 30.0);
}

double good(double x) {
    return std::max(0.0, std::min(x / 50.0, 1.0));
}

double excellent(double x) {
    return std::max(0.0, (x - 50.0) / 30.0);
}

// Fuzzy Logic Rule Evaluation
double applyRule(double inputTemp, double inputHumidity) {
    double rule1 = std::min(poor(inputTemp), poor(inputHumidity));
    double rule2 = std::min(excellent(inputTemp), good(inputHumidity));
    double rule3 = std::min(good(inputTemp), excellent(inputHumidity));

    // Defuzzification (Centroid Method)
    double numerator = rule1 * 10.0 + rule2 * 30.0 + rule3 * 70.0;
    double denominator = rule1 + rule2 + rule3;

    if (denominator != 0.0) {
        return numerator / denominator;
    }

    return 0.0; // Default value
}

int main() {
    double temperature, humidity;

    std::cout << "Enter temperature (in Celsius): ";
    std::cin >> temperature;

    std::cout << "Enter humidity (0-100%): ";
    std::cin >> humidity;

    // Fuzzy Logic Inference and Control
    double airConditioningPower = applyRule(temperature, humidity);

    std::cout << "Air Conditioning Power: " << airConditioningPower << std::endl;

    return 0;
}
