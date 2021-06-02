#include <string.h>
#include <WiFi.h>
#include "FirebaseESP32.h"
#include <SPI.h>
#include <MFRC522.h>
#include "time.h"
#define FIREBASE_HOST "iotbase-7acc0-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "effGDQfVBkjd19yB5vJ86kN6gkxB4yOTArSoNPAi"
#define RST_PIN        22 //15           //5 配置针脚
#define SS_PIN          21  //5        //4
const char* ssid     = "TP-Link_AA5C";
const char* password = "065744330";
FirebaseData firebaseData;
const char* ntpServer = "pool.ntp.org";
const long  gmtOffset_sec = 28800;
const int   daylightOffset_sec = 0;


MFRC522 mfrc522(SS_PIN, RST_PIN);   // 创建新的RFID实例
MFRC522::MIFARE_Key key;
String read_rfid;  //定义变量，用于存储要输出显示的字符串内容


void setup() {
  Serial.begin(115200); // 设置串口波特率为9600
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected.");
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
  
  SPI.begin();        // SPI开始
  mfrc522.PCD_Init(); // Init MFRC522 card
  Serial.println("test-demo-start");
  
  //disconnect WiFi as it's no longer needed
  WiFi.disconnect(true);
  WiFi.mode(WIFI_OFF);
  
  
}
 
 
void loop() {
  // 寻找新卡
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    Serial.println("没有找到卡");
    delay(1000);
    return;
  }
 
  // 选择一张卡
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    Serial.println("没有卡可选");
    delay(1000);
    return;
  }
 
 
  // 显示卡片的详细信息
  Serial.print(F("卡片 UID:"));
  dump_byte_array(mfrc522.uid.uidByte, mfrc522.uid.size);
  Serial.print(F("卡片类型: "));
  MFRC522::PICC_Type piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);
  Serial.println(mfrc522.PICC_GetTypeName(piccType));
  
  //停止 PICC
  mfrc522.PICC_HaltA();
  //停止加密PCD
  mfrc522.PCD_StopCrypto1();
 
  delay(2000);
  
}
 
/**
   将字节数组转储为串行的十六进制值
*/
void dump_byte_array(byte *buffer, byte bufferSize) {

  read_rfid="";

  for (byte i = 0; i < bufferSize; i++) {
     read_rfid=read_rfid + String(buffer[i], HEX);
  }
  Serial.println(read_rfid);
  char out_str[40]; 
  strcat(out_str,"/python_final/");
  strcat(out_str,"2021-5-24");
  strcat(out_str,"/");
  strcat(out_str,"02:55:52");
  Serial.println(out_str);
  Firebase.setString(firebaseData, out_str, read_rfid);
  Firebase.setString(firebaseData, out_str, read_rfid);
  Firebase.setString(firebaseData, out_str, read_rfid);
  Firebase.setString(firebaseData, out_str, read_rfid);
  
  Firebase.setString(firebaseData, out_str, read_rfid);
  if (Firebase.setString(firebaseData, out_str, read_rfid))
  {
    Serial.println("PASSED");
    Serial.println("PATH: " + firebaseData.dataPath());
    Serial.println("TYPE: " + firebaseData.dataType());
    Serial.println("ETag: " + firebaseData.ETag());
    Serial.println("------------------------------------");
    Serial.println();
  }
  else
  {
    Serial.println("FAILED");
    Serial.println("REASON: " + firebaseData.errorReason());
    Serial.println("------------------------------------");
    Serial.println();
  }
}
//char* dump_byte_array(byte *buffer, byte bufferSize) {
//  char* h= new char[20];
//  for (byte i = 0; i < bufferSize; i++) {
////  Serial.print(buffer[i] < 0x10 ? " 0" : " ");
//    Serial.println(buffer[i], HEX);
//    char buf = (char)buffer[i];
//    const char *b=&buf;
//    Serial.println(b);
//  strcat(h,b);
//  Serial.println(h);
////Serial.print(buffer[i]);
//  }
//  return h;
//}
 
 
//void GetCode(byte blockAddr)
//{
//    //byte blockAddr      =1;
//  MFRC522::StatusCode status;
//  byte buffer[18];
//    byte size = sizeof(buffer);
////  if (status != MFRC522::STATUS_OK) {
////    Serial.print(F("身份验证失败？或者是卡链接失败"));
////    Serial.println(mfrc522.GetStatusCodeName(status));
////    return;
////  }
// 
//    // 从块儿读取数据
//    Serial.print(F("读取块儿的数据在：")); Serial.print(blockAddr);
//    Serial.println(F("块 ..."));
//    status = (MFRC522::StatusCode) mfrc522.MIFARE_Read(blockAddr, buffer, &size);//读取size个第blockAddr块的数据到buffer
// 
//    Serial.print(F("数据内容在第 ")); 
//    Serial.print(blockAddr); 
//    Serial.println(F(" 块:"));
//    dump_byte_array(buffer, 16); 
//    Serial.println();//输出第4块的数据
//    Serial.println();
//}
