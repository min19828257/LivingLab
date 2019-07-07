import kalman_2

#삼변측량 알고리
def Trilateration(data):
        R_1 = float(data[0]);R_2 = float(data[1]); R_3 = float(data[2])

        x_1 = 1;x_2 = 100;x_3 = 5
        y_1 = 2;y_2 = 4;y_3 = 6     

        A_1 = (-2*x_1 + 2*x_2)
        B_1 = (-2*y_1 + 2*y_2)
        C_1 = (R_1*R_1) - (R_2*R_2) - (x_1*x_1) + (x_2*x_2) - (y_1*y_1) + (y_2*y_2)
        D_1 = (-2*x_2) + (2*x_3)
        E_1 = (-2*y_2) + (2*y_3)
        F_1 = (R_2*R_2) - (R_3*R_3) - (x_2*x_2) + (x_3*x_3) - (y_2*y_2) + (y_3*y_3)
        X = (C_1*E_1 - F_1*B_1)/10 #(E_1*A_1 - B_1*D_1)
        Y = (C_1*D_1 - A_1*F_1)/10 #(B_1*D_1 - A_1*E_1)
        print("(E_1*A_1 - B_1*D_1) : ",E_1*A_1 - B_1*D_1)
        print("(B_1*D_1 - A_1*E_1) : ",B_1*D_1 - A_1*E_1)
        X,Y = kalman_2.Kalman_2(X,Y)
        return str(X)+","+str(Y)
