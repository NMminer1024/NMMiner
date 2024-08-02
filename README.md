# NMMiner - New ESP32 Solo Miner

- Deeply Optimazion for ESP32-S3: Achieves high performance of 117kH/s with a single chip in solo miner mode, while maintaining low power consumption.

## Requirements

- [Heltec Vision Master T190](https://www.aliexpress.us/item/1005007449552504.html)
- [Putty](https://www.putty.org/)
- 3D BOX (not supported now, coming soon)

## Features

<div align="center">
  <img src="fig/hashrate.png" alt="hashrate">
</div>

- SHA256d deeply Optimazation for ESP32-S3, max hashrate: 117 KH/s

<div align="center">
  <img src="fig/share.png" alt="share">
</div>

The testing Hashrate from the public-pool:

![pool](fig/pool.png)

## Install and Start

### Flash Binary

- Download the binary file, just click **tool/download.bat** if you have got a correct board.

  Following items should be adjust to fit your environment first before execute **download.bat**：

<div align="center">
  <img src="fig/download.jpg" alt="download">
</div>


- Please wait patiently for the download to be completed.

- If it's the first time you download the firmware, you may got a configuration request on screen to remind you config the miner. just config it as [NMMiner Configuration](#nmminer-configuration)

- Open a tool something like **putty**, the machine log will rolling in putty.


### Buttons

| Buttons           | Action             | Description             |
| :---------------  | :-----------------:|:-----------------:      |
|user               | Single click       |      Screen wake up     |
|user               | Double click       |  Switch to next screen    |
|user               | Hold on when power on       |      Miner Configuration      |
|boot               | Long press after boot       |  Clear all status in nvs(if enabled this feature)  |

### NMMiner Configuration

1. Hold on the **user** button, then reset, wait until a QR code appeared.

<div align="center">
  <img src="fig/nmap.png" alt="AP Config">
</div>

2. Seach a AP named: nmap-2.4g, pwd: 12345678

3. Connect the AP via your phone, if everything goes well, it will jump to the configuration page directly.

4. Connect the AP via a PC, just login to: 192.168.4.1

5. Keep all parameters default except BTC address and wifi.

<div align="center">
  <img src="fig/config.jpg" alt="config">
</div>

6. You can back to the configuration page anytime via a action hold on the user button when power on.

7. Enabled the SSL option if you know what you did.


## How to Usage

ESP32 implementing Stratum protocol to mine on solo pool. Pool can be changed but originally works with [public-pool.io](https://web.public-pool.io/)


## Contact
- We are committed to supporting more models of Arduino development boards.
- Anything not work as your expectation, just let us know.

| Email                   |
| :-----------------:     |
|nmminer1024@gmail.com    |


##  Useful documentation:

- [Solominer](https://github.com/iceland2k14/solominer/blob/main/solo_miner.py)
- [pyminer.py](https://github.com/jgarzik/pyminer/blob/master/pyminer.py)
- [Stratum Protocol](https://reference.cash/mining/stratum-protocol)
- [Stratum Protocol Diagram](https://github.com/aeternity/protocol/blob/master/STRATUM.md)
- [NBits](https://learnmeabitcoin.com/technical/bits)
- [Bitcoin Mining](https://www.righto.com/2014/02/bitcoin-mining-hard-way-algorithms.html)
- [How To Mine](https://gist.github.com/Ending2015a/70373b2f6f665a765b4d0b0c427f052b)
- [Image Converter 565](http://www.rinkydinkelectronics.com/t_imageconverter565.php)
- [Lilygo-T-Display-S3](https://github.com/Xinyuan-LilyGO/T-Display-S3/tree/main)
- [HAN](https://github.com/valerio-vaccaro/HAN)
- [NerdMinerv2](https://github.com/BitMaker-hub/NerdMiner_v2)
- [Jade](https://github.com/Blockstream/Jade/tree/miner_all_0.1.47/components/miner)
- [LeafMiner](https://github.com/matteocrippa/leafminer)

## Release Log

### (2024.08.02) - v0.1.54
- Features:
  - BTC solo miner base on esp32s3 series 
  - Up to **117kH/s** 
  - ssl connection support
  - Screen auto off in 60s
  - Real time clock
  - Configuration on websever, it's easy enough to build your first BTC Miner.
  - WiFi Signal Strength add.
- Fixed:
  - Some issues after full chip erase.
- Modify:
  - None
- Baord support
  - [Heltec Vision Master T190](https://www.aliexpress.us/item/1005007449552504.html)


### (2024.08.01) - v0.1.53
- Features:
  - BTC solo miner base on esp32s3 series 
  - Up to **117kH/s** 
  - ssl connection support
  - Screen auto off in 60s
  - Real time clock
  - Configuration on websever, it's easy enough to build your first BTC Miner.
  - WiFi Signal Strength add.
- Fixed:
  - Fixed default WiFi parameters issues.
  - Fixed parameter of 'screen off time out'.
- Modify:
  - Some nvs handles, not compatible with v0.1.52.
- Baord support
  - heltec-vision-master-t190 

### (2024.07.31) - v0.1.52
- Features:
  - BTC solo miner base on esp32s3 series 
  - Up to **117kH/s** 
  - ssl connection support
  - Screen auto off in 60s, can be setted from the Configuration Page
  - Real-time clock
  - Configuration on webserver, it's easy enough to build your first BTC Miner.
- Fixed:
  - First push 
- Modify:
  - None
- Board support
  - [Heltec Vision Master T190](https://www.aliexpress.us/item/1005007449552504.html)
