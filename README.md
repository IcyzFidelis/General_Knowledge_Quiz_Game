# 🧠 General Knowledge Quiz Game

A Python-based command-line quiz application that tests users on general knowledge across various categories including science, geography, history, and pop culture. The game features randomized questions, real-time scoring, and immediate feedback for an engaging experience.

## 📁 Project Overview

- **Title:** General Knowledge Quiz Game
- **Author:** Seyi Ajanaku  
- **Last Updated:** 27/11/2025  
- **Version:** 1.0  

## 🛠️ Technologies Used

- **Language:** Python 3.x  
- **Libraries:**
  - `csv` – Reading question data
  - `random` – Randomizing question order  
- **Data Format:** CSV  
- **Architecture:** Object-Oriented Programming (OOP)

## 🎮 Key Features

- 🔀 Randomized question order for each session  
- ✅ Input validation (only accepts A/B/C/D)  
- 🧮 Accurate scoring based on valid attempts  
- 🚪 Early exit option (`quit` command)  
- 🔡 Case-insensitive answer matching  
- ⚡ Real-time feedback on answers  
- 📚 100 diverse general knowledge questions  

## 💻 System Requirements

- Python 3.6 or higher  
- Compatible with Windows, macOS, and Linux  

## 🧩 Implementation Details

### Class Structure

```python
class QuizGame:
    def __init__(filename):  # Initializes game with questions
    @staticmethod
    def load_questions():    # Reads CSV data
    def play():              # Main game loop and logic
```

### Data Management

- **Source File:** `general_knowledge_quiz.csv`  
- **Columns:** `question`, `option_a`, `option_b`, `option_c`, `option_d`, `answer`  
- **Validation:** Automatic column verification during load  

### Error Handling

- Graceful handling of missing or corrupted CSV files  
- Validation for required columns and malformed data  
- Friendly messages for invalid user inputs  

Example:

```python
try:
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        # File operations
except FileNotFoundError:
    print(f"Error: Quiz file '{filename}' not found.")
    raise
```

## 🧠 Challenges & Solutions

| Challenge | Solution | Impact |
|----------|----------|--------|
| Question Randomization | `random.shuffle(self.questions)` | Enhances replay value |
| Accurate Score Tracking | Count only valid A/B/C/D inputs | Maintains scoring integrity |
| Case-Insensitive Matching | Compare `.lower()` values | Improves user experience |
| CSV Data Integrity | Validate required columns | Prevents runtime errors |

## 🚀 Future Enhancements

### Short-term

- Difficulty levels (Easy, Medium, Hard)  
- Category-based question selection  
- Timed questions  

### Medium-term

- Web interface (Flask/Django)  
- User authentication and score history  
- Admin panel for question management  
- Multiplayer functionality  

### Long-term

- Mobile app (React Native/Flutter)  
- Integration with external question APIs  
- AI-powered adaptive difficulty  
- Global leaderboard system  

## 📦 Installation & Usage

### Setup Instructions

1. Ensure Python 3.6+ is installed  
2. Save `quiz_game.py` and `general_knowledge_quiz.csv` in the same directory  
3. Run the game:

```bash
python quiz_game.py
```

### Game Commands

- `A/B/C/D` – Select answer  
- `quit` – Exit the game  
- Invalid input – Prompts for valid response  

## 🎓 Learning Outcomes

- Object-Oriented Programming  
- File I/O with CSV  
- Data validation and error handling  
- User input processing  
- Code documentation and organization  

## ✅ Conclusion

The General Knowledge Quiz Game is a well-structured Python project that demonstrates strong software engineering principles while delivering an enjoyable user experience. It serves as a solid foundation for future development and enhancements.
