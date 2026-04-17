# NMMiner HTTP API Reference

All endpoints are served on **port 80**. JSON is used for all request and response bodies unless noted otherwise.

| Item | Value |
| :--- | :---- |
| Base URL | `http://<device-ip>` |
| Content-Type | `application/json` |
| Authentication | None |
| CORS | `*` (all origins) |

---

## Table of Contents

- [Discovery & Status](#-discovery--status)
  - [GET /probe](#get-probe)
  - [GET /alive](#get-alive)
  - [GET /api/system/info](#get-apisysteminfo)
- [Settings](#%EF%B8%8F-settings)
  - [G/P /api/setting/network](#gp-apisettingnetwork)
  - [G/P /api/setting/mining](#gp-apisettingmining)
  - [G/P /api/setting/time](#gp-apisettingtime)
  - [G/P /api/setting/preference](#gp-apisettingpreference)
  - [G/P /api/setting/market](#gp-apisettingmarket)
  - [G/P /api/setting/weather](#gp-apisettingweather)
- [Market Data](#-market-data)
  - [GET /api/market/pairs](#get-apimarketpairs)
- [Weather](#-weather)
  - [POST /api/weather/refresh](#post-apiweatherrefresh)
- [System Control](#%EF%B8%8F-system-control)
  - [POST /api/swarm/find](#post-apiswarmfind)
  - [POST /api/system/restart](#post-apisystemrestart)
- [Screensaver](#-screensaver)
  - [GET /api/update/screensaver/preflight](#get-apiupdatescreensaverpreflight)
  - [POST /api/update/screensaver](#post-apiupdatescreensaver)

---

## 🔌 Discovery & Status

Endpoints used by NM Monitor for LAN device discovery and live status polling.

---

### GET `/probe`

Lightweight identity probe. Called by NM Monitor on every reachable LAN host to decide whether it is a compatible miner. `hr` and `ver` must both be present; if either is missing the host is skipped.

**Response 200**
```json
{
  "model":    "NMMiner",
  "hostname": "NMMiner-ABCD",
  "ver":      "2.1.0",
  "sw":       320,
  "sh":       240,
  "hr":       2450000000,
  "sbd":      45200000000,
  "ebd":      1230000000000,
  "ut":       5025
}
```

| Field | Description |
| :---- | :---------- |
| `model` | Device type — routes NM Monitor to `/api/system/info` |
| `hostname` | mDNS / display name |
| `ver` | Firmware version (required for discovery) |
| `sw` / `sh` | Screen width / height in pixels |
| `hr` | Hashrate in H/s (required for discovery) |
| `sbd` | Session best difficulty (H) |
| `ebd` | All-time best difficulty (H) |
| `ut` | Uptime in seconds since last boot |

---

### GET `/alive`

Returns the device's own IP and a deduplicated list of all reachable hosts found by the background LAN ping scan. Wakes the scan thread if sleeping.

> **Note** The background scan thread only runs while the device is on the **Miner** page. Calling this endpoint wakes the scan thread and resets a 30-second idle timer. If no further `/alive` request arrives within 30 s and the device has left the Miner page, the scan thread sleeps and subsequent responses return an empty `ips` list.

**Response 200**
```json
{
  "self": "192.168.1.100",
  "ips": [
    "192.168.1.100",
    "192.168.1.101",
    "192.168.1.105"
  ]
}
```

---

### GET `/api/system/info`

Full real-time snapshot: device identity, mining statistics, active stratum pool, and temperatures. Polled by NM Monitor when `/probe` returns `model = "NMMiner"`.

**Response 200**
```json
{
  "identity": {
    "hwModel":   "NMMiner",
    "hostName":  "NMMiner-ABCD",
    "fwVersion": "2.1.0",
    "rssi":      -62
  },
  "miner": {
    "hashRate":        2.45,
    "sAccepted":       42,
    "sRejected":       0,
    "uptimeSeconds":   5025,
    "uptimeEver":      86400,
    "networkDiff":     "92.67T",
    "poolDiff":        "8.00K",
    "lastDiff":        "12.30K",
    "bestDiffSession": "45.20K",
    "bestDiffEver":    "1.23M",
    "blkhits":         0,
    "freeHeap":        145408,
    "minFreeHeap":     131072
  },
  "stratum": {
    "url":  "public-pool.io:21496",
    "user": "18dK8EfyepKuS74fs27iuDJWoGUT4rPto1.worker"
  },
  "temps": {
    "vcore": 42.5,
    "asic":  null
  },
  "storage": {
    "fsTotal": 393216,
    "fsUsed":  262144
  }
}
```

| Field | Description |
| :---- | :---------- |
| `identity.rssi` | Wi-Fi signal strength in dBm |
| `miner.hashRate` | Current hashrate in GH/s |
| `miner.uptimeSeconds` | Seconds since last boot |
| `miner.uptimeEver` | Cumulative seconds (NVS + session) |
| `temps.vcore` | Core temperature in °C; `null` if sensor absent |
| `storage.fsTotal` / `fsUsed` | LittleFS total / used bytes |

---

## ⚙️ Settings

All settings endpoints support **partial updates** — include only the keys you want to change. Changes are persisted to NVS flash. The Wi-Fi password is never returned in GET responses.

---

### G/P `/api/setting/network`

Read or update hostname and Wi-Fi credentials.

> **Note** Only include the Wi-Fi password when you actually want to change it. Credential changes require a reboot to reconnect.

**GET Response 200**
```json
{
  "Hostname": "NMMiner-ABCD",
  "WiFiSSID": "MyNetwork"
}
```

**POST Request Body** *(all keys optional)*
```json
{
  "Hostname": "NMMiner-NEW",
  "WiFiSSID": "MyNetwork",
  "WiFiPWD":  "newpassword"
}
```

**POST Response 200** — `OK` (text/plain)

---

### G/P `/api/setting/mining`

Read or update stratum pool configuration. New pool connection takes effect after reboot.

**GET Response 200**
```json
{
  "PrimaryPool":       "stratum+tcp://public-pool.io:21496",
  "PrimaryAddress":    "18dK8EfyepKuS74fs27iuDJWoGUT4rPto1.worker",
  "PrimaryPassword":   "x",
  "SecondaryPool":     "stratum+tcp://pool.tazmining.ch:33333",
  "SecondaryAddress":  "18dK8EfyepKuS74fs27iuDJWoGUT4rPto1.worker",
  "SecondaryPassword": "x"
}
```

**POST Request Body** *(all keys optional)*
```json
{
  "PrimaryPool":       "stratum+tcp://pool.example.com:3333",
  "PrimaryAddress":    "yourWallet.worker",
  "PrimaryPassword":   "x",
  "SecondaryPool":     "stratum+tcp://backup.example.com:3333",
  "SecondaryAddress":  "yourWallet.worker",
  "SecondaryPassword": "x"
}
```

**POST Response 200** — `OK` (text/plain)

---

### G/P `/api/setting/time`

Read or update time and date settings. `Timezone`, `TimeFormat`, and `DateFormat` all take effect immediately on the device display without a reboot.

**GET Response 200**
```json
{
  "Timezone":   "Asia/Shanghai",
  "TimeFormat": 24,
  "DateFormat": "YYYY-MM-DD"
}
```

| Field | Values |
| :---- | :----- |
| `Timezone` | IANA timezone string |
| `TimeFormat` | `12` or `24` |
| `DateFormat` | `"YYYY-MM-DD"` \| `"MM/DD/YYYY"` \| `"DD/MM/YYYY"` |

**POST Request Body** *(all keys optional)*
```json
{
  "Timezone":   "America/New_York",
  "TimeFormat": 12,
  "DateFormat": "MM/DD/YYYY"
}
```

**POST Response 200** — `OK` (text/plain)

---

### G/P `/api/setting/preference`

Read or update display and LED preferences. `Brightness`, `RotateScreen`, and `ScreenSaver` take effect immediately. `LedEnable` requires a reboot.

**GET Response 200**
```json
{
  "Brightness":   80,
  "RotateScreen": 270,
  "LedEnable":    1,
  "ScreenSaver":  "never"
}
```

| Field | Values |
| :---- | :----- |
| `Brightness` | `1` – `100` |
| `RotateScreen` | `0` \| `90` \| `180` \| `270` |
| `LedEnable` | `0` = off, `1` = on |
| `ScreenSaver` | `"never"` \| `"30s"` \| `"1m"` \| `"5m"` \| `"15m"` \| `"30m"` |

**POST Request Body** *(all keys optional)*
```json
{
  "Brightness":   60,
  "RotateScreen": 90,
  "LedEnable":    0,
  "ScreenSaver":  "5m"
}
```

**POST Response 200** — `OK` (text/plain)

---

### G/P `/api/setting/market`

Read or update market display settings. After saving, the market task triggers an immediate data refresh — no reboot required. `WatchCoins` is silently truncated to 20 symbols.

**GET Response 200**
```json
{
  "MainCoin":      "BTC",
  "WatchCoins":    "ETH,BNB,SOL",
  "KlineRotate":   "30s",
  "PricePageMode": "kline"
}
```

| Field | Values |
| :---- | :----- |
| `MainCoin` | Primary coin shown on price page |
| `WatchCoins` | Comma-separated watchlist (max 20 symbols) |
| `KlineRotate` | `"never"` \| `"10s"` \| `"30s"` \| `"60s"` |
| `PricePageMode` | `"kline"` \| `"ticker"` |

**POST Request Body** *(all keys optional)*
```json
{
  "MainCoin":      "ETH",
  "WatchCoins":    "BTC,BNB,SOL,XRP",
  "KlineRotate":   "60s",
  "PricePageMode": "ticker"
}
```

**POST Response 200** — `OK` (text/plain)

---

### G/P `/api/setting/weather`

Read or update weather location. After saving, the weather task triggers an immediate data fetch — no reboot required.

**GET Response 200**
```json
{
  "WeatherCity": "Beijing, Beijing, China",
  "WeatherLat":  "39.9075",
  "WeatherLon":  "116.3972"
}
```

**POST Request Body** *(all keys optional)*
```json
{
  "WeatherCity": "Tokyo, Tokyo, Japan",
  "WeatherLat":  "35.6762",
  "WeatherLon":  "139.6503"
}
```

**POST Response 200** — `OK` (text/plain)

---

## 📈 Market Data

Read-only market data cached on the device from Binance.

---

### GET `/api/market/pairs`

Returns a cached list of USDT trading pair base symbols fetched from Binance. Used by the settings page to populate coin selection dropdowns. The list may be empty shortly after first boot.

> **Note** The market data thread only runs while the device is on the **Miner**, **Clock**, or **Price** page. If the device is on the **Loading**, **Config**, or **Weather** page, the market thread is asleep and this endpoint returns an empty array `[]`.

**Response 200**
```json
["BTC", "ETH", "BNB", "SOL", "XRP", "DOGE", "ADA", "TRX", ...]
```

---

## 🌤 Weather

---

### POST `/api/weather/refresh`

Triggers an immediate weather + AQI fetch, bypassing the normal polling interval. Rate-limited to once per 60 seconds.

**Request Body**
```json
{}
```

**Response 200** — `OK` (text/plain)

**Response 429** — `Rate limited, please wait 42s before refreshing again.` (text/plain)

---

## 🛠️ System Control

---

### POST `/api/swarm/find`

Triggers a brief visual alert (screen flash / LED blink) on the physical device to help identify it among multiple units on the same network.

**Request Body**
```json
{}
```

**Response 200**
```json
{ "status": "ok" }
```

---

### POST `/api/system/restart`

Triggers an immediate software reboot. The HTTP 200 response is delivered before the reboot sequence starts (~600 ms delay).

> **Warning** The device will be unreachable for several seconds while rebooting.

**Request Body**
```json
{}
```

**Response 200**
```json
{ "status": "ok" }
```

---

## 🌄 Screensaver

Upload custom screensaver images to the device. Files must be in the NMMiner `.ss` binary format (RGB565 + RLE/Huffman compression). Each file is named `saver_{W}_{H}_{NNN}.ss` where W×H matches the device screen resolution.

---

### GET `/api/update/screensaver/preflight`

Call before uploading a `.ss` file to check available space or whether older files must be removed.

**Query Parameters**

| Parameter | Required | Description |
| :-------- | :------: | :---------- |
| `size` | ✓ | File size in bytes |

**Response 200**
```json
{
  "fileSize":       81920,
  "fsFree":         118784,
  "maxUploadable":  204800,
  "action":         "new",
  "overwriteCount": 0,
  "overwriteFiles": [],
  "existingCount":  2,
  "spaceAfter":     36864
}
```

| `action` | Meaning |
| :------- | :------ |
| `"new"` | Enough free space for the new file |
| `"overwrite"` | Old files must be deleted to make room |
| `"reject"` | Not enough space even after deleting old files |

**Error Responses**
- `400` — Missing `size` parameter
- `400` — Invalid `size` value

---

### POST `/api/update/screensaver`

Upload a `.ss` binary file via `multipart/form-data`. The firmware validates the file header (magic `0x4E53`) in the first chunk and rejects invalid files immediately. If free space is insufficient, the oldest matching screensaver file(s) are automatically deleted to make room.

> **Warning** Maximum file size is **200 KB**. Files exceeding this limit are rejected with HTTP 413.

**Request**
```
Content-Type: multipart/form-data

file: <binary .ss data>   // field name: any (filename must end in .ss)
```

**Response 200**
```json
{
  "status": "ok",
  "path":   "/ss/saver_320_240_003.ss"
}
```

**Error Responses**
- `400` — Only `.ss` files are accepted
- `400` — Invalid `.ss` file header
- `413` — File too large (max 200 KB)
- `500` — Failed to open file for writing
- `500` — Write error
