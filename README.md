# CSC Exercise

This FastAPI backend allows users to retrieve their starred repositories from GitHub.

## Configuration

Before running the application, you need to set up a GitHub OAuth application to obtain the client ID and secret. Follow these steps:

1. Go to [GitHub Developer Settings](https://github.com/settings/developers).
2. Click on "New OAuth App" button.
3. Fill in the required information:
   - Application name: Choose a name for the application.
   - Homepage URL: `http://127.0.0.1:8000/start`
   - Authorization callback URL: `http://127.0.0.1:8000/callback`.
4. Click on "Register application" to create the OAuth application.
5. Once the application is registered, note down the "Client ID" and "Client Secret".

## Running the Application

To run the application locally, follow these steps:

1. Clone the repository:

```
git clone https://github.com/Piketulus/CSCexercise
cd CSCexercise
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Set up GitHub client ID and secret:

Replace `"GITHUB_CLIENT_ID"` and `"GITHUB_CLIENT_SECRET"` on lines [9](https://github.com/Piketulus/CSCexercise/blob/0f3af6b447d5b986bc3ee998030635ba727b77ee/main.py#L9) and [10](https://github.com/Piketulus/CSCexercise/blob/6ff627e2c3328f46d9f8d48a6aa2e428376f8c1c/main.py#L10) with the client ID and secret obtained from GitHub OAuth application.

4. Run the application using Uvicorn:

```
uvicorn main:app --reload
```

## Usage

- Navigate to `http://127.0.0.1:8000/start` or `http://localhost:8000/start` endpoint to initiate the OAuth login flow.
- After authentication and authorization with GitHub, you will be redirected back to the application, which will have returned the info on the starred repositories in JSON format.
