# Environment Setup Guide

## Setting Up Your Environment Variables

To keep secrets secure and avoid exposing them in version control, follow these steps:

### 1. Create your .env file
```bash
cp .env.template .env
```

### 2. Edit the .env file with your actual values
```bash
nano .env  # or use your preferred editor
```

### 3. Never commit the .env file
The `.env` file is already in `.gitignore` and should never be committed to version control.

### 4. Load environment variables in your code
Instead of hardcoding secrets, load them from environment variables:

**Python example:**
```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file
api_key = os.getenv('GOOGLE_API_KEY')
```

**Node.js example:**
```javascript
require('dotenv').config();
const apiKey = process.env.GOOGLE_API_KEY;
```

### 5. For production deployment
Set environment variables directly in your deployment platform:
- Heroku: `heroku config:set GOOGLE_API_KEY=your_key`
- Vercel: Add in dashboard under Environment Variables
- AWS: Use Parameter Store or Secrets Manager
- Docker: Use `--env-file` or `docker-compose.yml` env_file

## Security Best Practices

1. **Never hardcode secrets** in source code
2. **Use different keys** for development and production
3. **Rotate keys regularly**
4. **Use least privilege** - only grant necessary permissions
5. **Monitor for exposed secrets** using tools like TruffleHog

## Emergency Response

If you accidentally expose a secret:
1. **Immediately revoke/rotate** the exposed secret
2. **Remove from git history** using BFG Repo-Cleaner
3. **Force push** the cleaned repository
4. **Generate new secrets** and update your environment
