# TubeSplitter

TubeSplitter is a web application that allows users to extract separate audio stems from a YouTube video. Simply input the YouTube video link, and the application will provide you with a zip file containing the stems.

## Features

- **YouTube Video Download**: Downloads the provided YouTube video link.
- **Audio Extraction**: Extracts the audio from the downloaded video and converts it into an MP3 format.
- **Stem Separation**: Uses the `spleeter` library to separate the audio into different stems.
- **File Provision**: Packs the separated stems into a zip file and provides a download link.

## Setup & Installation

1. Clone the repository.

2. Navigate into the project directory.

3. Install the required Python packages.

4. Start the Flask application.

5. Navigate to `http://127.0.0.1:5000/` in your browser.

## Contribution

Feel free to fork this project, make changes, and submit pull requests. Any contributions are heartily welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).
