# Video Compressor

This is a simple Python script that compresses video files using FFmpeg. It allows users to specify an input video file and a target file size, then compresses the video accordingly.

## Features

- Interactive command-line interface
- Automatic output file naming
- Customizable target file size
- Uses FFmpeg for efficient video compression

## Requirements

- Python 3.6 or higher
- FFmpeg

## Installation

1. Ensure you have Python 3.6 or higher installed on your system.
2. Install FFmpeg:
   - On Ubuntu or Debian:
     ```
     sudo apt update
     sudo apt install ffmpeg
     ```
   - On macOS (using Homebrew):
     ```
     brew install ffmpeg
     ```
   - On Windows (using Chocolatey):
     ```
     choco install ffmpeg
     ```
   - For other systems, please refer to the [official FFmpeg documentation](https://ffmpeg.org/download.html).

3. Download the `video_compressor.py` script to your local machine.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `video_compressor.py` script.
3. Run the script:
   ```
   python3 video_compressor.py
   ```
4. Follow the prompts to enter the input file path and target file size.

Example:
```
$ python3 video_compressor.py
Enter the path of the video file you want to compress: /path/to/your/video.mp4
Enter the target file size in MB (default: 10): 20
Input file: /path/to/your/video.mp4
Output file: /path/to/your/video_compressed.mp4
Target size: 20MB
Compressed /path/to/your/video.mp4 and created /path/to/your/video_compressed.mp4.
```

## How it works

1. The script prompts the user for an input video file path.
2. It then asks for a target file size in megabytes (MB).
3. Using FFmpeg, it analyzes the input video to determine its duration.
4. Based on the duration and target size, it calculates appropriate bitrates for video and audio.
5. The script then uses FFmpeg to compress the video, maintaining a balance between file size and quality.
6. The compressed video is saved with "_compressed" added to the original filename.

## Limitations

- The script uses a simplified approach to bitrate calculation, which may not always result in the exact target file size.
- Very short videos or extreme target sizes may produce unexpected results.
- The quality of the compressed video depends on various factors, including the original video's quality and content.

## Contributing

Feel free to fork this project, submit issues, or send pull requests if you have ideas for improvements.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
