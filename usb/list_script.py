import usb.core
import usb.util

devs = usb.core.find(find_all=True)
for d in devs:
    print d
