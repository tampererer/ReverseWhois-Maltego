# [Reverse Whois] Maltego Local Transforms
Maltego Local Transforms to use the following services.
- DomainEye - https://domaineye.com/
- PrePostSEO - https://www.prepostseo.com/reverse-whois-checker
- Viewdns - https://viewdns.info/

# Prerequisites
- Python 2.7.x + requests, re module
- Python 3.6.x will probably work.

# 必要なもの
- Python 2.7.x + requests, re モジュール
- Python 3.6.x でもたぶん動作します。

# Setup
- Put all python files into your working directory. (e.g. C:\Maltego\Transforms\ReverseWhois)
- Open Whoismind.mtz to import Maltego configuration.
- The current configuration uses the following directories, so you may have to change them according to your environment. (Maltego -> Transforms -> Transform Manager)  

  Command line = C:\Python27\python.exe  
  Working directory = C:\Maltego\Transforms\ReverseWhois

# セットアップ
- 全てのPythonファイルを、このTransform用に作ったディレクトリに置いてください。（例： C:\Maltego\Transforms\WebPulse）
- ReverseWhois.mtz を開いて、Maltegoの設定をインポートしてください。
- mtzファイルに含まれる設定では、下記のディレクトリが指定されていますが、自分の環境に合わせて変更してください。（Maltego -> Transforms -> Transform Manager）

  Command line = C:\Python27\python.exe  
  Working directory = C:\Maltego\Transforms\ReverseWhois

# Transforms
- [DomainEye] email_to_domain.py
- [PrePostSEO] email_to_domain.py
- [Viewdns] email_to_domain.py  
<img src="https://user-images.githubusercontent.com/16297449/42561523-4d4785ce-8534-11e8-8265-a552a8d47d5b.png" width="600">
