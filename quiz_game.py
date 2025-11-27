import csv
import random

class QuizGame:
    """
    A comprehensive quiz game system that loads questions from CSV files,
    administers quizzes, tracks scores, and validates answers.

    The class handles question randomization, input validation, score tracking,
    and provides real-time feedback to players.

    Attributes:
        questions (list): questions (list): List of question dictionaries loaded from CSV.
        score (int): The player's current score.
        attempts (int): Number of valid answer attempts made by player.
    """

    def __init__(self, filename: str) -> None:
        """
        Initialize the QuizGame by loading questions from the specified file.

        Args:
            filename (str): Path to CSV file containing quiz questions.
                Expected columns: question, option_a, option_b, option_c, option_d, answer

        Raises:
            FileNotFoundError: If the specified CSV file cannot be found
            KeyError: If CSV file missing required columns
        """
        self.questions = self.load_questions(filename)
        # Randomize question order for varied gameplay experience
        random.shuffle(self.questions)
        self.score = 0 # Tracks correct answers
        self.attempts = 0 # Tracks valid answer attempts (A/B/C/D inputs)

    @staticmethod
    def load_questions(filename: str) -> list[dict]:
        """
        Parse CSV file and extract quiz questions with options and answers.

        Expected CSV format:
            question, option_a, option_b, option_c, option_d, answer

        Args:
            filename (str): Path to the CSV file containing quiz data.

        Returns:
            list: List of question dictionaries with keys:
                - question (str): The quiz question
                - option_a, option_b, option_c, option_d (str): Answer choices
                - answer (str): Correct answer text (matches one of the options)

        Raises:
            FileNotFoundError: If the specified file doesn't exist
            csv.Error: If CSV file is malformed or unreadable
        """
        questions = []
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                # Validate that required columns exist in CSV
                required_columns = {'question', 'option_a', 'option_b',
                                    'option_c', 'option_d', 'answer'}
                if not required_columns.issubset(reader.fieldnames):
                    missing = required_columns - set(reader.fieldnames)
                    raise ValueError(f"CSV missing required columns: {missing}")

                for row in reader:
                    questions.append(row)
        except FileNotFoundError:
            print(f"Error: Quiz file '{filename}' not found.")
            raise
        except csv.Error as e:
            print(f"Error reading CSV file: {e}")
            raise

        return questions

    def play(self) -> None:
        """
        Execute the main quiz game loop.

        Presents questions sequentially, collects user input, validates answers,
        updates score, and provides immediate feedback. The loop continues until
        all questions are answered or the player enters 'quit'.

        Features:
            - Case-insensitive input handling
            - Input validation with helpful error messages
            - Real-time score tracking
            - Early exit capability
        """
        print("Welcome to the General Knowledge Quiz!")
        print("Type 'quit' anytime to exit the game.\n")

        # Iterate through the randomized questions
        for i, question in enumerate(self.questions, start=1):
            # Display current question number and question text
            print(f"Question: {question['question']}")
            print(f"A. {question['option_a']}")
            print(f"B. {question['option_b']}")
            print(f"C. {question['option_c']}")
            print(f"D. {question['option_d']}")

            # Map user input to the corresponding option text for validation
            option_map = {
                'a': question['option_a'],
                'b': question['option_b'],
                'c': question['option_c'],
                'd': question['option_d']
            }

            # Collect and normalize user input
            user_input = input("Your answer (A/B/C/D) or 'quit': ").strip().lower()

            # Exit mechanism - break loop if user wants to quit
            if user_input == 'quit':
                print("\nExiting quiz...")
                break

            # Validate input and process answer
            if user_input in option_map:
                self.attempts += 1  # Only count valid attempts

                # Compare selected option text with correct answer (case-insensitive)
                if option_map[user_input].lower() == question['answer'].lower():
                    print("✅ Correct!\n")
                    self.score += 1
                else:
                    print("❌ Incorrect.")
                    print(f"The correct answer is: {question['answer']}\n")
            else:
                # Handle invalid input without counting as an attempt
                print("Invalid input. Please choose A, B, C, or D.\n")

        # Final score display when quiz concludes
        print("Quiz Ended!")
        if self.attempts > 0:
            print(f"Total Score: {self.score}/{self.attempts}")
        else:
            print("No questions were attempted.")


if __name__ == "__main__":
    # Initialize and start the quiz game
    game = QuizGame("general_knowledge_quiz.csv")
    game.play()
