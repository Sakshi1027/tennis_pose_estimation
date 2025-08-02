# Tennis Pose Detection AI Web Application

A beautiful web interface for detecting and classifying tennis poses using advanced AI models. This application combines YOLO person detection, pose estimation, and machine learning classification to identify tennis poses in uploaded images.

## Features

- **Person Detection**: Uses YOLOv8 to detect people in images
- **Pose Estimation**: Extracts 17 key body landmarks and draws skeletal connections
- **Pose Classification**: Classifies tennis poses into 4 categories:
  - Backhand
  - Forehand
  - Ready Position
  - Serve
- **Confidence Scoring**: Provides detailed confidence scores for classifications
- **Modern UI**: Beautiful, responsive web interface with drag-and-drop upload

## Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)
- Your trained model file: `pose_classifier_new.pkl`
- YOLO models will be downloaded automatically on first run

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/tennis-pose-detection.git
   cd tennis-pose-detection
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the setup script**:
   ```bash
   python setup.py
   ```

4. **Add your model files**:
   - Place `pose_classifier_new.pkl` in the project directory
   - The setup script will guide you through any missing files

## Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Upload an image**:
   - Drag and drop an image onto the upload area
   - Or click "Choose File" to browse and select an image
   - Supported formats: JPG, JPEG, PNG, GIF

4. **View results**:
   - Person detection status
   - Pose landmarks extraction
   - Pose classification with confidence score
   - Processed image with skeleton overlay

## How It Works

### 1. Person Detection
- Uses YOLOv8 model to detect people in the uploaded image
- Returns bounding boxes and confidence scores for detected persons

### 2. Pose Estimation
- Uses YOLOv8-pose model to extract 17 key body landmarks
- Draws skeletal connections between landmarks
- Creates a visual skeleton overlay on the image

### 3. Pose Classification
- Extracts flattened landmark coordinates
- Uses your trained Random Forest classifier (`pose_classifier_new.pkl`)
- Classifies the pose into one of 4 tennis categories
- Provides confidence scores for the classification

## File Structure

```
tennis-pose-detection/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── setup.py              # Setup script for model files
├── README.md             # This file
├── .gitignore            # Git ignore rules
├── pose_classifier_new.pkl # Your trained model (required)
├── yolov8m.pt            # YOLO person detection model
├── yolov8m-pose.pt       # YOLO pose estimation model
├── templates/
│   └── index.html        # Web interface template
└── uploads/              # Temporary upload directory (auto-created)
```

**Note**: Large model files (`.pt`, `.pkl`, `.zip`) are excluded from Git to keep the repository size manageable. Users need to add these files manually or download them separately.

## API Endpoints

- `GET /` - Main web interface
- `POST /upload` - Handle image upload and processing
- `GET /health` - Health check endpoint

## Model Information

The application uses your trained Random Forest classifier that was trained on:
- **Dataset**: Tennis Player Actions Dataset
- **Classes**: 4 tennis poses (Backhand, Forehand, Ready Position, Serve)
- **Features**: 34-dimensional landmark coordinates (17 keypoints × 2 coordinates)
- **Accuracy**: ~96% based on your training results

## Troubleshooting

### Common Issues

1. **Model file not found**:
   - Ensure `pose_classifier_new.pkl` is in the project directory
   - Check file permissions

2. **YOLO models downloading slowly**:
   - Models are downloaded automatically on first run
   - This may take a few minutes depending on your internet connection

3. **Memory issues**:
   - The application loads multiple AI models
   - Ensure you have at least 4GB of available RAM

4. **Port already in use**:
   - Change the port in `app.py` line: `app.run(debug=True, host='0.0.0.0', port=5000)`

### Performance Tips

- Use images with clear, well-lit subjects
- Ensure the person is clearly visible and not heavily occluded
- Higher resolution images generally provide better results
- The application processes images in real-time, so larger images may take longer

## Technical Details

### Models Used
- **YOLOv8m**: Person detection (49.7MB)
- **YOLOv8m-pose**: Pose estimation (50.8MB)
- **Random Forest**: Pose classification (your trained model)

### Processing Pipeline
1. Image upload and validation
2. Person detection with YOLO
3. Pose landmark extraction
4. Skeleton visualization
5. Pose classification
6. Results display with confidence scores

## Contributing

Feel free to enhance the application by:
- Adding more pose classes
- Improving the UI/UX
- Adding video processing capabilities
- Implementing real-time webcam detection

## License

This project is for educational and research purposes. The trained model is based on your tennis dataset and should be used responsibly.

---

**Enjoy detecting tennis poses with AI! 🎾🤖** 