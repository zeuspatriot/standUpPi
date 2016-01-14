import faceDetection
import webbrowser
import distanceDetection
import time

dist = distanceDetection
f_lib = faceDetection
youtrack_url = 'https://maxymiser.myjetbrains.com/youtrack/rest/agile/EMEA%20Travel-83/sprint/Undefined?q=Assignee%3A+'
flag = True
tries = 0
# print f_lib.detect_face()
while flag:

    while dist.get_distance() > 90:
        dist.get_distance()
    else:
        arr = []
        photos = []
        print 'person num: ',tries
        if tries > 3:
            flag = False

        for ind in range(5):
            photos.append(f_lib.take_photo())
            print 'photo num: ', ind, ' taken'

        for photo in photos:
            if len(f_lib.detect_face_manual(photo)) > 0:
                current_face = f_lib.detect_face_manual(photo)[0]['faceId']
                arr.append(str(current_face))
                print 'Face detected'

        print arr
        print f_lib.identify_face(arr,'qwe',1).json()
        if len(f_lib.identify_face(arr, 'qwe', 1).json()[0]['candidates']) > 0:
            current_person = str(f_lib.identify_face(arr, 'qwe', 1).json()[0]['candidates'][0]['personId'])
            email = f_lib.get_person('qwe',current_person).json()['userData']
            print email
            webbrowser.open(youtrack_url+email, 0)

        else:
            print 'person is not recognized :('

        tries += 1
        time.sleep(5)
else:
    dist.cleanup()