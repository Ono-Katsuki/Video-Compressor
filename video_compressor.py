import subprocess
import os

def compress_video(input_file, output_file, target_size_mb=10, min_audio_bitrate=32000, max_audio_bitrate=256000, min_video_bitrate=100000):
    # Get the duration of the input video (in seconds)
    probe = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_file], capture_output=True, text=True)
    duration = float(probe.stdout)
    
    # Calculate target bitrate
    target_total_bitrate = (target_size_mb * 8 * 1024 * 1024) / duration
    
    # Determine audio bitrate (assuming it's 10% of the total bitrate)
    audio_bitrate = max(min(target_total_bitrate * 0.1, max_audio_bitrate), min_audio_bitrate)
    
    # Calculate video bitrate
    video_bitrate = target_total_bitrate - audio_bitrate
    
    # Ensure video bitrate is not lower than the minimum
    if video_bitrate < min_video_bitrate:
        video_bitrate = min_video_bitrate

    # Construct FFmpeg command
    cmd = [
        'ffmpeg', '-i', input_file,
        '-c:v', 'libx264', '-preset', 'slow',
        '-b:v', str(int(video_bitrate)),
        '-maxrate', str(int(video_bitrate * 1.5)),
        '-bufsize', str(int(video_bitrate * 2)),
        '-c:a', 'aac', '-b:a', str(int(audio_bitrate)),
        '-y', output_file
    ]

    # Run FFmpeg
    subprocess.run(cmd)

def main():
    # Get input file path interactively
    input_file = input("Enter the path of the video file you want to compress: ").strip()

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    # Generate output file name (input file name + "_compressed" + original extension)
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_compressed{ext}"

    # Get target size interactively (default: 10MB)
    target_size_mb = input("Enter the target file size in MB (default: 10): ").strip()
    target_size_mb = int(target_size_mb) if target_size_mb else 10

    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    print(f"Target size: {target_size_mb}MB")

    compress_video(input_file, output_file, target_size_mb)
    print(f'Compressed {input_file} and created {output_file}.')

if __name__ == "__main__":
    main()
