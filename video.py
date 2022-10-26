#скачать пробное видео по ссылке https://drive.google.com/file/d/1jnVE-Bu3FQogeBDgx9l4zXE5I4CL41xq/view?usp=sharing

import numpy as np
import cv2
from skimage import data, filters

# обращение к видео
cap = cv2.VideoCapture('/video2.mp4')

# Выбор случайных 40 кадров
frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=40)

# Сохраняем кадры в массиве
frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)

# Вычисляем медиану по оси времени
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)

# Показываем средний кадр (фон без динамики)
cv2.imshow('frame', medianFrame)
cv2.waitKey(0)

# Сбросить номер кадра на 0
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Средний кадр (Фон) конвертируется в серые оттенки
grayMedianFrame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)

# Перебор всех кадров
ret = True
while(ret):

  # Обращение к кадру
  ret, frame = cap.read()
  # КОнкретный кадр в конверт в серый оттенок
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Вычисляем абсолютную разницу между конкретным кадром и средним кадром
  dframe = cv2.absdiff(frame, grayMedianFrame)
  # Установка порога бинаризации (чтобы отображалась разница)
  th, dframe = cv2.threshold(dframe, 30, 255, cv2.THRESH_BINARY)
  # Отобразить
  cv2.imshow('frame', dframe)
  cv2.waitKey(20)

# Вывести видео
cap.release()

# Всё закрыть
cv2.destroyAllWindows()
