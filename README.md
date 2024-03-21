# JsZ-Document-Generator:

This Python script allows you to generate multiple documents with varying content based on Wikipedia articles. It utilizes natural language processing (NLP) techniques to paraphrase Wikipedia content and create documents suitable for using as study documents to upload to sites like Coursehero.

## Usage

- Clone this repository to your local machine.
- Ensure you have Python installed on your system.
- Install the required dependencies by running the following command: 
- `pip install -r requirements.txt`
- Once the dependencies are installed, you can generate documents by running the following command in your terminal:
- `python generate_documents.py <number_of_docs>`

## Dependencies
Make sure you have Python installed on your system. The script requires the following Python packages:
`
docx
nltk
paraphrase
wikipedia
names`
You can install these dependencies using pip with the provided requirements.txt file.


## Notes
The script fetches random Wikipedia pages, so internet connectivity is required.
Each document's content is then paraphrased and saved in the documents/ folder with a filename format: `<CLASS_NAME>_<CLASS_NUMBER>_<DOC_TYPE>.docx`.
