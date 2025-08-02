#!/usr/bin/env python3
"""
Setup script for Tennis Pose Detection AI Web Application
This script downloads required model files and sets up the environment.
"""

import os
import sys
import urllib.request
import zipfile
from pathlib import Path

def download_file(url, filename):
    """Download a file from URL to filename with progress indicator."""
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"✓ Downloaded {filename}")
        return True
    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")
        return False

def main():
    print("🎾 Tennis Pose Detection AI - Setup")
    print("=" * 50)
    
    # Create uploads directory if it doesn't exist
    uploads_dir = Path("uploads")
    uploads_dir.mkdir(exist_ok=True)
    print("✓ Created uploads directory")
    
    # Check for required model files
    required_files = [
        "pose_classifier_new.pkl",
        "yolov8m.pt", 
        "yolov8m-pose.pt"
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️  Missing model files: {', '.join(missing_files)}")
        print("\nPlease download the required model files:")
        print("1. pose_classifier_new.pkl - Your trained Random Forest classifier")
        print("2. yolov8m.pt - YOLOv8 model for person detection")
        print("3. yolov8m-pose.pt - YOLOv8-pose model for pose estimation")
        print("\nYou can download these files from:")
        print("- Your local training environment")
        print("- YOLO model repository")
        print("\nPlace them in the project directory and run this script again.")
        return False
    
    print("✓ All required model files found")
    
    # Check Python dependencies
    print("\nChecking Python dependencies...")
    try:
        import flask
        import ultralytics
        import numpy
        import cv2
        import pickle
        import sklearn
        print("✓ All required Python packages are available")
    except ImportError as e:
        print(f"✗ Missing Python package: {e}")
        print("Please install dependencies with: pip install -r requirements.txt")
        return False
    
    print("\n🎉 Setup complete! You can now run the application with:")
    print("python app.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 