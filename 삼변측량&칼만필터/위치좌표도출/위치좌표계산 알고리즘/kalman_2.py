import kalman

#Make the Kalman

def Kalman_2(NX,NY):

        # Create some random temperature data

        random_data = (NX,NY)

 

        # Initialise the Kalman Filter

 

        A = 1  # No process innovation

        C = 1  # Measurement

        B = 0  # No control input

        Q = 0.005  # Process covariance

        R = 1  # Measurement covariance

        x = 0  # Initial estimate

        P = 1  # Initial covariance

 

        kalman_filter = kalman.SingleStateKalmanFilter(A, B, C, x, P, Q, R)

 

        # Empty lists for capturing filter estimates

        kalman_filter_estimates = []

 

        # Simulate the data arriving sequentially

        for data in random_data:

            kalman_filter.step(0, data)

            kalman_filter_estimates.append(kalman_filter.current_state())

#       print("kalman values: ", kalman_filter_estimates[0]," : ", kalman_filter_estimates[1])

        return kalman_filter_estimates[0],kalman_filter_estimates[1]


def Kalman_3(Rssi):

        # Create some random temperature data
        print("kalman_3 ok")
        random_data = Rssi

 

        # Initialise the Kalman Filter

 

        A = 1  # No process innovation

        C = 1  # Measurement

        B = 0  # No control input

        Q = 0.005  # Process covariance

        R = 1  # Measurement covariance

        x = 0  # Initial estimate

        P = 1  # Initial covariance

 

        kalman_filter = kalman.SingleStateKalmanFilter(A, B, C, x, P, Q, R)

 

        # Empty lists for capturing filter estimates

        kalman_filter_estimates = []

 

        # Simulate the data arriving sequentially

        for data in random_data:

            kalman_filter.step(0, data)

            kalman_filter_estimates.append(kalman_filter.current_state())

#       print("kalman values: ", kalman_filter_estimates[0]," : ", kalman_filter_estimates[1])

        return kalman_filter_estimates
