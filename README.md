# Clothing Similarity Search

## Overview

Clothing Similarity Search is a machine learning project that focuses on providing users with a convenient way to find similar clothing items based on text descriptions. The project utilizes a machine learning model deployed on Google Cloud to analyze the input text and generate a ranked list of links to similar clothing items available on various websites.

## How It Works

1. **Input**: The user provides a text description of a clothing item.
2. **Model Processing**: The machine learning model processes the input text and extracts relevant features that capture the clothing item's characteristics.
3. **Similarity Calculation**: The model computes the similarity between the input text and the text descriptions of clothing items in its database.
4. **Ranking**: Based on the calculated similarity scores, the model ranks the clothing items from most similar to least similar.
5. **Results**: The model returns a JSON response containing a ranked list of links to similar clothing items on different websites.

## Project Structure

The project repository includes the following files:

- `.dockerignore`: Specifies files and directories to be excluded when building Docker images.
- `Dockerfile`: Configuration file for building a Docker image of the project.
- `README.md`: This file, providing an overview and instructions for the project.
- `main.py`: Python script containing the implementation of the clothing similarity search function.
- `nn.h5`: Serialized machine learning model for similarity calculation.
- `requirements.txt`: List of Python dependencies required for running the project.

## Getting Started

To use the Clothing Similarity Search project, follow these steps:

1. Install the required dependencies specified in `requirements.txt`.
2. Run the `main.py` script to start the similarity search function.
3. Provide a text description of a clothing item as input.
4. Retrieve the JSON response containing the ranked list of similar clothing items' links.

## Deployment

The project is deployed on Google Cloud. You can access the clothing similarity search function as a web service by deploying it on Google Cloud Functions or Google Cloud Run. Once deployed, you can send HTTP requests to the function and receive JSON responses with ranked suggestions.
#### 1. Write App (Flask, TensorFlow)
- The code to build, train, and save the model is in the `test` folder.
- Implement the app in `main.py`
#### 2. Setup Google Cloud 
- Create new project
- Activate Cloud Run API and Cloud Build API

#### 3. Install and init Google Cloud SDK
- https://cloud.google.com/sdk/docs/install

#### 4. Dockerfile, requirements.txt, .dockerignore
- https://cloud.google.com/run/docs/quickstarts/build-and-deploy#containerizing

#### 5. Cloud build & deploy
```
gcloud builds submit --tag gcr.io/<project_id>/<function_name>
gcloud run deploy --image gcr.io/<project_id>/<function_name> --platform managed
```
## Contributing

Contributions to the Clothing Similarity Search project are welcome! If you find any issues or have suggestions for improvements, please submit them through the project's issue tracker.

## License

The Clothing Similarity Search project is open-source and available under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

## Contact

If you have any questions or inquiries regarding the project, please contact the project maintainers:

- Name: [Your Name]
- Email: [Your Email]

We appreciate your interest and hope that Clothing Similarity Search proves to be a valuable tool for finding similar clothing items based on text descriptions.
