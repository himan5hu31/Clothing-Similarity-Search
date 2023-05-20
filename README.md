# Clothing Similarity Search

## Overview

Clothing Similarity Search is a machine learning project that focuses on providing users with a convenient way to find similar clothing items based on text descriptions. The project utilizes a machine learning model deployed on Google Cloud to analyze the input text and generate a ranked list of links to similar clothing items available on various websites.

## How It Works

1. **Input**: The user provides a text description of a clothing item.
2. **Model Processing**: The machine learning model processes the input text and extracts relevant features that capture the clothing item's characteristics.
3. **Similarity Calculation**: The model computes the similarity between the input text and the text descriptions of clothing items in its database.
4. **Ranking**: Based on the calculated similarity scores, the model ranks the clothing items from most similar to least similar.
5. **Results**: The model returns a JSON response containing a ranked list of links to similar clothing items on different websites.

### Example
```
import requests
response= requests.post("https://rankpedict-nxlb6twtva-as.a.run.app",
                    json={"text": "western denim black jeans color "})
                    
print(response.json())

{'product_link': 'https://www.amazon.com/Cinch-White-Relaxed-Mid-Rise-Stonewash/dp/B07F5LHFKY/ref=sr_1_2200?crid=1DVUGE5NG5UUO&keywords=men+fashion&qid=1684499787&rnid=7141123011&s=apparel&sprefix=menfashion%2Caps%2C282&sr=1-2200', 'productname': 'cinch western denim jeans mens white label low dark wash mb'}, 
{'product_link': 'https://www.flipkart.com/crishtaliyo-regular-men-black-jeans/p/itmbe5b4e877bc50?pid=JEAGZS88EFQYXKJ9&lid=LSTJEAGZS88EFQYXKJ9B7OOIP&marketplace=FLIPKART&store=clo&srno=b_20_779&otracker=browse&fm=organic&iid=d54f2af1-65b8-48dd-9240-354ef9fd2067.JEAGZS88EFQYXKJ9.SEARCH&ppt=None&ppn=None&ssid=o98bgb7ojk0000001684497563652', 'productname': 'men regular high rise black jeans'},
{'product_link': 'https://www.flipkart.com/highlander-tapered-fit-men-black-jeans/p/itm6706765bca917?pid=JEAGA5JKH3BBGQFH&lid=LSTJEAGA5JKH3BBGQFHIDTBNS&marketplace=FLIPKART&store=clo%2Fvua&srno=b_8_309&otracker=browse&fm=organic&iid=61d2aecd-bf8b-4d37-aa0a-957adc3f0ed1.JEAGA5JKH3BBGQFH.SEARCH&ppt=None&ppn=None&ssid=hrs7lxbdrk0000001684505882013', 'productname': 'men tapered fit low rise black jeans'},
```
## Project Structure

The project repository includes the following files:

- `.dockerignore`: Specifies files and directories to be excluded when building Docker images.
- `Dockerfile`: Configuration file for building a Docker image of the project.
- `README.md`: This file, providing an overview and instructions for the project.
- `main.py`: Python script containing the implementation of the clothing similarity search function.
- `requirements.txt`: List of Python dependencies required for running the project.

## Getting Started

To use the Clothing Similarity Search project, follow these steps:

1. Install the required dependencies specified in `requirements.txt`.
2. Run the `main.py` script to start the similarity search function.
3. Provide a text description of a clothing item as input.
4. Retrieve the JSON response containing the ranked list of similar clothing items' links.

## Directory structure

The directory structure for the Clothing Similarity Search project is as follows:

```
Clothing-Similarity-Search/
├── GCP/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   └── templates/
│       └── index.html
├── Dockerfile
├── .dockerignore
├── main.py
├── requirements.txt
├── webscraping/
│   ├── data/
│   └── scripts/
│       ├── amazon_data.py
│       └── flipkart_data.py
└── README.md
```

- `GCP/`: Directory for the web application deployed on Google Cloud Platform (GCP).
  - `static/`: Directory for static files used by the web application.
    - `css/`: Directory for CSS files.
      - `style.css`: CSS file for styling the web application.
  - `templates/`: Directory for HTML templates used by the web application.
    - `index.html`: HTML template for the main page of the web application.

- `Dockerfile`: Configuration file for building a Docker image of the project.

- `.dockerignore`: Specifies files and directories to be excluded when building Docker images.

- `main.py`: Python script containing the implementation of the clothing similarity search function and web application.

- `requirements.txt`: List of Python dependencies required for running the project.

- `webscraping/`: Directory for web scraping-related scripts and data.
  - `data/`: Directory for storing data obtained from web scraping.
  - `scripts/`: Directory for web scraping scripts.
    - `amazon_data.py`: Python script for scraping clothing item data from Amazon.
    - `flipkart_data.py`: Python script for scraping clothing item data from Flipkart.

- `README.md`: README file providing an overview and instructions for the project.

This updated directory structure reflects the addition of directories specific to web application development and web scraping tasks. The web application files are organized under the `GCP/` directory, and the web scraping scripts and data are stored under the `webscraping/` directory.


## Deployment

The project is deployed on Google Cloud. You can access the clothing similarity search function as a web service by deploying it on Google Cloud Functions or Google Cloud Run. Once deployed, you can send HTTP requests to the function and receive JSON responses with ranked suggestions.
#### 1. Write App (Flask)
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

If you have any questions or inquiries regarding the project, please contact :
We appreciate your interest and hope that Clothing Similarity Search proves to be a valuable tool for finding similar clothing items based on text descriptions.
