
# Business Card Manager - Streamlit App

This Streamlit application simplifies business card management by extracting information using OCR (Optical Character Recognition).

## About

This user-friendly application extracts key details from business card images, eliminating the need for manual data entry. Streamline your business card organization process with features like:

* **Effortless Data Extraction:** Leverage OCR technology to automatically extract information from uploaded business card images.
* **Intuitive Interface:** The application guides you through a simple upload and extraction process.
* **Clear Data Display:** Review extracted information in a well-organized format.
* **Optional Database Storage:** Save extracted data and the corresponding business card image for future reference.

**Additional Features:**

* **Read Existing Data:** Access previously saved business card information.
* **Update Data:** Modify any saved information as needed.
* **Delete Data:** Remove unwanted entries from the database.

## How to Use

1. **Clone the Repository:**

  ```bash
  git clone https://github.com/WolfAtTheDesk/BusinessCard-Storer-using-OCR.git
  ```

2. **Install Dependencies:**

  Navigate to the project directory and install required libraries using pip:

  ```bash
  pip install streamlit easyocr 
  ```


3. **Run the Application:**

  ```bash
  streamlit run main.py
  ```

  This will launch the application in your web browser.

4. **Upload an Image:**

  Click the "Upload Image" button and select the image of your business card. Ensure the image is clear and well-lit for optimal results.

5. **Extract Information:**

  Click the "Extract Information" button. The application will use OCR to analyze the image and extract data.

6. **Review & Save (Optional):**

  Review the extracted information and make any necessary corrections. If you wish to save the data, click "Save to Database." This will store the information and image for future access.

## Technologies Used

* Streamlit: Python framework for creating web UIs.
* EasyOCR: Open-source library for text extraction from images.
* Pillow (PIL Fork): Python Imaging Library for image processing.
* (Other technologies used in your project)


## Contributing

We welcome contributions to this project! Feel free to create a pull request with your improvements or bug fixes.
