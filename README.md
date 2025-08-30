# FastAPI Hello API

A simple FastAPI application with automated CI/CD deployment using GitHub Actions.

## Features

- `/` - Root endpoint
- `/hello` - Hello world endpoint
- `/health` - Health check endpoint

## Local Development

1. Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

2. Run the application:
\`\`\`bash
uvicorn main:app --reload
\`\`\`

3. Visit `http://localhost:8000` to see the API
4. Visit `http://localhost:8000/docs` for interactive API documentation

## Deployment Setup

### GitHub Secrets Required

Add these secrets to your GitHub repository (Settings > Secrets and variables > Actions):

1. `SERVER_IP` - Your server's IP address
2. `SERVER_USERNAME` - SSH username for your server
3. `SSH_PRIVATE_KEY` - Your SSH private key content

### SSH Key Setup

1. Generate SSH key pair on your local machine:
\`\`\`bash
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
\`\`\`

2. Copy public key to your server:
\`\`\`bash
ssh-copy-id username@your-server-ip
\`\`\`

3. Add the private key content to GitHub secrets as `SSH_PRIVATE_KEY`

### Server Requirements

- Python 3.11+
- Git installed
- SSH access enabled

## CI/CD Pipeline

The GitHub Actions workflow will:
1. Run tests on every push/PR
2. Deploy to server only on main branch pushes
3. Automatically restart the FastAPI service
4. Verify deployment success

## Testing

Run tests locally:
\`\`\`bash
pytest test_main.py -v
