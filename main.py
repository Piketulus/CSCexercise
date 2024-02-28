from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from starlette.requests import Request
import httpx


app = FastAPI()

github_client_id = "GITHUB_CLIENT_ID"
github_client_secret = "GITHUB_CLIENT_SECRET"

@app.get("/start")
async def start(request: Request):
    return RedirectResponse(url=f"https://github.com/login/oauth/authorize?client_id={github_client_id}")

@app.get("/callback")
async def callback(code: str):
    # Exchange code for access token
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://github.com/login/oauth/access_token",
            data={
                "client_id": github_client_id,
                "client_secret": github_client_secret,
                "code": code
            },
            headers={"Accept": "application/json"}
        )
        data = response.json()
        access_token = data["access_token"]

    # Use access token to get user's starred repositories
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.github.com/user/starred",
            headers={"Authorization": "Bearer " + access_token}
        )
        starred_repos = response.json()

    # Filter out private repositories and extract required information
    starred_repos_info = {
        "total_count": len(starred_repos),
        "repositories": []
    }
    for repo in starred_repos:
        if not repo["private"]:
            repo_info = {
                "name": repo["name"],
                "description": repo["description"],
                "url": repo["html_url"],
                "license": repo["license"]["name"] if repo["license"] else None,
                "topics": repo["topics"]
            }
            starred_repos_info["repositories"].append(repo_info)

    return JSONResponse(starred_repos_info)
