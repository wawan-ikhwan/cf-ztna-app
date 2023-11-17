import os, sys
os.chdir(sys.path[0])

from dotenv import load_dotenv
isEnvLoaded = load_dotenv('.env')
print('Environment Load:', isEnvLoaded)
if not isEnvLoaded:
  raise Exception('Pastikan ada file .env (dotenv) dan bukannya .example.env !')

import uvicorn

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')

if __name__ == '__main__':
  uvicorn.run('src.main:app', port=int(PORT), host=HOST, reload=True)
  