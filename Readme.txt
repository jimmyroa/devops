
# Readme.txt

## Instructions to Run the Build Script for Automated Testing

### Prerequisites:
- Ensure Python is installed on your machine (recommended version 3.8 or higher).
- Make sure `unittest` is available (it is built-in with Python).

### Setup Instructions:
1. Clone the repository containing the Python script and test files.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install any dependencies if listed in a `requirements.txt` file (if not, skip this step):
   ```bash
   pip install -r requirements.txt
   ```
   
### Running the Build Script:
1. To run the main script, use the command:
   ```bash
   python devops_a2.py
   ```
   Note: This will execute the main program, prompting for user input (if not protected with an `if __name__ == "__main__":` guard).

2. To run automated tests using the `unittest` framework, execute the following:
   ```bash
   python -m unittest discover
   ```
   This will automatically detect and run all unit tests in files starting with `test_`.

