# NMMiner - New ESP32 Solo Miner

- Deeply optimazion for ESP32-S3: Achieves high performance of 117kH/s with a single chip in solo miner mode, while maintaining low power consumption.

## Requirements

- [Heltec Vision Master T190](https://www.aliexpress.us/item/1005007449552504.html)
- [Putty](https://www.putty.org/)
- 3D BOX (not supported now, coming soon)

## Features

<div align="center">
  <img src="fig/hashrate.png" alt="hashrate">
</div>

- SHA256d deeply optimazation for ESP32-S3, max hashrate: 117 KH/s

<div align="center">
  <img src="fig/share.jpg" alt="share">
</div>

- The testing Hashrate from the public-pool:

<div align="center">
  <img src="fig/pool.png" alt="pool">
</div>

### Buttons

| Buttons           | Action             | Description             |
| :---------------  | :-----------------:|:-----------------:      |
|user               | Single click       |  Screen wake up         |
|user               | Double click       |  Switch to next screen  |
|user               | [Press and hold before reset](#normal-configuration)  |  Miner Configuration    |
|boot               | Long press         |  Clear all status from nvs(if enabled this feature)  |
|boot               | Single click       |  Screen wake up         |


### NMMiner Configuration
***
#### Normal configuration

1. Press and hold the **User** button, then click the **Reset** button, wait until the QR code appears, then release the **User** button.

<div align="center">
  <img src="fig/nmap.png" alt="AP Config">
</div>

2. Search for AP named: nmap-2.4g, enter password: 12345678

3.  If connect to AP via mobile phone and everything goes well, you will be redirected to the configuration page; if connect to AP via PC, just log in: 192.168.4.1.

<div align="center">
  <img src="fig/config-1.png" alt="config-1">
</div>

4. You will see the following page. Follow the steps to configure your mining machine. The larger the UI refresh value, the higher the hash rate, and the hash rate will also increase when the screen is turned off.

<div align="center">
  <img src="fig/config-2.png" alt="config-2">
</div>

5. You can return to the configuration page at any time and refer to the [button](#buttons) operations.

6. In some areas, the pool is blocked by the local firewall. If you have an SSL encrypted channel, you can enable this option.

7. When you click **Save** it will take a while (10-15 seconds), do not reset the miner manually, just let it restart automatically.
***
#### firmware update

- Open the dir **'firmware/heltec-vision-master-t190'**, connect your Miner to your computer, then try to click **fw_update.exe**.

<div align="center">
  <img src="fig/fw.png" alt="fw">
</div>

- It would be better that there is only one COM port on your computer, **fw_update.exe** search the COM list on your computer and select the largest COM port index as the target port. So if there are more than one COMx, make sure the T190 COM port index is the largest one on your computer, just as below：

<div align="center">
  <img src="fig/comx.jpg" alt="comx">
</div>

- If some error occur when you update the firmware as below, one of the solutions as follow: 

##### Error:
<div align="center">
  <img src="fig/fwup-failed.png" alt="fw failed">
</div>

##### solutions:

  a). Hold on **boot** button;

  b). Wait 1s;

  c). Then click **reset** button;

  d). Wait 1s;

  e). Release **reset** button;

  f). Wait 1s;

  g). Release **boot** button;

  h). Click **fw_update.exe**.


## How to Usage

- ESP32 implementing stratum protocol to mine on solo pool. Pool can be changed but originally works with a low difficulty pool [public-pool.io](https://web.public-pool.io/).



## Contact
- We are committed to supporting more models of Arduino development boards.
- Anything do not work as your expectation, just let us know.

| Email                   |  Telegram                       |
| :-----------------:     |  :-----------------:            |
|nmminer1024@gmail.com    |  https://t.me/+IYFC1D0al1E5Yjdl |


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

### (2024.08.13) - v0.2.02
- Features:
  - BTC solo miner base on esp32s3 series 
  - Up to **118kH/s** 
  - ssl connection support
  - Screen auto off in 60s
  - Real time clock
  - Configuration on websever, it's easy enough to build your first BTC Miner.
  - WiFi signal strength on screen.
- Fixed:
  - Mining status clean issues.
- Modify:
  - None
- Baord support
  - [Heltec Vision Master T190](https://www.aliexpress.us/item/1005007449552504.html)


### (2024.08.10) - v0.2.01
- Features:
  - BTC solo miner base on esp32s3 series 
  - Up to **118kH/s** 
  - ssl connection support
  - Screen auto off in 60s
  - Real time clock
  - Configuration on websever, it's easy enough to build your first BTC Miner.
  - WiFi signal strength on screen.
- Fixed:
  - **Configuration of user BTC address not effective issue.**
- Modify:
  - Contact us, telegram group add.
  - Modify firmware update tools, make it easy to update firmware.
- Baord support
  - [Heltec Vision Master T190](https://www.aliexpress.us/item/1005007449552504.html)

### (2024.08.09) - v0.1.55
- Features:
  - BTC solo miner base on esp32s3 series 
  - Up to **118kH/s** 
  - ssl connection support
  - Screen auto off in 60s
  - Real time clock
  - Configuration on websever, it's easy enough to build your first BTC Miner.
  - WiFi signal strength on screen.
- Fixed:
  - Some ssl issues.
- Modify:
  - Add some log on loading screen.
  - Hashrate upto 118K when screen off.
- Baord support
  - [Heltec Vision Master T190](https://www.aliexpress.us/item/1005007449552504.html)

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
  - [Heltec Vision Master T190](https://www.aliexpress.us/item/1005007449552504.html)

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
