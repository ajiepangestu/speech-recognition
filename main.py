import speech_recognition as sr


r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
robot = True
jplay = True
while(jplay):
    try:
        if robot:
            print('''             .andAHHAbnn.
           .aAHHHAAUUAAHHHAn.
          dHP^~"        "~^THb.
    .   .AHF                YHA.   .
    |  .AHHb.              .dHHA.  |
    |  HHAUAAHAbn      adAHAAUAHA  |
    I  HF~"_____        ____ ]HHH  I
   HHI HAPK""~^YUHb  dAHHHHHHHHHH IHH
   HHI HHHD> .andHH  HHUUP^~YHHHH IHH
   YUI ]HHP     "~Y  P~"     THH[ IUP
    "  `HK                   ]HH'  "
        THAn.  .d.aAAn.b.  .dHHP
        ]HHHHAAUP" ~~ "YUAAHHHH[
        `HHP^~"  .annn.  "~^YHH'
         YHb    ~" "" "~    dHF
          "YAb..abdHHbndbndAP"
           THHAAb.  .adAHHF
            "UHHHHHHHHHHU"
              ]HHUUHHHHHH[
            .adHHb "HHHHHbn.
     ..andAAHHHHHHb.AHHHHHHHAAbnn..
.ndAAHHHHHHUUHHHHHHHHHHUP^~"~^YUHHHAAbn.
  "~^YUHHP"   "~^YUHHUP"        "^YUP^"
       ""         "~~"
''')
            print("Author : Ajie Pangestu")
            robot = False
        with mic as source:
            print("J.A.R.V.I.S. mendengarkan......")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        print("Tuan mengatakan\t: " + r.recognize_google(audio))
        if str(r.recognize_google(audio)) == "keluar":
            jplay = False
            print("Program J.A.R.V.I.S. dihentikan......")
    except:
        print("Tuan tidak mengatakan mengatakan apapun......")