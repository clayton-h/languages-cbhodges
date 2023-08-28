# Enable WSL2 in windows

## To start powershell as admin:
1. Using the Start menu
1. Click the Start button.
1. Type "PowerShell" in the search bar.
1. Right-click the Windows PowerShell app and select "Run as administrator".

In this shell, run the following commands:

```sh
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /provisioned
wsl --install-kernel
wsl --set-default-version 2
```
