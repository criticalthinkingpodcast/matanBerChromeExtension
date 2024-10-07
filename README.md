# Image Uploader Demo App

This is a demo application created for MatanBer's Chrome extension hacking demonstrations. It's a simple web app that allows users to upload and view images, secured by an API token.

## Purpose

This application serves as a controlled environment for demonstrating various aspects of Chrome extension development and potential security considerations. It's not intended for production use and should only be used for educational purposes.

## Features

- Image upload via web interface
- API token authentication
- Display of uploaded images
- Dockerized for easy deployment

## Prerequisites

To run this application, you need to have the following installed on your system:

- Docker
- Docker Compose

## Getting Started

Follow these steps to spin up the Docker container and run the application:

1. Clone this repository to your local machine.

2. Navigate to the project directory in your terminal.

3. Build and start the Docker container using Docker Compose:

   ```
   docker-compose up --build
   ```

4. Open a web browser and go to `http://localhost:8000`.

5. You'll see the API token displayed on the page. You can now use the web interface to upload images and view them.

## Important Notes

- This is a demo application and should not be used in a production environment.
- Uploaded images are stored within the Docker container and will be lost when the container is removed. For persistence between container restarts, you can modify the Docker volume configuration.

## Shutting Down

To stop the application, use `Ctrl+C` in the terminal where the Docker container is running, or run the following command in the project directory:
