how_to_text = f"""1. **Upload Image:** \n
\tClick the "Upload Image" button and select the image of your business card. \n
\tEnsure the image is clear and well-lit for optimal results.\n

2. **Extract Information:**\n
\tClick the "Extract Information" button.\n
\tThe application will use OCR to analyze the image and attempt to identify relevant fields like name, company, contact details, and address.\n

3. **Review & Save:**\n
\tThe extracted information will be displayed.\n
\tReview the data and make any necessary corrections.\n
\tClick "Save to Database" to store the information and the business card image for future reference.\n
"""

about_text ="""This application is designed to streamline your business card management process.
It utilizes the power of Optical Character Recognition (OCR) to extract key information from business card images."""

how_it_works = f"""This application leverages the following technologies:\n

* **EasyOCR:** A powerful OCR library that converts text within the image to digital text.
* **Streamlit:** A Python framework for creating user-friendly web applications.

Here's a breakdown of the process:

1. **Image Upload:** You upload a business card image.
2. **OCR Processing:** EasyOCR analyzes the image and extracts text data.
3. **Information Extraction:** The application parses the extracted text using pre-defined rules to identify specific details like name, company, and contact information.
4. **Data Display:** The extracted information is presented in a clear and organized format for your review.
5. **Database Storage (Optional):** Upon your confirmation, the extracted information and the uploaded image are saved to a database for future access and management.

**Additional Features:**

This application allows you to not only save data but also:

* **Read Existing Data:** View previously saved business card information from the database.
* **Update Data:** Edit any saved information as needed.
* **Delete Data:** Remove unwanted entries from the database.

This comprehensive functionality helps you efficiently manage your business card collection."""
