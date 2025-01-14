import PyPDF2

def pdf_to_text(pdf_path, output_path):
    # Open the PDF file in binary read mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Open the output text file
        with open(output_path, 'w', encoding='utf-8') as text_file:
            # Iterate through all pages
            for page_num in range(len(pdf_reader.pages)):
                # Get the page object
                page = pdf_reader.pages[page_num]

                # Extract text from the page
                text = page.extract_text()

                # Write the text to the output file
                text_file.write(text + '\n')

if __name__ == "__main__":
    # Example usage
    input_pdf = r"2501.00663v1.pdf"  # Replace with your PDF file path
    output_txt = r"output.txt"  # Replace with your desired output path

    try:
        pdf_to_text(input_pdf, output_txt)
        print(f"Successfully converted {input_pdf} to {output_txt}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
