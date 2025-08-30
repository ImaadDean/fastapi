from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pywhatkit as pwk
from datetime import datetime, timedelta
import time

app = FastAPI(title="Hello API", version="1.0.0")

class WhatsAppMessage(BaseModel):
    phone_number: str
    message: str
    delay_minutes: int = 1

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/send-whatsapp")
def send_whatsapp_message(message_data: WhatsAppMessage):
    try:
        # Calculate send time (current time + delay)
        now = datetime.now()
        send_time = now + timedelta(minutes=message_data.delay_minutes)
        
        # Format phone number (ensure it starts with country code)
        phone = message_data.phone_number
        if not phone.startswith('+'):
            phone = '+' + phone
        
        # Send WhatsApp message using pywhatkit
        pwk.sendwhatmsg(
            phone_no=phone,
            message=message_data.message,
            time_hour=send_time.hour,
            time_min=send_time.minute,
            wait_time=15,  # Wait 15 seconds for WhatsApp Web to load
            tab_close=True,  # Close tab after sending
            close_time=3  # Close after 3 seconds
        )
        
        return {
            "status": "success",
            "message": "WhatsApp message scheduled successfully",
            "phone_number": phone,
            "scheduled_time": send_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send WhatsApp message: {str(e)}")

@app.post("/send-whatsapp-now")
def send_whatsapp_now(message_data: WhatsAppMessage):
    try:
        # Format phone number
        phone = message_data.phone_number
        if not phone.startswith('+'):
            phone = '+' + phone
        
        # Send WhatsApp message instantly
        pwk.sendwhatmsg_instantly(
            phone_no=phone,
            message=message_data.message,
            wait_time=15,
            tab_close=True,
            close_time=3
        )
        
        return {
            "status": "success",
            "message": "WhatsApp message sent instantly",
            "phone_number": phone
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send WhatsApp message: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
