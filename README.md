
# Amharic Real Time Sign Language Detection And Interpretation


### Description:

This repository contains a custom-made dataset consisting of 45 signs in the Amharic Language, a widely spoken language in Ethiopia. The dataset is specifically tailored for training a machine learning model named YOLOV8 for object detection tasks.


### Installation:

    To install and set up the application, follow these steps:

    1. Clone this repository to your local machine:
        ```
        git clone https://github.com/AbrhamWendmeneh/Amharic-Sign-language-Interpreter.git
        ```
    2. Install the necessary dependencies


### Usage:
    To use the application, follow these steps:

    1. Import the required libraries:
        ```python
        import cv2
        import numpy as np
        from ultralytics import YOLO
        ```

    2. Define the function to patch the image:
        ```python
        def patch_image(img, results):
            # Implementation details provided in the source code
            ...
        ```

    3. Load the YOLOV8 model:
        ```python
        model = YOLO('best.pt')
        ```

    4. Capture video from the camera and perform object detection:
        ```python
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            # Implementation details provided in the source code
            ...
        ```

###  Features:
    - Custom-made dataset containing 45 signs in the Amharic Language.
    - Trained YOLOV8 model for object detection tasks.
    - Real-time object detection capabilities using OpenCV.


###  Contributing:

Contributions to this project are welcome. If you find any issues or would like to suggest improvements, please follow these guidelines:

- Report bugs by opening an issue on GitHub.
- Suggest new features or enhancements through GitHub discussions.
- Submit code changes via pull requests. Please ensure that your code follows the repository's coding standards and follow these steps to contribute code:

    - Fork the repository to your GitHub account.
    - Create a new branch for your changes based on the `main` branch.
    - Make your desired changes to the codebase.
    - Test your changes thoroughly to ensure they do not introduce any new issues.
    - Commit your changes with descriptive commit messages.
    - Push your changes to your forked repository.
    - Open a pull request to the original repository, clearly explaining the purpose of your changes.

- Code Style and Guidelines:

    - Adhere to the coding style and guidelines used in the project. Familiarize yourself with the existing codebase and maintain consistency with naming conventions, code structure, and formatting.

- Review Process:

    - Your pull requests will undergo a review process by project maintainers. Please be patient during this review process, and be prepared to address any feedback or suggestions for improvement.

-Collaboration and Communication:

    - Feel free to engage with other contributors and project maintainers through GitHub discussions, comments on pull requests, or other communication channels. Collaboration and constructive feedback are key to the success of the project.


### Contact:

For support or inquiries, you can reach out to us through the following channels:

- Email: [abrham.wendmeneh.a@gmail.com](mailto:abrham.wendmeneh.a@gmail.com)
- GitHub: [AbrhamWendmeneh](https://github.com//AbrhamWendmeneh//)

- Email: [fraolmulugeta17@gmail.com](mailto:fraolmulugeta17@gmail.com)
- GitHub: [Fraol7](https://github.com//Fraol7//)

We are here to assist you and address any questions or concerns you may have regarding this project. Don't hesitate to reach out!


Credits:

- The Amharic Sign Dataset was created by [Fraol Mulugeta].
- The YOLOV8 model is provided by the Ultralytics team.

We would like to extend our appreciation to the developers of the YOLO8 (You Only Look Once) object detection method, which played a crucial role in the development of our **Amharic Sign Language Interpreter**. YOLO8 is a state-of-the-art deep learning-based object detection algorithm that offers efficient and accurate real-time object detection in images. Its robustness and performance have significantly contributed to the effectiveness of our app in **interpreting Amharic sign language in real-time**. We are grateful for the innovative work and contributions of the YOLO8 team, which have enabled us to make this system in better way.
