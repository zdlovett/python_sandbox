import usb.core
import usb.util

devs = usb.core.find(find_all=True)
numd = 0
for d in devs:
    print(d)
    numd += 1
print(f"number of detected devices:{numd}")
