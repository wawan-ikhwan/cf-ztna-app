import httpx
from .cache import FunctionCacher
import os

BASE_URL_API = 'https://api.cloudflare.com/client/v4'
CF_EMAIL = os.environ.get('CF_EMAIL')
CF_API_KEY = os.environ.get('CF_API_KEY')
CF_ZTNA_ID = os.environ.get('CF_ZTNA_ID')

def uncached_list_devices() -> dict:
  headers = {
    'Content-Type': 'application/json',
    'X-Auth-Email': CF_EMAIL,
    'X-Auth-Key': CF_API_KEY,
  }
  response = httpx.get(f'{BASE_URL_API}/accounts/{CF_ZTNA_ID}/devices', headers=headers)
  return response.json()

def uncached_get_virtual_ip(DEVICE_UUID) -> dict:
  headers = {
    'Content-Type': 'application/json',
    'X-Auth-Email': CF_EMAIL,
    'X-Auth-Key': CF_API_KEY,
  }
  response = httpx.get(f'{BASE_URL_API}/accounts/{CF_ZTNA_ID}/devices/{DEVICE_UUID}/ip', headers=headers)
  return response.json()

request_list_devices = FunctionCacher(uncached_list_devices, ttl_seconds=60)
request_get_virtual_ip = FunctionCacher(uncached_get_virtual_ip, ttl_seconds=60)
