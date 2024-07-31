# CarDataAPI

This project is a REST API built with FastAPI to manage car product details. It is designed to be run with Docker and docker-compose.

## Endpoints

- `GET /get_products`: Returns a list of three products with their short descriptions.
- `GET /get_products/{product_id}`: Returns detailed information for a product by ID (length, engine type and price).
- `POST /set_price/{product_id}`: Sets the price for a specified product.

## Requirements

- Python 3.7+
- Docker
- Docker-compose

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/tarolih/CarDataAPI.git
    cd CarDataAPI
    ```

2. **Build and run the Docker containers**:
    ```bash
    docker-compose up --build
    ```

3. The API will be available at `http://localhost:8080`.

## Example Requests (or use Postman)

- **Get products**:
    ```bash
    curl -X GET "http://localhost:8080/get_products"
    ```

- **Get product details**:
    ```bash
    curl -X GET "http://localhost:8080/get_products/1"
    ```

- **Set product price**:
    ```bash
    curl -X POST "http://localhost:8080/set_price/1" -H "Content-Type: application/json" -d '{"price": 12000}'
    ```

## Project Structure

- `app/main.py`: Contains the API routes.
- `app/models.py`: Defines the Product model and the in-memory database.
- `Dockerfile`: Docker configuration for the FastAPI app.
- `docker-compose.yml`: Docker Compose configuration to run the application.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Specifies files and directories to be ignored by git.
- `tests/test_main.py`: Contains the test cases for the API endpoints.

## Running Tests

To run the tests for this project using Docker Compose, follow these steps:

1. **Build and run the tests**:
    ```bash
    docker-compose run test
    ```