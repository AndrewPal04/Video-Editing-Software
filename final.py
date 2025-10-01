import time
import cv2

print("Hello, welcome to the video editing software!")
time.sleep(1)
while True:
    w=str(input("What video file do u want to edit (type 'q' to quit): "))
    if w=="q":
        break
    print("What do u wanna do with the video")
    print(" 1. Make it black and white")
    print(" 2. Give coordinates to draw something onto the video")
    print(" 3. Change the fps of the video")
    print(" 4. Crop videos")
    print(" 5. Resize the video")
    print(" 6. Rotate the video")
    print(" 7. Change the color (RGB) of the video")
    print(" 8. Quit editting")
    e=str(input("Answer:"))
    vid_capture = cv2.VideoCapture(w)
    frame_width = int(vid_capture.get(3))
    frame_height = int(vid_capture.get(4))
    frame_size=(frame_width,frame_height)
    if e == "8":
        break
    if e=="2":
        print("1. circle")
        print("2. square/rectangle")
        print("3. text")
        print("4. line")
        
        z=str(input("answer:"))
        if z=="1":
            while True:
                B=int(input("Enter Blue value (0-255): "))
                G=int(input("Enter Green value (0-255): "))
                R=int(input("Enter Red value (0-255): "))
                if B>=0 and B<=255 and G>=0 and G<=255 and R>=0 and R<=255:
                    BGR=(B,G,R)
                    break
                else:
                    print("omg actually enter values between 0-255")

            print("put in the values for x and y")
            x=int(input("x: "))
            y=int(input("y: "))
            center=(x,y)
            axis=(250,250)
        elif z=="2":

            while True:
                B=int(input("Enter Blue value (0-255): "))
                G=int(input("Enter Green value (0-255): "))
                R=int(input("Enter Red value (0-255): "))
                if B>=0 and B<=255 and G>=0 and G<=255 and R>=0 and R<=255:
                    BGR=(B,G,R)
                    break
                else:
                    print("omg actually enter values between 0-255")
            print("put in the values for x and y")
            x1=int(input("starting x:"))
            y1=int(input("starting y: "))
            x2=int(input("ending x:"))
            y2=int(input("ending y: "))
            pointA=(x1,y1)
            pointB=(x2,y2)
            t=int(input("how thick do u want ur rectangle???"))
        elif z=="3":

            textt=str(input("what u wanna say?:"))
            orgx=int(input("x:"))
            orgy=int(input("y:"))
            while True:
                B=int(input("Enter Blue value (0-255): "))
                G=int(input("Enter Green value (0-255): "))
                R=int(input("Enter Red value (0-255): "))
                if B>=0 and B<=255 and G>=0 and G<=255 and R>=0 and R<=255:
                        BGR=(B,G,R)
                        break
                else:
                    print("omg actually enter values between 0-255")
                    
        elif z=="4":
            print("what ur coordinates")
            x1=int(input("starting x:"))
            y1=int(input("starting y: "))
            x2=int(input("ending x:"))
            y2=int(input("ending y: "))

            while True:
                B=int(input("Enter Blue value (0-255): "))
                G=int(input("Enter Green value (0-255): "))
                R=int(input("Enter Red value (0-255): "))
                if B>=0 and B<=255 and G>=0 and G<=255 and R>=0 and R<=255:
                        BGR=(B,G,R)
                else:
                    print("omg actually enter values between 0-255")
    elif e == "3":
        fpsnew=int(input("what do u want for ur new fps??? "))
    elif e == "4":
        newy1=int(input("where should we start the crop (0 is top)?")) 
        print("Where should we end the crop (",frame_height,"is bottom)")
        newy2=int(input())
        newx1=int(input("where should we start the crop (0 is left)?")) 
        print("Where should we end the crop (",frame_width,"is right)")
        newx2=int(input())

    elif e == "5":
        up_w =int(input("how wide do u want the vid to be?"))
        up_h =int(input("how tall do u want ur vid to be?"))
        up_points = (up_w, up_h)
    elif e == "6":
        center = (frame_width/2,frame_height/2)
        scale= 1.0
        newrotate=int(input("how many degrees do u want to rotate it?"))
        M = cv2.getRotationMatrix2D(center,newrotate,scale)
    elif e == "7":
        print("0. Blue\n1. Green\n2. Red")
        colors=int(input("what color u want to edit?"))
        newValue=int(input("How much of that color do you want? (0 means none, 255 means max): "))

    if (vid_capture.isOpened() == False):
        print("Error opening the video file")
        quit()
    else:
        fps = int(vid_capture.get(5))
        frame_count = vid_capture.get(7)

    frame_width = int(vid_capture.get(3))
    frame_height = int(vid_capture.get(4))
    frame_size = (frame_width,frame_height)
    name=str(input("uh what do u wanna name ur new file: "))
    new_name=(name+".mp4")

    frame_size_out = frame_size
    if e == "4":
        if newx2 < newx1:
            newx1, newx2 = newx2, newx1
        if newy2 < newy1:
            newy1, newy2 = newy2, newy1
        frame_size_out = (max(1, newx2 - newx1), max(1, newy2 - newy1))
    elif e == "5":
        frame_size_out = up_points

    if e == "3":
        output=cv2.VideoWriter(new_name,cv2.VideoWriter_fourcc(*'mp4v'),fpsnew,frame_size_out)
    else:
        output=cv2.VideoWriter(new_name,cv2.VideoWriter_fourcc(*"mp4v"),fps,frame_size_out)
    while(vid_capture.isOpened()):
        ret, frame = vid_capture.read()
        if ret == True:
                if e=="1":
                    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                    frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
                if e=="2":
                    if z=="1":
                        cv2.ellipse(frame,center,axis,0,0,360,BGR,thickness=10)
                    elif z=="2":
                        cv2.rectangle(frame,pointA,pointB,BGR,t)
                    elif z=="3":
                        cv2.putText(frame,textt,(orgx,orgy),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.5, color = BGR)
                    elif z=="4":
                        cv2.line(frame,(x1,y1),(x2,y2),BGR, thickness=10)
                if e=="4":
                    frame = frame[newy1:newy2, newx1:newx2]
                if e == "5":
                    frame = cv2.resize(frame, up_points, interpolation= cv2.INTER_LINEAR)
                if e == "6":
                    frame=cv2.warpAffine(frame,M,(frame_width,frame_height))
                if e == "7":
                    frame[:,:,colors] =newValue
                output.write(frame)
        else:
            print("Stream disconnected")
            break

    vid_capture.release()
    output.release()
    print("ye ur video is edited :D")
    print("Take a look at",new_name)
