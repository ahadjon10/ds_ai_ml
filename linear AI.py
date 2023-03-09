#Kutubxonalrni chaqirib olish
import matplotlib.pyplot as plt
import numpy as np

#Ma'lumotlarni kiritish
house_price = np.array([24,28,32,35,40,46])
area = np.array([50,61, 66, 71, 82, 90 ])

#To'g'ri hisoblash uchun funksiya
def forward(x):
    return x*w
#Xatolik (Loss) ning funksiyasi
def loss(x,y):
    y_pred = forward(x)
    return (y_pred-y)**2

#Grafikni yaratib olishimiz uchun kontaynerlar
w_list=[]
mse_list=[]

#w ni 0 dan 4 gacha oralig'ida hisblash
for w in np.arange(1.0,2.0,3.0):
    print("w={:.3f}".format(w))
    L_umum=0

    for x_hb_qiym, y_hb_qiym in zip(house_price, area):
        y_hb_bash = forward(x_hb_qiym)
        L_hb_qiym = loss(x_hb_qiym, y_hb_qiym)
        L_umum += L_hb_qiym
        print("\t", "{:.2f}, {:.2f}, {:.2f}, {:.2f}".format(x_hb_qiym, y_hb_qiym, y_hb_bash, L_hb_qiym))

    # Har bir ma'lumot uchun MSE ni hisoblaymiz
    print("MSE=", L_umum / len(house_price))  #len(x_soat)--> N
    w_list.append(w)
    mse_list.append(L_umum / len(house_price))

#Grafik natija
plt.plot(w_list, mse_list, color="r")
plt.ylabel('Loss')
plt.xlabel('w')
ax= plt.axes()
ax.set_facecolor('#030101')
plt.show()
