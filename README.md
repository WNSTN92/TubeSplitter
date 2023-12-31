# TubeSplitter

TubeSplitter is a web application that allows users to extract separate audio stems from a YouTube video. Simply input the YouTube video link, and the application will provide you with a zip file containing the stems.

<img src="https://github.com/WNSTN92/TubeSplitter/assets/147709972/cd5c4413-09b7-4353-8d06-e4a4ff7af11c" width="400">

## Features

- **YouTube Video Download**: Downloads the provided YouTube video link.
- **Audio Extraction**: Extracts the audio from the downloaded video and converts it into an MP3 format.
- **Stem Separation**: Uses the `spleeter` library to separate the audio into different stems.
- **File Provision**: Packs the separated stems into a zip file and provides a download link.

## Setup & Installation

1. Clone the repository.
   `git clone https://github.com/WNSTN92/TubeSplitter.git`

3. Navigate into the project directory.
   `cd TubeSplitter`

5. Install the required Python packages.
   `pip install -r requirements.txt`

7. Start the Flask application.
   `python app.py`

9. Navigate to `http://127.0.0.1:5000/` in your browser.

## Contribution

Feel free to fork this project, make changes, and submit pull requests. Any contributions are heartily welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).
