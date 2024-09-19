class MortgageCalculator:
    def __init__(self, principal, annual_interest_rate, years, taxes=0, insurance=0):
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.years = years
        self.taxes = taxes
        self.insurance = insurance
        self.monthly_payment = self.calculate_monthly_payment()

    def calculate_monthly_payment(self):
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        number_of_payments = self.years * 12

        if monthly_interest_rate == 0:  # Handle 0% interest
            payment = self.principal / number_of_payments
        else:
            payment = (self.principal * monthly_interest_rate) / \
                      (1 - (1 + monthly_interest_rate) ** -number_of_payments)

        # Add taxes and insurance to the monthly payment
        total_monthly_payment = payment + self.taxes + self.insurance
        return total_monthly_payment

    def display_results(self):
        print(f"Loan Amount (Principal): ${self.principal:.2f}")
        print(f"Annual Interest Rate: {self.annual_interest_rate:.2f}%")
        print(f"Loan Term: {self.years} years")
        print(f"Monthly Payment (including taxes and insurance): ${self.monthly_payment:.2f}")


if __name__ == "__main__":
    # User inputs
    principal = float(input("Enter the loan amount (principal): "))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    years = int(input("Enter the loan term in years: "))

    # Optional inputs
    taxes = float(input("Enter the monthly property taxes (default is $0): ") or 0)
    insurance = float(input("Enter the monthly insurance cost (default is $0): ") or 0)

    # Create a mortgage calculator instance
    calculator = MortgageCalculator(principal, annual_interest_rate, years, taxes, insurance)

    # Display the results
    calculator.display_results()
