from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Create a text summarization pipeline with the BART model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route('/')
def home():
    # Render the home page (index.html)
    return render_template('index.html')

@app.route('/text-summarization', methods=["POST"])
def summarize():
    if request.method == "POST":
        # Get the input text from the HTML form
        inputtext = request.form["inputtext_"]

        # Use the summarizer pipeline to generate the summary
        summary = summarizer(inputtext, max_length=300, min_length=30, do_sample=False)

        # Extract the generated summary
        summary_text = summary[0]['summary_text']

        # Render the output.html template with the generated summary
        '''
            Example:
            inputtext = "This is an example text for summarization."

            summary_text = "This is a summary of the input text."
        '''

    return render_template("output.html", data={"summary": summary_text})

if __name__ == '__main__':
    # Start the Flask application if the script is run directly
    app.run()
