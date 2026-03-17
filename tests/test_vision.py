"""
Vision testing utilities for image processing and screenshot capture.

This module provides a template for working with computer vision tasks,
including image manipulation (cv2), numerical operations (numpy), and
screen capture (mss).
"""

import cv2
import numpy as np
from mss import mss


def load_image(path: str) -> np.ndarray:
    """Load an image from file path using OpenCV."""
    return cv2.imread(path)


def capture_screenshot() -> np.ndarray:
    """Capture a screenshot using mss library."""
    with mss() as sct:
        monitor = sct.monitors[1]  # Primary monitor
        screenshot = sct.grab(monitor)
        return np.array(screenshot)


def process_image(image: np.ndarray) -> np.ndarray:
    """Process an image using OpenCV operations."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


if __name__ == "__main__":
    # Example usage
    print("Vision module loaded successfully")