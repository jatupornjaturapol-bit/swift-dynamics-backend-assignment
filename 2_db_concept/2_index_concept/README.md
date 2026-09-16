## Question
- 2_index_concept: อธิบายเกี่ยวกับการทำ Index
![](/assets/q_indexing.png)
## Response Section
Index ให้คิดเหมือน สารบัญของหนังสือ
สมมุติเราเก็บหนังสืออันหนึ่งที่มี 100,000 หน้าหากต้องการหาหน้าที่ 9999 ปกติคือต้องเปิดทีละหน้าแค่ index สามารถชี้ไปหาหน้าที่ 9999 ได้เลย

---
ตัวอย่าง:
CREATE INDEX idx_users_email
ON users(email);
หมายถึงเราสร้าง Index สำหรับ email
เมื่อค้นหา:
SELECT *
FROM users
WHERE email = 'jatuporn@gmail.com';
Database สามารถใช้ Index เพื่อหาตำแหน่งข้อมูลได้เร็วขึ้น แทนการไล่ทุก Row
-

สรุป:
ไม่มี Index → ไล่หาข้อมูลจำนวนมาก
มี Index → ใช้โครงสร้างที่จัดไว้ช่วยตัดพื้นที่ค้
หา → เจอเร็วขึ้น
