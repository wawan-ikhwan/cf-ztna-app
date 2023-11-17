from .util import request_list_devices, request_get_virtual_ip, get_ping_latency

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

import os

app = FastAPI()

origins = ["*"]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="./src/static"), name="static")

templates = Jinja2Templates(directory="./src/template")

@app.get("/api/v1/vip/{UUID}")
async def get_virtual_ip(UUID):
  return request_get_virtual_ip(UUID)

@app.get("/api/v1/devices")
async def list_devices():
  api_response_devices = request_list_devices()

  for device in api_response_devices["result"]:
    api_response_virtual_ip = request_get_virtual_ip(device["id"])
    device["vipv4"] = api_response_virtual_ip["result"]["result"]["ipv4"]
    device["vipv6"] = api_response_virtual_ip["result"]["result"]["ipv6"]
    device["ping"] = get_ping_latency(device["vipv4"])

  return api_response_devices

@app.get("/ip")
async def list_ip():
  api_response_devices = await list_devices()
  print(type(api_response_devices))
  res = ''
  for device in api_response_devices["result"]:
    res += f"{device['name']}|{device['ip']}|{device['vipv4']}|{device['vipv6']}\n"
  return PlainTextResponse(res)

# Front-End
@app.get("/", response_class=[PlainTextResponse, HTMLResponse])
async def read_root(request: Request):
  server_host = request.headers.get("Host", "")
  client_host = request.client.host

  if os.environ.get("MYIP_DOMAIN") in server_host:
    return PlainTextResponse(client_host)
  
  return templates.TemplateResponse("index.html", context={"request": request, "host": server_host, "port": 80})
  