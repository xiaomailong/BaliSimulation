#import ctypes
from ctypes import *
import os


def testMain():
#    print("In testMain......")
    obj = CDLL("./libDecode.so")
    
    tele_ori=b" 98 3B E6 32 7B 23 75 ED 96 19 46 9A 3D 0E F2 A6 3D 2D 7C 37 88 CD F7 77  C3 DD EB D1 82 65 A7 F5 22 D4 BB D4 75 3A DC 4D 34 2F 5E 63 91 C7 B3 92 96 BA 7D 7B EC DB 14 2F 24 5C 87 F8 EA 7D 3E 0D 2B F6 F2 F1 AB 99 5B 7E DF 45 3C 41 3C AE 77 C2 3B E9 7C 47 5A 7D F2 C5 5D 49 AA F3 30 6774 FC4A C7 59 F2 D9 ED 5E F9 13 E2 E6 17 85 92 CD 7B 0F D9 10 1B 51 67 29 2F  B5 DF 89 B8 AC DE DA 7C"

    print("\nDecoding......\n")
    output = create_string_buffer(b'\0'*1000)
    output2 = create_string_buffer(b'\0'*1000)
    obj.Decode(tele_ori,byref(output),byref(output2))

  #  output = c_char_p()
  #  output= b"outputResult"
#    print("next step")
   # output = "fjalksjfaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadalfjlajfdlkaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
   
   
  #  obj.Decode(tele_ori,output)
    print(output.value.decode('utf-8'))
    print(output2.value.decode('utf-8'))


def DecodeMain():
    obj = CDLL("./libDecode.so")
    tele_ori=b" 98 3B E6 32 7B 23 75 ED 96 19 46 9A 3D 0E F2 A6 3D 2D 7C 37 88 CD F7 77  C3 DD EB D1 82 65 A7 F5 22 D4 BB D4 75 3A DC 4D 34 2F 5E 63 91 C7 B3 92 96 BA 7D 7B EC DB 14 2F 24 5C 87 F8 EA 7D 3E 0D 2B F6 F2 F1 AB 99 5B 7E DF 45 3C 41 3C AE 77 C2 3B E9 7C 47 5A 7D F2 C5 5D 49 AA F3 30 6774 FC4A C7 59 F2 D9 ED 5E F9 13 E2 E6 17 85 92 CD 7B 0F D9 10 1B 51 67 29 2F  B5 DF 89 B8 AC DE DA 7C"

    output = c_char_p
    output = b"Decode result"
    #output = "fjalksjfaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadalfjlajfdlkaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    #rst = obj.Decode(tele_ori,output)
    print("\n\nHERE COMES DECODING.....\n")
    obj.Decode(tele_ori,output)
    #print(output)
    print(output.decode('utf-8'))

   # data = ctypes.string_at(rst, -1)
   # print(data)
#    data = data.decode('utf-8')
    #print("\n\nHERE COMES DECODING.....\n")
   # print(data)



def Decode(tele_ori):
    print("tele_ori is")
    print(tele_ori)
    print("Step111111")
    print("current work directory")
    print(os.getcwd())
    obj = ctypes.CDLL("./bali/PyDecode/libDecode.so")
    print("Step22222")
    #tele_ori=" 98 3B E6 32 7B 23 75 ED 96 19 46 9A 3D 0E F2 A6 3D 2D 7C 37 88 CD F7 77  C3 DD EB D1 82 65 A7 F5 22 D4 BB D4 75 3A DC 4D 34 2F 5E 63 91 C7 B3 92 96 BA 7D 7B EC DB 14 2F 24 5C 87 F8 EA 7D 3E 0D 2B F6 F2 F1 AB 99 5B 7E DF 45 3C 41 3C AE 77 C2 3B E9 7C 47 5A 7D F2 C5 5D 49 AA F3 30 6774 FC4A C7 59 F2 D9 ED 5E F9 13 E2 E6 17 85 92 CD 7B 0F D9 10 1B 51 67 29 2F  B5 DF 89 B8 AC DE DA 7C";
    output = "fjalksjfaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadalfjlajfdlkaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    rst = obj.Decode(tele_ori,output)
    data = "\n\nHERE COMES DECODING.....\n"+ctypes.string_at(rst, -1).decode('utf-8')
    print(data)
    return data
   # print("\n\nHERE COMES DECODING.....\n")
   # print(data)

if __name__=="__main__":
    testMain()
