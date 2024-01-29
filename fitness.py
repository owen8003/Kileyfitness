class FitnessTracker:
    def __init__(self):
        self.plan = {}
        self.weight = None
 
    def set_plan(self, day, activity):
        self.plan[day] = activity

    def set_weight(self, weight):
        self.weight = weight

    def update_progress(self, day, did_complete):
        if day in self.plan:
            self.plan[day] = did_complete

    def calculate_progress(self):
        completed = sum(1 for activity in self.plan.values() if activity.lower() == 'yes')
        total = len(self.plan)
        return completed / total if total > 0 else 0

    def display_progress(self):
        progress = self.calculate_progress() * 100
        print(f"You completed {progress:.2f}% of your planned activities.")

    def display_weight_change(self):
        if self.weight is not None:
            print(f"Your weight change for the week: {self.weight_change()} lb")

    def weight_change(self):
        # Assuming self.weight is the weight at the end of the week and initial weight is 0
        return self.weight

def save_data(data):
    with open("fitness_data.txt", "a") as file:
        file.write(data + "\n")

def main():
    tracker = FitnessTracker()

    # Set plan for the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        activity = input(f"What is your plan for {day}? ")
        tracker.set_plan(day, activity)
        save_data(f"{day}: {activity}")

    # Set initial weight
    initial_weight = float(input("Enter your weight at the beginning of the week: "))
    tracker.set_weight(initial_weight)
    save_data(f"Initial weight: {initial_weight} lb")

    # Update progress each day
    for day in days:
        did_complete = input(f"Did you complete your planned activity for {day}? (yes/no) ")
        tracker.update_progress(day, did_complete.lower())
        save_data(f"{day} progress: {did_complete.lower()}")

    # Display progress and weight change
    tracker.display_progress()
    tracker.display_weight_change()

if __name__ == "__main__":
    main()
    
