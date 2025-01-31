# HNG Stage 0 Backend Task - Public API

## Description

This is a simple FastAPI-based public API that returns:

- My registered HNG email
- Current datetime in ISO 8601 format
- Link to this GitHub repository

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/mayowa-kalejaiye/hng-stage0-task.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the API:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

4. Open in browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API Endpoint

- **URL:** `https://hng-stage0-task-ewk2.onrender.com`
- **Method:** GET
- **Response Example:**

  ```json
  {
    "email": "kalejaiyemayowa3@gmail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/mayowa-kalejaiye/hng-stage0-task.git"
  }
  ```

## API Documentation

### Endpoint URL

The endpoint for this API is:

   ```curl
      GET https://hng-stage0-task-ewk2.onrender.com
   ```

### Request Format

This API does not require any parameters in the request. It only accepts GET requests.

- **Method:** GET
- **Headers:** None required.

### Response Format

The response will be in JSON format.

```json
{
  "email": "kalejaiyemayowa3@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/mayowa-kalejaiye/hng-stage0-task.git"
}
```

- **email:** The email address used to register on the HNG12 Slack workspace.
- **current_datetime:** The current UTC datetime in ISO 8601 format (e.g., 2025-01-30T09:30:00Z).
- **github_url:** The URL of the GitHub repository hosting the project.

### Example Usage

#### Request Example

Send a GET request to the endpoint:

   ```curl
      GET https://hng-stage0-task-ewk2.onrender.com
   ```

#### Response Example

On success (200 OK), the response will look like:

```json
{
  "email": "kalejaiyemayowa3@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/mayowa-kalejaiye/hng-stage0-task.git"
}
```

### Additional Notes

- Ensure that the deployment is publicly accessible to receive requests.
- The `current_datetime` is dynamically generated when the request is made.

## Deployment

This API is hosted on Render.

## More Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [HNG Python Developers](https://hng.tech/hire/python-developers)
