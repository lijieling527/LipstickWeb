{
  "version": 2,
  "builds": [
    {
      "src": "manager.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/$1.py"
    },
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ]
}
