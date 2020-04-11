# Speed Limit Sign Detection With Python And OpenCV
My high school open-source project uses for learning Python and OpenCV

## How does it work?
First, the program needs to input an image or a video. it was converted to grayscale for finding edges by ``` cv2.cvtColor() ``` function. Then, the program will detect shapes by exact contours (In this part you can custom contours as well.). At the same time, it will also detect text on a shape by Google Tesseract OCR. If they are in condition. Finally, the program will print the output by replacing a detection message into a result

## Getting Started
### Installing
You have installed Python 3.6.8 and Google Tesseract OCR. All requirements are available in ``` requirement.txt ```. You can easily install by using ``` pip install -r requirement.txt ```.

Python 3.6.8:
https://www.python.org/downloads/release/python-368/

Google Tesseract OCR: 
https://tesseract-ocr.github.io/tessdoc/Home.html

### Demo and Applying
For an image version, Demo images are available in demo folder. You can also change demo location image in line ``` image = cv2.imread('img/1.jpg') ``` to your specific location image.

For a video version, You can also change default webcam in line ``` capture = cv2.VideoCapture(0) ``` to your webcam.

## Screenshot

![Image description](https://o2ckww.sn.files.1drv.com/y4m7Ka39pA2PT4BSq6vEAt3HMKkwZYL1JcLHEDijd3oZ-sYIWroTrrIJpIUNVSAnAuALX1GVESEWXQN_0SEANEoaITAlBlKJVRnEi_9Lc7dUaa3kBP-NaVexQQiPg3JzZmu-RBvk3Qc04rmoRABI2Rre-JR_FU7BkhPpY19ZJXdC_5sDv_xXCKvVFymV8SA3osvkYjGmrafYvfW2TS_m02UBQ?width=1920&height=1080&cropmode=none)

![Image description](https://o2cdfa.sn.files.1drv.com/y4mB1klVEZuztR-Py2NyKKnh_l6uWsBVxzrmeCDG-kEqHk1UW3e_lK-rcmES6g7azCUgTtJ8eng-WnFlvE5QTAO45IPmx9hPLev-vL9NpqWgMq1hUqM36amXGClFdyvGTabTtgkQvcbgt5CIA-IuvRQktw3KAYQp1ZbUbqiZuv6-euopKVxbDXY5-AIS3ehREbvvOx8mpGKxn5gh-pA9j1ryw?width=1920&height=1080&cropmode=none)

![Image description](https://o2aloa.sn.files.1drv.com/y4mpJY6a_E_Ptyd0T7e-vrhATGdONJdFa7SSHnPCPqDTs_1k_-YMG--byOKQ4_XRPNo4ZkYhNcSmgOrBx9Df52QOGM-CF8SZDMHChUIt0UD3RUkJIDgzPkt_qap8hNTVpQqquk59OybZBz2uBseCQerf1yPIfXth9MhMlVd2ZSE3smIgOJuSvWDKT01gdTQQrYTdJ3WNGcV-baEoLQPJuxxEg?width=1920&height=1080&cropmode=none)

## Author
* **Sippawit Thammawiset** - A high school student
