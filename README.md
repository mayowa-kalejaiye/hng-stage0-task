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
- **URL:** `<your-deployed-url>`
- **Method:** GET
- **Response Example:**
  ```json
  {
    "email": "kalejaiyemayowa3@gmail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/mayowa-kalejaiye/hng-stage0-task.git"
  }
  ```

## Deployment
This API is hosted on Render / Railway.

## More Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [HNG Python Developers](https://hng.tech/)
