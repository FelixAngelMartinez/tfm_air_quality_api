from fastapi import FastAPI
from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.protocol.models import CloudToDeviceMethod
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException,status
import os
from api import schemas
import logging

CONNECTION_STRING = ""
#CONNECTION_STRING = os.environ["CONNECTION_STRING"]

app = FastAPI()

@app.get(path="/", status_code=status.HTTP_200_OK)
def read_devices():
    logging.info("read_devices api method")     
    try:
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)
        devices = registry_manager.get_devices()
        print(*devices, sep = "\n")
        json_compatible_item_data = jsonable_encoder(devices)
    except Exception as ex:
        print("Unexpected error {0}".format(ex))
    return JSONResponse(content=json_compatible_item_data)

# https://docs.microsoft.com/en-us/python/api/azure-iot-hub/azure.iot.hub.protocol.operations.devicemethodoperations?view=azure-python-preview
@app.post(path='/method', status_code=status.HTTP_200_OK)
def invoque_method(request: schemas.Method):    
    logging.info("invoque_method api method")
    device_id = request.device.lower()
    method_name = request.method.lower()
    method_payload =  int(request.payload)
    print(device_id)
    print(method_name)
    print(method_payload)
    available_methods = ["start", "stop", "buzzersound", "stopbuzzer", "setcolorrgb", "calibratesgp30", "autoCalibrationsgp30", "calibratemhz19", "modifyautocalibrationmhz19"]
    if method_name in available_methods:
        logging.info("Method: %s is inside available methods", method_name) 
        try:
            registry_manager = IoTHubRegistryManager(CONNECTION_STRING)
            direct_method_request = CloudToDeviceMethod(method_name=method_name, payload=method_payload)
            response = registry_manager.invoke_device_method(device_id=device_id, direct_method_request=direct_method_request)
        except Exception as ex:
            print("Unexpected error {0}".format(ex))
    else:
        logging.error("Method: %s is NOT inside available methods", method_name) 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Method {method_name} is not available")    
    return

