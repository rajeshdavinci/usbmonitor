import notify2
import glib

from pyudev import Context, Monitor
from pyudev.glib import GUDevMonitorObserver as MonitorObserver

context = Context()
monitor = Monitor.from_netlink(context)

monitor.filter_by(subsystem='usb')
observer = MonitorObserver(monitor)



def device_event(observer, action, device):
    product = str(device.get('ID_MODEL'))
    productid = str(device.get('ID_MODEL_ID'))
    vendor =  str(device.get('ID_VENDOR'))
    vendorid = str(device.get('ID_VENDOR_ID'))   
    icon_path = "/opt/usbmonitor/notification.png"
    
    if product != "None":    
         
         if action == "add":
            notify2.init('USB Notification')
            n = notify2.Notification("New Device is added",' VendorID=' + vendorid + '\n' + ' ProductID=' + productid + '\n' + ' Manufacturer=' + vendor + '\n' + ' Product=' + product + '\n',icon=icon_path)
            n.set_timeout(1000)
            n.show()
         else: 
              notify2.init('USB Notification')
              n = notify2.Notification("Device is Removed",' VendorID=' + vendorid + '\n' + ' ProductID=' + productid + '\n' + ' Manufacturer=' + vendor + '\n' + ' Product=' + product + '\n',icon=icon_path)
              n.set_timeout(1000)
              n.show()


observer.connect('device-event', device_event)
monitor.start()


glib.MainLoop().run()

