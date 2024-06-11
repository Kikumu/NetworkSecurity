'''
with open(OUTPUT_FILE_PATH, 'w') as output_file:
    capture = pyshark.LiveCapture(interface=CAPTURE_INTERFACE)
    print(capture)
    print("starting..")
    for packet in capture.sniff_continuously():
        print("in loop")
        output_file.write(f'{packet}\n')
        print(packet)
        print("end loop")
'''
