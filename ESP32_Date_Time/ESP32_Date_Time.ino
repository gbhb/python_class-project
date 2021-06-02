
#include <string.h>
#include <WiFi.h>
#include "FirebaseESP32.h"
#include "time.h"
#include <SPI.h>
#include <MFRC522.h>
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

void printLocalTime(){
  // 寻找新卡
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
//    Serial.println("没有找到卡");
    delay(1000);
    return;
  }
  // 选择一张卡
  if ( ! mfrc522.PICC_ReadCardSerial()) {
//    Serial.println("没有卡可选");
    delay(1000);
    return;
  }
   // 显示卡片的详细信息
//  Serial.print(F("卡片 UID:"));
  dump_byte_array(mfrc522.uid.uidByte, mfrc522.uid.size);
//  Serial.print(F("卡片类型: "));
  MFRC522::PICC_Type piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);
//  Serial.println(mfrc522.PICC_GetTypeName(piccType));
//  
  //停止 PICC
  mfrc522.PICC_HaltA();
  //停止加密PCD
  mfrc522.PCD_StopCrypto1();
  
//  struct tm timeinfo;
//  if(!getLocalTime(&timeinfo)){
//    Serial.println("Failed to obtain time");
//    return;
//  }
//  Serial.println(&timeinfo, "%A, %B %d %Y %H:%M:%S");
//  Serial.print("Day of week: ");
//  Serial.println(&timeinfo, "%A");
//  Serial.print("Month: ");
//  Serial.println(&timeinfo, "%B");
//  Serial.print("Day of Month: ");
//  Serial.println(&timeinfo, "%d");
//  Serial.print("Year: ");
//  Serial.println(&timeinfo, "%Y");
//  Serial.print("Hour: ");
//  Serial.println(&timeinfo, "%H");
//  Serial.print("Hour (12 hour format): ");
//  Serial.println(&timeinfo, "%I");
//  Serial.print("Minute: ");
//  Serial.println(&timeinfo, "%M");
//  Serial.print("Second: ");
//  Serial.println(&timeinfo, "%S");
//  char out_str[40]; 
//  strcat(out_str,"/python_final/");
//  strcat(out_str,"2021-5-24");
//  strcat(out_str,"/");
//  strcat(out_str,"02:55:56");
//  Serial.println(out_str);
//   if(Firebase.setString(firebaseData, out_str, "2945A659"))
//  {
//    Serial.println("PASSED");
//    Serial.println("PATH: " + firebaseData.dataPath());
//    Serial.println("TYPE: " + firebaseData.dataType());
//    Serial.println("ETag: " + firebaseData.ETag());
//    Serial.println("------------------------------------");
//    Serial.println();
//  }
//  else
//  {
//    Serial.println("FAILED");
//    Serial.println("REASON: " + firebaseData.errorReason());
//    Serial.println("------------------------------------");
//    Serial.println();
//  }

}

void dump_byte_array(byte *buffer, byte bufferSize) {

  read_rfid="";

  for (byte i = 0; i < bufferSize; i++) {
     read_rfid=read_rfid + String(buffer[i], HEX);
  }
  Serial.println(read_rfid);
}

void setup(){
  Serial.begin(115200);

  // Connect to Wi-Fi
//  Serial.print("Connecting to ");
//  Serial.println(ssid);
//  WiFi.begin(ssid, password);
//  while (WiFi.status() != WL_CONNECTED) {
//    delay(500);
////    Serial.print(".");
//  }
//  Serial.println("");
//  Serial.println("WiFi connected.");
//  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
//  Firebase.reconnectWiFi(true);
//  // Init and get the time
//  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
//  printLocalTime();
  SPI.begin();        // SPI开始
  mfrc522.PCD_Init(); // Init MFRC522 card
//  Serial.println("test-demo-start");
  
  //disconnect WiFi as it's no longer needed
//  WiFi.disconnect(true);
//  WiFi.mode(WIFI_OFF);
  
}

void loop(){
  delay(1000);
  printLocalTime();
}
