## Question
- 2_data_format: ความเข้าใจเรื่อง Data format ของ API
![](/assets/q_data_format.png)
## Response Section

Data Format ของ API คือรูปแบบที่ใช้สำหรับรับและส่งข้อมูลระหว่าง Client และ Server โดยทั้งสองฝั่งต้องเข้าใจโครงสร้างและชนิดของข้อมูลตรงกัน

ตัวอย่างเช่น การสมัคร User ของเกมออนไลน์ โดยมีผู้สมัครชื่อ "จตุพร"

Client ส่งข้อมูลไปยัง Server โดยใช้

Content-Type: application/json

Request Body:

{
  "name": "จตุพร",
  "idCard": "1234567890123",
  "registeredAt": "2026-09-16T06:00:00+07:00"
}

โดยกำหนด Data Type เช่น

name เป็น String

idCard เป็น String

registeredAt เป็น Date/Time ในรูปแบบ ISO 8601

Response กรณีสมัครสำเร็จ

{
  "data": {
    "userId": 1001,
    "name": "จตุพร",
    "registeredAt": "2026-09-16T06:00:00+07:00"
  }
}

ตัวอย่าง HTTP Status:

201 Created

Response กรณีชื่อ User ซ้ำ

{
  "error": {
    "code": "USER_DUPLICATE",
    "message": "Username already exists. Please select another name."
  }
}

ตัวอย่าง HTTP Status:

409 Conflict
